# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”

n = input("Enter Binary number: ")
reverseN = n[::-1]

decimalNum = 0

for i in range(len(reverseN)):
    if reverseN[i] == '1':
        decimalNum += 2 ** i

print(decimalNum)
