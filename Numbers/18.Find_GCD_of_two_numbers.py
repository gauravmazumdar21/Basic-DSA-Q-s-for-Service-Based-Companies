# Input: num1 = 4, num2 = 8
# Output: 4
# Explanation: Since 4 is the greatest number which divides both num1 and num2.

# Input: num1 = 3, num2 = 6
# Output: 3
# Explanation: Since 3 is the greatest number which divides both num1 and num2.

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
ans = 0

for i in range(1,min(num1,num2)+1):
    if(num1%i==0 and num2%i==0):
        ans = i

print(ans)