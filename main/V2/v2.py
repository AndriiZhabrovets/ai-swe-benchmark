import time
import sys
import os
import pandas as pd
import json
import subprocess
import tempfile
import tracemalloc
import logging
import openai
from dotenv import load_dotenv
import anthropic
import google.generativeai as genai
import matplotlib.pyplot as plt
from mistralai import Mistal
# Connecting the paths of all problems
sys.path.insert(0, './main/problems/leetcode/easy')
sys.path.insert(0, './main/problems/leetcode/medium')
sys.path.insert(0, './main/problems/leetcode/hard')


sys.path.insert(0, './main/problems/generated')


logging.basicConfig(
    filename='./main/logs/benchmark.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


load_dotenv(dotenv_path='./main/.env')
openai_api_key = os.getenv("GPT_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
anth_api_key = os.getenv("CLAUDE_API_KEY")
mistral_api_key = os.getenv("MISTRAL_API_KEY")
genai.configure(api_key=gemini_api_key)
client_open = openai.OpenAI(api_key=openai_api_key)
client_anth = anthropic.Anthropic(api_key=anth_api_key)
client_mistr = Mistal(api_key=mistral_api_key)



class TestCase:
    def __init__(self, status, error_msg, runtime, memory):
        self.status = status
        self.error_msg = error_msg
        self.runtime = runtime
        self.memory = memory

easy_problems = [
    ["two_sum", "twoSum"],
    ["roman_to_int", "romanToInt"],
    ["longest_common_prefix", "longestCommonPrefix"],
    ["valid_parentheses", "isValid"],
    ["merge_two_lists", "mergeTwoLists"]
]
medium_problems = [
    ["add_two_numbers", "addTwoNumbers"],
    ["longest_substring", "lengthOfLongestSubstring"],
    ["longest_palindrome", "longestPalindrome"],
    ["reverse_integer", "reverse"],
    ["str_int_atoi", "myAtoi"]
]
hard_problems = [
    ["median_sorted_arrays", "findMedianSortedArrays"],
    ["regex_match", "isMatch"],
    ["merge_k_lists", "mergeKLists"],
    ["first_missing_positive", "firstMissingPositive"],
    ["trapping_rain_water", "trap"]
]

categories = {"easy_problems":easy_problems, "medium_problems":medium_problems, "hard_problems":hard_problems}

def load_test_cases(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def create_summary(st, dataset, total_success_count):
    success_count = 0

    for i, tcase in enumerate(st):
        if tcase.status:
            solved = "Success 🟢"
            success_count += 1
        else:
            solved = "Fail 🔴"

        msg = tcase.error_msg
        tm = tcase.runtime

        dataset["Test Case"].append(i)
        dataset["Status"].append(solved)
        dataset["Memory Usage (bytes)"].append(tcase.memory)
        dataset["Run Time (ms)"].append(tm)

        if not tcase.status:
            dataset["Error Message"].append(msg)
        else:
            dataset["Error Message"].append(None)

        logging.info(f"Test Case {i}: Status: {solved}, Run Time: {tm} ms, Memory Usage: {tcase.memory} mb, Error: {msg}")
        # print(f"\nTest Case {i}:")
        # print(f"Solution Status: {solved}")
        # print(f"Run Time: {round(tm, 3)} milliseconds")
        # print(f"Error Message: {msg}")
    
    if success_count == len(st):
        total_success_count += 1
    return total_success_count

def call_problem_subprocess(problem_name, args):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write('import sys\n')
        temp_file.write('sys.path.insert(0, \'./main/problems/leetcode/easy\')\n')
        temp_file.write('sys.path.insert(0, \'./main/problems/leetcode/medium\')\n')
        temp_file.write('sys.path.insert(0, \'./main/problems/leetcode/hard\')\n')
        temp_file.write('sys.path.insert(0, \'./main/problems/generated\')\n')

        temp_file.write(f'import {problem_name[0]}\n')
        temp_file.write(f'import json\n')
        temp_file.write(f'print(json.dumps({problem_name[0]}.{problem_name[1]}(*{args})))')
        temp_file.flush()
        start_time = time.time()
        tracemalloc.start()
        
        try:
            logging.debug(f"Starting subprocess for problem: {problem_name[0]} with args: {args}")
            result = subprocess.check_output([sys.executable, temp_file.name], stderr=subprocess.PIPE, text=True).strip()
            memory = tracemalloc.get_traced_memory()
            runtime = (time.time() - start_time) * 1000
            logging.info(f"Subprocess completed for problem: {problem_name[0]} in {runtime} ms with memory {memory[0]} bytes")
            return json.loads(result), runtime, memory[0], None
        except subprocess.CalledProcessError as e:
            logging.error(f"Error in subprocess for problem: {problem_name[0]}. Error: {e.stderr.strip()}")
            runtime = (time.time() - start_time) * 1000
            memory = tracemalloc.get_traced_memory()
            return None, runtime, memory[0], e.stderr
        finally:
            tracemalloc.stop()
            os.unlink(temp_file.name)
            logging.debug(f"Temporary file deleted for problem: {problem_name[0]}")

def clean_code(solution_code):
    """Remove markdown formatting from the AI-generated code."""
    if solution_code.startswith("```"):
        lines = solution_code.splitlines()
        # Remove the first line (e.g., ```python) and the last line (```)
        return "\n".join(lines[1:-1])
    return solution_code

def save_ai_file(problem_name, solution_code):
    """Save the AI-generated solution to a temporary Python file."""
    file_path = f"./main/problems/generated/{problem_name}.py"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(solution_code)

def generate_ai_solution(problem_name, prompts, model, provider):
    """Generates solution code for a given problem using OpenAI API."""
    system_prompt = prompts[problem_name][0]["system_prompt"]
    user_prompt = prompts[problem_name][0]["user_prompt"]


    try:
        if provider == "openai":
            response = client_open.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )
            solution_code = response.choices[0].message.content
        elif provider == "anthropic":
            response = client_anth.completions.create(
                model=model,
                system=system_prompt,
                 messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": user_prompt
                            }
                        ]
                    }
                ],
                max_tokens=2048,
                temperature=0.7
            )
            solution_code = response["completion"]
            
        elif provider == "gemini":
            response = genai.generate_text(
                model=model,
                prompt=f"system_prompt:{system_prompt}\nuser_prompt:{user_prompt}",
                temperature=0.7,
                max_output_tokens=2048
            )
            solution_code = response.result

        solution_code = response.choices[0].message.content
        solution_code = clean_code(solution_code)
       
        logging.info(f"Generated AI solution for problem: {problem_name}")
        return solution_code 
    except Exception as e:
        logging.error(f"Error generating AI solution for problem {problem_name}: {str(e)}")
        return None

