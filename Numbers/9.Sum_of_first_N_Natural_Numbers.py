# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

num = int(input("Enter number: "))

sum = 0

for i in range(1,num+1):
    sum += i

print(sum)