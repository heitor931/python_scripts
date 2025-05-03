# Consider the following string: nums = '10,20,30,40,50'
# Create a Python script that creates a list of integers from the string.


nums = "10,20,30,40,50"

integers = nums.split(",")
converted_strings = [int(i) for i in integers]
print(converted_strings)