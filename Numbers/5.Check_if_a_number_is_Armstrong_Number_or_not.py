# Input:153 
# Output: Yes, it is an Armstrong Number
# Explanation: 1^3 + 5^3 + 3^3 = 153

# Input:170 
# Output: No, it is not an Armstrong Number
# Explanation: 1^3 + 7^3 + 0^3 != 170

# What are Armstrong Numbers?
# Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number.

num = int(input("Enter number: "))

# to find the length of the number, convert num into string then find the length
num_str = str(num)
num_len = len(num_str)

sum_of_powers = 0
temp = num

for i in range(num_len):
    digit = temp % 10

    sum_of_powers += digit ** num_len
    
    temp = temp // 10

if num == sum_of_powers:
    print("Yes, it is an Armstrong Number")
else:
    print("No, it is not an Armstrong Number")