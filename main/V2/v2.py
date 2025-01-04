import time
import sys
import os
import pandas as pd
import json
import subprocess
import tempfile

# Connecting the paths of all problems
sys.path.insert(0, './main/problems/easy')
sys.path.insert(0, './main/problems/medium')
sys.path.insert(0, './main/problems/hard')

class TestCase:
    def __init__(self, status, error_msg, runtime):
        self.status = status
        self.error_msg = error_msg
        self.runtime = runtime

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

def summary_print(st, dataset):
    for i, tcase in enumerate(st):
        solved = "Success 🟢" if tcase.status else "Fail 🔴"
        msg = tcase.error_msg
        tm = tcase.runtime

        dataset["Test Case"].append(i)
        dataset["Status"].append(solved)
        dataset["Run Time (ms)"].append(tm)

        print(f"\nTest Case {i}:")
        print(f"Solution Status: {solved}")
        print(f"Run Time: {round(tm, 3)} milliseconds")
        if not tcase.status:
            print(f"Error Message: {msg}")
            dataset["Error Message"].append(msg)
        else:
            dataset["Error Message"].append(None)

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
        try:
            result = subprocess.check_output([sys.executable, temp_file.name], stderr=subprocess.PIPE, text=True).strip()
            runtime = (time.time() - start_time) * 1000
            return json.loads(result), runtime, None
        except subprocess.CalledProcessError as e:
            runtime = (time.time() - start_time) * 1000
            return None, runtime, e.stderr
        finally:
            os.unlink(temp_file.name)

def solution_check(problem_name, cases_data):
    results = []
    test_cases = cases_data[problem_name[0]]
    for tcase in test_cases:
        sol, runtime, error = call_problem_subprocess(problem_name, tcase["input"])
        print(sol)
        print(type(sol))
        print(tcase["expected_output"])
        print(type(tcase["expected_output"]))
        if error:
            results.append(TestCase(False, error, runtime))
        elif sol in tcase["expected_output"]:
            results.append(TestCase(True, None, runtime))
        else:
            results.append(TestCase(False, f"Incorrect output: {sol}", runtime))
    return results

def average_runtime(data):
    return data["Run Time (ms)"].mean()

def export_data(data, name):
    file_name = f'main/data/{name}.xlsx'
    data.to_excel(file_name)
    print('DataFrame is written to Excel File successfully.')

def main():
    os.system("clear")
    dataset = {
        'Test Case': [],
        'Status': [],
        'Run Time (ms)': [],
        'Error Message': []
    }
    test_cases = load_test_cases('main/data/test_cases.json')
    status = solution_check(easy_problems[0], test_cases)
    summary_print(status, dataset)
    print("\n")

    solution_data = pd.DataFrame(dataset)
    print(solution_data)
    print("\n")
    export_data(solution_data, 'TestData')
    print(f"Average Run Time: {round(average_runtime(solution_data), 3)} milliseconds")

if __name__ == "__main__":
    main()