def solution_check(problem_name, cases_data, prompts=None, use_ai=False, success_count=0, model=None, provider=None):
    results = []
    test_cases = cases_data[problem_name[0]]
    logging.info(f"Checking solution for problem: {problem_name[0]} with {len(test_cases)} test cases.")

    if use_ai:
        name = f"{problem_name[0]}_ai" 
        solution_code = generate_ai_solution(name, prompts, model, provider)
        if solution_code:
            save_ai_file(name, solution_code)
            problem_name = [name, problem_name[1]]

    for tcase in test_cases:
        sol, runtime, memory, error = call_problem_subprocess(problem_name, tcase["input"])
        if error:
            results.append(TestCase(False, error, runtime, memory))
            logging.warning(f"Test case failed with error: {error.strip()}")
        elif sol in tcase["expected_output"]:
            results.append(TestCase(True, None, runtime, memory))
            logging.info(f"Test case passed. Output: {sol}")
            success_count += 1
        else:
            results.append(TestCase(False, f"Incorrect output: {sol}", runtime, memory))
            logging.warning(f"Test case failed. Expected: {tcase['expected_output']}, Got: {sol}")
    return results, success_count

def average_measure(data):
    return [round(data["Run Time (ms)"].mean(),3), round(data["Memory Usage (bytes)"].mean(),3)]

def export_data(data, name):
    file_name = f'main/data/{name}.xlsx'
    data.to_csv(file_name, sep="\t")
    # print('DataFrame is written to Excel File successfully.')

def visualize_results(summary_df):
    # Bar Chart: Success Rate
    plt.figure(figsize=(10, 6))
    plt.bar(summary_df["Model"], 
            [float(rate.strip('%')) for rate in summary_df["Success Rate"]], 
            color='blue')
    plt.title("Success Rate by Model")
    plt.ylabel("Success Rate (%)")
    plt.xlabel("Model")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Success_Rate.png")
    plt.show()

    # Bar Chart: Average Runtime
    plt.figure(figsize=(10, 6))
    plt.bar(summary_df["Model"], summary_df["Average Runtime (ms)"], color='green')
    plt.title("Average Runtime by Model")
    plt.ylabel("Runtime (ms)")
    plt.xlabel("Model")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Average_Runtime.png")
    plt.show()

    # Bar Chart: Average Memory Usage
    plt.figure(figsize=(10, 6))
    plt.bar(summary_df["Model"], summary_df["Average Memory Usage (bytes)"], color='red')
    plt.title("Average Memory Usage by Model")
    plt.ylabel("Memory Usage (bytes)")
    plt.xlabel("Model")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("./paper/attachments/Average_Memory_Usage.png")
    plt.show()


