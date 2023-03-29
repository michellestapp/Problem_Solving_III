# Task 1: Happy Numbers
# A happy number is a number defined by the following process: starting with any 
# positive integer, replace the number by the sum of the squares of its digits, and 
# repeat the process until the number equals 1. An example of a happy number is 19
# (For more info: https://en.wikipedia.org/wiki/Happy_number)
# Write a method that determines if a number is happy or sad

hold_num_index = 0
hold_nums = []
happy = 'False'
index = 0

sum = 0


input_number = input(" Enter a number to see if it's happy: ")

# Add the number to the list hold_nums
hold_nums.append(int(input_number))
# number_index = len(str(hold_nums[hold_num_index])) - 1

while happy == "False":
    number = str(hold_nums[hold_num_index])
        
    print(number)
    for char in number:
        sum += int(char) * int(char)
        if sum in hold_nums:
            print(f" {input_number} is NOT a happy number!")
            break
    hold_nums.append(int(sum))
    if sum == 1:
        print(f" {input_number} is a happy number!")
        break
    else:
       
    hold_num_index += 1
    sum = 0
          

