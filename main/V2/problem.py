import sys
import json
def twoSum(nums, target):
        # Create a dictionary to store numbers and their corresponding indices
        number_map = {}

        # Loop through the array
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - num

            # Check if the difference already exists in the dictionary
            if diff in number_map:
                # If it exists, return the indices of the current number and the number that adds up to the target
                return [i, number_map[diff]]

            # If it doesn't exist, add the current number and its index to the dictionary
            number_map[num] = i
        
        # If no two numbers add up to the target, return None
        return None

def main():
    input_data = sys.stdin.read()

    try:
        # Deserialize the JSON string into a Python dictionary
        test_case = json.loads(input_data)

        # Extract relevant data from the test_case dictionary
        numbers = test_case["num"]
        target = test_case["target"]

        # Implement your solution logic here
        # Example: Let's assume we just return an empty list as a placeholder
        # Replace this with your actual solution implementation
        print(twoSum(numbers,target))

    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()