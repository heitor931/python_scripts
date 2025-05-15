#Challenge #3

# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.

list_of_requested_nums = []
# calculate the numbers
for num in range(1500, 3201):
    if num % 7 == 0:
        if num % 5 == 0:
            continue
        else:
            list_of_requested_nums.append(str(num))

# Print the numbers in csv format
print(','.join(list_of_requested_nums))


