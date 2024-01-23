# Answer to Question 1: Sum of Numbers
import os
print("Current Working Directory:", os.getcwd())

def sum_of_numbers(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            try:
                num = int(line.strip())
                total += num
            except ValueError:
                # Handle the case where the line is not a valid integer
                continue
    return total

# Answer to Question 2: Filter Numbers

def filter_numbers(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            try:
                num = int(line.strip())
                if num > 5000:
                    output_file.write(f"{num}\n")
            except ValueError:
                # Handle the case where the line is not a valid integer
                continue

# Example usage (assuming the file paths are correct)
sum_result = sum_of_numbers('random.txt')
print("Sum of numbers:", sum_result)

filter_numbers('random.txt', 'filtered_numbers2.txt')
print("Filtered numbers saved to 'filtered_numbers.txt'")
