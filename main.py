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
   
