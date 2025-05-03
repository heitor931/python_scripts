# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.

user = int(input("Enter a number: "))

def divisor_numbers(num):
    list_of_divisors = []
    for n in range(num+1):
        if n == 0:
            continue
        else:
            if num % n == 0:
                list_of_divisors.append(n)
    print(list_of_divisors)

divisor_numbers(user)
