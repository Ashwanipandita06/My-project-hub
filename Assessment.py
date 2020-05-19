# Factorial with loop
take_number = int(input("Enter the number"))


def factorial_with_loop(number):
    f = 1
    for i in range(1, number + 1):
        f = f * i
    return f


print(factorial_with_loop(take_number))

# 2) Factorial without loop

take_number1 = int(input("Enter the number"))


def factorial_without_loop (number):
    if number == 0:
        return 1

    return number * factorial_without_loop(number - 1)


print(factorial_without_loop(take_number1))


# 3) to find the second highest

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 5, 3, 2, 1]
print("The second highest number in the list is " + str(max(list1)-1))

# 4 Fibonacci













