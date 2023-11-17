# Input: n=5
# Output: odd
# Explanation: 5 is not divisible by 2.
 
# Input: n=6
# Output: even
# Explanation: 6 is divisible by 2.

num = int(input("Enter number: "))

if(num % 2 == 0):
    print("even")
else:
    print("odd")