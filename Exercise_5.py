# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

user_input = input("Enter the sentence in hyphen separated format: ")

user_words = user_input.split("-")
print('-'.join(sorted(user_words)))