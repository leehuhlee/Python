import sys

sys.argv.pop(0)

numbers = list(map(int, sys.argv))
for number in numbers:
    divisible_3 = number % 3 == 0
    divisible_5 = number % 5 == 0

    if divisible_3 and divisible_5:
        print("fizzbuzz")
    elif divisible_3:
        print("fizz")
    elif divisible_5:
        print("buzz")
    else:
        print(number)






