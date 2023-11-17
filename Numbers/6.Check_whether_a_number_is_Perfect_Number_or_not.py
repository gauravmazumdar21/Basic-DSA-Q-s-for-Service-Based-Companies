# Input: n=6
# Output: 6 is a perfect number

# Input: n=15
# Output: 15 is not a perfect number

# Input: n=28
# Output: 28 is a perfect number
# Reason:
# For 6 and 28 , the sum of their proper divisors (1+2+3) and (1+4+7+14) is equal to the respective numbers and for 15 it is not.

num = int(input("Enter Number: "))

sum_of_divisors = 0

for i in range(1,num):
    if num % i == 0:
        sum_of_divisors += i

if num == sum_of_divisors:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not a perfect number")
