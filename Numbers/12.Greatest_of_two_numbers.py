# Input: 1 3
# Output: 3
# Explanation: Answer is 3,since 3 is greater than 1.

# Input: 1.123  1.124
# Output: 1.124
# Explanation: Answer is 1.124,since 1.124 is greater than 1.123.

arr = list(map(int, input("Enter the val of array separated by spaces-> ").split()))

if arr[0] > arr[1]:
    print(arr[0])
else:
    print(arr[1])
