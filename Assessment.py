# Factorial with loop
take_number = int(input("Enter the number"))


def factorial_without_loop(number):
    f = 1
    for i in range(1, number + 1):
        f = f * i
    return f


print(factorial_without_loop(take_number))

# Factorial without loop

take_number1 = int(input("Enter the number"))


def factorial_without_loop (number):
    if number == 0:
        return 1

    return number * factorial_without_loop(number - 1)


print(factorial_without_loop(take_number1))
