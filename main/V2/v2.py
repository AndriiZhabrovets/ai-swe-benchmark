import time
import sys
import os
import pandas as pd
import json
import subprocess
import tempfile
import tracemalloc
import logging
# Connecting the paths of all problems
sys.path.insert(0, './main/problems/easy')
sys.path.insert(0, './main/problems/medium')
sys.path.insert(0, './main/problems/hard')

logging.basicConfig(
    filename='./main/logs/benchmark.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
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

def create_summary(st, dataset):
    for i, tcase in enumerate(st):
        if tcase.status:
            solved = "Success 🟢"
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

def call_problem_subprocess(problem_name, args):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write('import sys\n')
        temp_file.write('sys.path.insert(0, \'./main/problems/easy\')\n')
        temp_file.write('sys.path.insert(0, \'./main/problems/medium\')\n')
        temp_file.write('sys.path.insert(0, \'./main/problems/hard\')\n')
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


def solution_check(problem_name, cases_data):
    results = []
    test_cases = cases_data[problem_name[0]]
    logging.info(f"Checking solution for problem: {problem_name[0]} with {len(test_cases)} test cases.")
    for tcase in test_cases:
        sol, runtime, memory, error = call_problem_subprocess(problem_name, tcase["input"])
        if error:
            results.append(TestCase(False, error, runtime, memory))
            logging.warning(f"Test case failed with error: {error.strip()}")
        elif sol in tcase["expected_output"]:
            results.append(TestCase(True, None, runtime, memory))
            logging.info(f"Test case passed. Output: {sol}")
        else:
            results.append(TestCase(False, f"Incorrect output: {sol}", runtime, memory))
            logging.warning(f"Test case failed. Expected: {tcase['expected_output']}, Got: {sol}")
    return results

def average_measure(data):
    return [round(data["Run Time (ms)"].mean(),3), round(data["Memory Usage (bytes)"].mean(),3)]

def export_data(data, name):
    file_name = f'main/data/{name}.xlsx'
    data.to_excel(file_name)
    # print('DataFrame is written to Excel File successfully.')

def main():
    os.system("clear")
    logging.info("Benchmarking process started.")
    total_dataset = {
        'Problem': [],
        'Average Run Time (ms)': [],
        'Average Memory Usage (bytes)': []
    }
    test_cases = load_test_cases('main/data/test_cases.json')
    logging.info("Loaded test cases.")
    for diff in categories:
        logging.info(f"Processing category: {diff.replace('_',' ').capitalize()}")
        for l in range(len(categories[diff])):
            logging.info(f"Processing problem: {categories[diff][l][1]}")
            # print(f"Problem: {categories[diff][l][1]}")
            dataset = {
                'Test Case': [],
                'Status': [],
                'Run Time (ms)': [],
                'Memory Usage (bytes)': [],
                'Error Message': []
            }
            status = solution_check(categories[diff][l], test_cases)
            create_summary(status, dataset)
            # print("\n")
            
            case_data = pd.DataFrame(dataset)
            case_data.set_index('Test Case', inplace=True)

            average_runtime = average_measure(case_data)[0]
            average_memory = average_measure(case_data)[1]

            total_dataset["Problem"].append(categories[diff][l][0])
            total_dataset["Average Run Time (ms)"].append(average_runtime)
            total_dataset["Average Memory Usage (bytes)"].append(average_memory)

            # print(case_data)
            # print("\n")
            export_data(case_data, categories[diff][l][0])
            # print(f"Average Run Time: {average_measure(case_data)[0]} milliseconds")
            # print(f"Average Memory Usage: {average_measure(case_data)[1]} megabytes")
            # print("\n")



    total_data = pd.DataFrame(total_dataset)
    export_data(total_data, 'TotalData')
    logging.info("Benchmarking process completed. Summary exported.")
    print(total_data)
if __name__ == "__main__":
    main()