def compute_avg_times_memory(total_dataset, models, categories):
    avg_time_memory_data = {
        "Model": [],
        "Difficulty": [],
        "Average Runtime (ms)": [],
        "Average Memory Usage (bytes)": []
    }

    for model in models:
        for category_name, problems in categories.items():
            # Filter the relevant problems for the current model and difficulty level
            model_category_filter = [
                i for i, problem in enumerate(total_dataset["Problem"])
                if f"({model['name']})" in problem and category_name[:-9].capitalize() in problem
            ]

            if model_category_filter:
                avg_runtime = sum([total_dataset["Average Run Time (ms)"][i] for i in model_category_filter]) / len(model_category_filter)
                avg_memory = sum([total_dataset["Average Memory Usage (bytes)"][i] for i in model_category_filter]) / len(model_category_filter)

                avg_time_memory_data["Model"].append(model["data_name"])
                avg_time_memory_data["Difficulty"].append(category_name[:-9].capitalize())
                avg_time_memory_data["Average Runtime (ms)"].append(avg_runtime)
                avg_time_memory_data["Average Memory Usage (bytes)"].append(avg_memory)

    avg_time_memory_df = pd.DataFrame(avg_time_memory_data)
    export_data(avg_time_memory_df, "Average_Times_Memory")
    return avg_time_memory_df

