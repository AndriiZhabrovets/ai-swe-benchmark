import time
import sys
import os
import pandas as pd
import json
import subprocess
import tempfile
import psutil
# Connecting the paths of all problems
sys.path.insert(0, './main/problems/easy')
sys.path.insert(0, './main/problems/medium')
sys.path.insert(0, './main/problems/hard')

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
        dataset["Memory Usage (mb)"].append(tcase.memory)
        dataset["Run Time (ms)"].append(tm)

        if not tcase.status:
            dataset["Error Message"].append(msg)
        else:
            dataset["Error Message"].append(None)

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
        process = psutil.Process(os.getpid())
        try:
            result = subprocess.check_output([sys.executable, temp_file.name], stderr=subprocess.PIPE, text=True).strip()
            runtime = (time.time() - start_time) * 1000
            memory = process.memory_info().rss / 1000000
            return json.loads(result), runtime, memory, None
        except subprocess.CalledProcessError as e:
            runtime = (time.time() - start_time) * 1000
            memory = process.memory_info().rss / 1000000
            return None, runtime, memory, e.stderr
        finally:
            os.unlink(temp_file.name)

def solution_check(problem_name, cases_data):
    results = []
    test_cases = cases_data[problem_name[0]]
    for tcase in test_cases:
        sol, runtime, memory, error = call_problem_subprocess(problem_name, tcase["input"])
        if error:
            results.append(TestCase(False, error, runtime, memory))
        elif sol in tcase["expected_output"]:
            results.append(TestCase(True, None, runtime, memory))
        else:
            results.append(TestCase(False, f"Incorrect output: {sol}", runtime, memory))
    return results

def average_measure(data):
    return [round(data["Run Time (ms)"].mean(),3), round(data["Memory Usage (mb)"].mean(),3)]

def export_data(data, name):
    file_name = f'main/data/{name}.xlsx'
    data.to_excel(file_name)
    print('DataFrame is written to Excel File successfully.')

def main():
    os.system("clear")
    
    total_dataset = {
        'Problem': [],
        'Average Run Time (ms)': [],
        'Average Memory Usage (mb)': []
    }

    case_dataset = {
        'Test Case': [],
        'Status': [],
        'Run Time (ms)': [],
        'Memory Usage (mb)': [],
        'Error Message': []
    }

    test_cases = load_test_cases('main/data/test_cases.json')
    status = solution_check(hard_problems[3], test_cases)
    create_summary(status, case_dataset)
    print("\n")

    case_data = pd.DataFrame(case_dataset)
    print(case_data)
    print("\n")
    export_data(case_data, 'TestData')
    print(f"Average Run Time: {average_measure(case_data)[0]} milliseconds")
    print(f"Average Memory Usage: {average_measure(case_data)[1]} megabytes")

if __name__ == "__main__":
    main()
