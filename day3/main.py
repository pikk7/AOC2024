import re

# Read the content of the file
file_path = "input.txt"  # Replace with your file path
with open(file_path, "r") as file:
    big_string = file.read()

# # Regular expression to match 'mul(n,m)'
# matches = re.findall(r"mul\((\d+),(\d+)\)", big_string)

# # Calculate the total sum of n * m
# total_sum = sum(int(n) * int(m) for n, m in matches)

# print(f"#1 TaskTotal sum: {total_sum}")


matches = re.findall(r"(do\(\)|don\'t\(\)|mul\(\d+,\d+\))", big_string)

# Variables to control inclusion of `mul`
total_sum = 0
include_mul = True  # By default, include `mul`

# Debugging print to see matches
print("Matches:", matches)

# Process matches
for match in matches:
    if match == "don't()":
        include_mul = False
    elif match == "do()":
        include_mul = True
    elif include_mul:
        data = match.split(",")
        numb1 = int(data[0].replace("mul(", ""))
        numb2 = int(data[1].replace(")", ""))
        total_sum = total_sum + numb1 * numb2


# Output the total sum
print(f"Total sum of valid mul(n, m): {total_sum}")
