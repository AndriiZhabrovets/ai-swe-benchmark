import time
import sys
import os
import pandas as pd
import subprocess
import json

test_cases = [
    {"num": [2, 7, 11, 15], "target": 9, "correct_sol": [[0, 1], [1, 0]]},
    {"num": [3, 2, 4], "target": 6, "correct_sol": [[1, 2], [2, 1]]}
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

def solution_check(number):
    result = {
        "status": True,
        "error_msg": "",
        "runtime": 0
    }

    test_case = test_cases[number]

    try:
        start_time = time.time()
        
        # Execute the user's script with subprocess
        process = subprocess.run(
            ["python3", "V2/problem.py"],
            input=json.dumps(test_case),
            text=True,
            capture_output=True,
            timeout=5  # Timeout for long-running scripts
        )

        runtime = (time.time() - start_time) * 1000
        result["runtime"] = runtime

        if process.returncode != 0:
            result["status"] = False
            result["error_msg"] = process.stderr
        else:
            try:
                solution_output = json.loads(process.stdout)
                if solution_output in test_case["correct_sol"]:
                    result["status"] = True
                else:
                    result["status"] = False
                    result["error_msg"] = "Incorrect output"
            except json.JSONDecodeError:
                result["status"] = False
                result["error_msg"] = "Output is not valid JSON"
    
    except subprocess.TimeoutExpired:
        result["status"] = False
        result["error_msg"] = "Solution timed out"
    except Exception as e:
        result["status"] = False
        result["error_msg"] = f"Exception: {e}"

    return result

def export_data(data):
    df = pd.DataFrame(data)
    file_name = 'data/TestData.xlsx'
    df.to_excel(file_name)
    print('DataFrame is written to Excel File successfully.')

def main():
    dataset = {
        'Test Case': [],
        'Status': [],
        'Run Time (ms)': [],
        'Error Message': []
    }

    os.system("clear")
    for i in range(len(test_cases)):
        print(f"Test Case {i+1}:")
        status = solution_check(i)
        summary_print(status, i, dataset)
        print("\n")

    export_data(dataset)

if __name__ == "__main__":
    main()
