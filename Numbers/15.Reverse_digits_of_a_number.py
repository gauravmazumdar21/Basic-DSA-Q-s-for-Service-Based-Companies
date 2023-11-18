# Input: N = 472
# Output: 274
# Explanation: Reading the number from back to front, we see that the output should be 274

# Input: N = 470
# Output: 74
# Explanation: Reading the number from back to front, we get 074. For an integer with no decimals, we know that leading zeros have no significance and therefore our answer should be 74

num = int(input("Enter number: "))

numStr = str(num)
numLen = len(numStr)

reverseNum = 0

for i in range(numLen):
    lastdigit = num % 10
    reverseNum = reverseNum*10 + lastdigit
    num = num//10

print(reverseNum)