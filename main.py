# # Task 1: Happy Numbers
# # A happy number is a number defined by the following process: starting with any 
# # positive integer, replace the number by the sum of the squares of its digits, and 
# # repeat the process until the number equals 1. An example of a happy number is 19
# # (For more info: https://en.wikipedia.org/wiki/Happy_number)
# # Write a method that determines if a number is happy or sad

def happy_numbers():

    hold_num_index = 0
    hold_nums = []
    happy = 'False'
    index = 0
    sum = 0


    input_number = input(" Enter a number to see if it's happy: ")

    # Add the number to the list hold_nums
    hold_nums.append(int(input_number))


    while happy == "False":
        number = str(hold_nums[hold_num_index])

        for char in number:
            sum += int(char) * int(char)


        if sum == 1:
            print(f" {input_number} is a happy 😊 number!")
            happy = 'True'


        else:
            if sum in hold_nums:
                print(f" {input_number} is a sad 😥 number!")
                break
            hold_nums.append(int(sum))
            hold_num_index += 1
            sum = 0
    
happy_numbers()

# Task 2: Prime Numbers
# A prime number is a number that is only divisible by one and itself.
# Write a method that prints out all prime numbers between 1 and 100 

def is_prime():
    sum_of_divides = 0
    prime = 'True'

    for num in range(2,101):
        for divisor in range(2, num-1):
            is_divisible = num % divisor
    
            if is_divisible == 0:
                prime = "False"

        if prime == "True":
            print(num)
        prime = "True"


is_prime()
   
# Task 3: Fibonacci
# A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# Write a method that does the Fibonacci sequence starting at 1

def fibonacci_from_1():
    fib_num = [1,1]

    for index in range(0,50):
        if index == 0 or index == 1:
            print(fib_num[index])
        else:
            num = fib_num[index -1] + fib_num[index-2]
            fib_num.append(num)
            print(fib_num[index])

fibonacci_from_1()

# Fibonacci Sequence from user input

def fibonacci_from_user():        
    fib_num_alt = []

    number = input(" Enter a number to start the Fibonacci Sequence: ")
    user_number = int(number)
    for index in range(0,50):
        if index == 0 or index == 1:
            fib_num_alt.append(user_number)
            print(fib_num_alt[index])
        else:
            num = fib_num_alt[index -1] + fib_num_alt[index-2]
            fib_num_alt.append(num)
            print(fib_num_alt[index])

fibonacci_from_user()