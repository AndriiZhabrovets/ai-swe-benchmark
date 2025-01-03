import time
import sys
import os
import pandas as pd
from importlib import import_module

# Connecting the paths of all problems
sys.path.insert(0, './main/problems/easy')
sys.path.insert(0, './main/problems/medium')
sys.path.insert(0, './main/problems/hard')


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


test_cases = [
    [[2, 7, 11, 15], 9, [[0, 1], [1, 0]]],
    [[3, 2, 4],6,[[1, 2], [2, 1]]]
]


def summary_print(st, i, dataset):
    if st["status"]:
        solved = "Success 🟢"
    else:
        solved = "Fail 🔴"

    msg = st["error_msg"]
    tm = st["runtime"]
    
    dataset["Test Case"].append(i)
    dataset["Status"].append(solved)
    dataset["Run Time (ms)"].append(tm) 


    print(f"Solution Status: {solved}")
    print(f"Run Time: {round(tm, 3)} milliseconds")
    if not st["status"]:
        print(f"Error Message: {msg}")
        dataset["Error Message"].append(msg)
    else:
        dataset["Error Message"].append(None)

def call_problem(problem_name, *args):
    module = import_module(problem_name[0])
    problem = getattr(module, problem_name[1])
    return problem(*args)

def solution_check(number, problem_name):
    sol = []
    result = {
        "status" : True,
        "error_msg" : "",
        "runtime": ""
    }
    start_time = time.time()
    try:
        sol = call_problem(problem_name,test_cases[number][0:len(test_cases[0])-1])
    except:
        exc_type, exc_value = sys.exc_info()[0:2]
        result["status"] = False;
        result["error_msg"] = f"Exception Type: {exc_type.__name__}, Message: {exc_value}"
    
    run_time = (time.time() - start_time)*1000
    result["runtime"] = run_time

    if sol in test_cases[number][-1]:
        result["status"] = True
        result["error_msg"] = None
    elif result["status"] == False:
        pass
    elif sol not in test_cases[number][-1]:
        result["error_msg"] = "Incorrect output"
        result["status"] = False

    return result

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
    'Error Message':[]
    }
    
    for i in range(len(test_cases)):
        print(f"Test Case {i+1}:\n")
        status = solution_check(i, easy_problems[0])
        summary_print(status, i, dataset)
        print("\n")
    
    solution_data = pd.DataFrame(dataset)
    print(solution_data)
    export_data(solution_data, 'TestData')
    print(f"Average Run Time: {round(average_runtime(solution_data),3)} milliseconds")


    
if __name__ == "__main__":
    main()