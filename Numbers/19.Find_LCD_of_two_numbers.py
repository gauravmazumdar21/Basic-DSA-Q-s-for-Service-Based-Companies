# Input: num1 = 4,num2 = 8
# Output: 8

# Input: num1 = 3,num2 = 6
# Output: 6

# lcm(a,b) = a*b/gcm(a,b)

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
gcm = 0

for i in range(1,min(num1,num2)+1):
    if(num1%i==0 and num2%i==0):
        gcm = i

print((num1*num2)/gcm)

