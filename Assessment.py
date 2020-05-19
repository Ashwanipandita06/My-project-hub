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


def factorial_without_loop(number):
    if number == 0:
        return 1

    return number * factorial_without_loop(number - 1)


print(factorial_without_loop(take_number1))


# 3) to find the second highest

list1 = [1, 2, 3]
list2 = set(list1)

list2.remove(max(list1))

print("Second highest number is : ", str(max(list2)))

# 4 Fibonacci

input_number = int(input("Enter the number"))


def fibonacci(number):
    first_number = 0
    second_number = 1
    print(first_number)
    print(second_number)

    for i in range(2, number):
        num = first_number + second_number
        first_number = second_number
        second_number = num
        print(num)


fibonacci(input_number)

# Fibonacci with recursion

















