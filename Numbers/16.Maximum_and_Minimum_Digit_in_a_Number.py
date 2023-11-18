# Input: N = 2746
# Output: Largest digit: 7
#         Smallest digit: 2
# Explanation: By simply going through the digits of 
# the number, we figure out the largest and smallest 
# digit in the number.

# Input: N = 23004
# Output: Largest digit : 4
#         Smallest digit : 0
# Explanation: By simply going through the digits of 
# the number, we figure out the largest and smallest 
# digit in the number.

num = int(input("Enter number: "))
numStr = str(num)
numLen = len(numStr)

max = int(numStr[0])
min = int(numStr[0])

for i in numStr:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)

print(f"Largest digit : {max}")
print(f"Smallest digit : {min}")