def main():
    os.system("clear")
    logging.info("Benchmarking process started.")
    total_dataset = {
        'Problem': [],
        'Status': [],
        'Success rate': [],
        'Average Run Time (ms)': [],
        'Average Memory Usage (bytes)': []
    }
    test_cases = load_test_cases('main/data/test_cases.json')
    prompts = load_test_cases('main/data/prompts.json')
    logging.info("Loaded test cases.")
    total_success_count = 0

    models = [
        {"name": "gpt-3.5-turbo", "provider": "openai", "data_name": "gpt-3.5"},
        {"name": "gpt-4o-mini", "provider": "openai", "data_name": "gpt-4o-mini"},

        {"name": "claude-3-sonnet-20240229", "provider": "anthropic", "data_name": "claude-3"},
        {"name": "claude-3-5-haiku-20241022", "provider": "anthropic", "data_name": "claude-3-5"},

        {"name": "gemini-1.5-flash", "provider": "gemini", "data_name": "gemini-1.5"},
        
        {"name": "mistral-large-latest", "provider": "mistral", "data_name": "mistral-large"}
    ]

    for diff in categories:
        logging.info(f"Processing category: {diff.replace('_',' ').capitalize()}")
        for l in range(len(categories[diff])):
            logging.info(f"Processing problem: {categories[diff][l][1]}")
            success_count = 0
            
            dataset = {
                'Test Case': [],
                'Status': [],
                'Run Time (ms)': [],
                'Memory Usage (bytes)': [],
                'Error Message': []
            }
            status, success_count = solution_check(categories[diff][l], test_cases)
            create_summary(status, dataset, total_success_count)

            print("\n")

            case_data = pd.DataFrame(dataset)
            case_data.set_index('Test Case', inplace=True)

            average_runtime = average_measure(case_data)[0]
            average_memory = average_measure(case_data)[1]

            total_dataset["Problem"].append(f"{categories[diff][l][0]} (Leetcode)")
            if success_count == len(test_cases[categories[diff][l][0]]):
                total_dataset["Status"].append("Success 🟢")
            else:
                total_dataset["Status"].append("Fail 🔴")
            total_dataset["Success rate"].append(f"{success_count}/{len(test_cases[categories[diff][l][0]])}")
            total_dataset["Average Run Time (ms)"].append(average_runtime)
            total_dataset["Average Memory Usage (bytes)"].append(average_memory)

            # print(case_data)
            # print("\n")
            # print(f"Successful Test Cases: {success_count}/{len(test_cases[categories[diff][l][0]])}")
            export_data(case_data, f"{categories[diff][l][0]}_human")
            # print(f"Average Run Time: {average_measure(case_data)[0]} milliseconds")
            # print(f"Average Memory Usage: {average_measure(case_data)[1]} megabytes")
            # print("\n")

            # Test AI-generated solution
            logging.info(f"Processing AI-generated solution for problem: {categories[diff][l][1]}")

            for model in models:
                ai_dataset = {
                    'Test Case': [],
                    'Status': [],
                    'Run Time (ms)': [],
                    'Memory Usage (bytes)': [],
                    'Error Message': []
                }
                success_count = 0 
                ai_status, success_count = solution_check(categories[diff][l], test_cases, prompts=prompts, use_ai=True, model=model["name"], provider=model["provider"])
                create_summary(ai_status, ai_dataset, total_success_count)
                
                ai_case_data = pd.DataFrame(ai_dataset)
                ai_case_data.set_index('Test Case', inplace=True)
                m_name = model["name"]
                ai_average_runtime, ai_average_memory = average_measure(ai_case_data)

                total_dataset["Problem"].append(f"{categories[diff][l][0]} ({m_name})")
                if success_count == len(test_cases[categories[diff][l][0]]):
                    total_dataset["Status"].append("Success 🟢")
                else:
                    total_dataset["Status"].append("Fail 🔴")
                total_dataset["Success rate"].append(f"{success_count}/{len(test_cases[categories[diff][l][0]])}")
                total_dataset["Average Run Time (ms)"].append(ai_average_runtime)
                total_dataset["Average Memory Usage (bytes)"].append(ai_average_memory)

                
                export_data(ai_case_data, f"{categories[diff][l][0]}_{m_name.replace('.','_')}")
            # print(ai_case_data)
            # print("\n")
            # print(f"Successful Test Cases: {success_count}/{len(test_cases[categories[diff][l][0]])}")
 
   
    total_data = pd.DataFrame(total_dataset)
    export_data(total_data, 'TotalData')
    logging.info("Benchmarking process completed. Summary exported.")
    # print(total_data)
    # print("\n") 
    
    summary_data = {
        "Model": [],
        "Success Rate": [],
        "Average Runtime (ms)": [],
        "Average Memory Usage (bytes)": []
    }

    # LeetCode stats
    leetcode_filter = [i for i, problem in enumerate(total_dataset["Problem"]) if "(Leetcode)" in problem]
    leetcode_success = sum([int(total_dataset["Success rate"][i].split("/")[0]) for i in leetcode_filter])
    leetcode_total = sum([int(total_dataset["Success rate"][i].split("/")[1]) for i in leetcode_filter])
    leetcode_avg_runtime = sum([total_dataset["Average Run Time (ms)"][i] for i in leetcode_filter]) / len(leetcode_filter)
    leetcode_avg_memory = sum([total_dataset["Average Memory Usage (bytes)"][i] for i in leetcode_filter]) / len(leetcode_filter)

    summary_data["Model"].append("Leetcode")
    summary_data["Success Rate"].append(f"{(leetcode_success / leetcode_total) * 100:.2f}%")
    summary_data["Average Runtime (ms)"].append(leetcode_avg_runtime)
    summary_data["Average Memory Usage (bytes)"].append(leetcode_avg_memory)

    # AI model stats
    for model in models:
        model_filter = [i for i, problem in enumerate(total_dataset["Problem"]) if f"({model['name']})" in problem]
        model_success = sum([int(total_dataset["Success rate"][i].split("/")[0]) for i in model_filter])
        model_total = sum([int(total_dataset["Success rate"][i].split("/")[1]) for i in model_filter])
        model_avg_runtime = sum([total_dataset["Average Run Time (ms)"][i] for i in model_filter]) / len(model_filter)
        model_avg_memory = sum([total_dataset["Average Memory Usage (bytes)"][i] for i in model_filter]) / len(model_filter)

        summary_data["Model"].append(model["data_name"])
        summary_data["Success Rate"].append(f"{(model_success / model_total) * 100:.2f}%")
        summary_data["Average Runtime (ms)"].append(model_avg_runtime)
        summary_data["Average Memory Usage (bytes)"].append(model_avg_memory)

    summary_df = pd.DataFrame(summary_data)
    export_data(summary_df, "Summary")

    logging.info("Benchmarking process completed. Summary exported.")
    # print(summary_df)
    # Testing OpenAI API
    
    visualize_results(summary_df)

    avg_time_memory_df = compute_avg_times_memory(total_dataset, models, categories)
    print(avg_time_memory_df)
if __name__ == "__main__":
    main()
