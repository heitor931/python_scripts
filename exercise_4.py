# Write a program that asks the user for a long string containing multiple words separated by whitespaces.
# Make it to print back the same string with the words in backward order.
# For example, say I type the string: My name is Andrei
# Then the script should print out: Andrei is name My

user_input = input("Write your sentence: ")

def invert_sentence(user_input):
    frases = user_input.split(" ")
    arranged_frases = " ".join(frases[::-1])
    return arranged_frases


print(invert_sentence(user_input))
