# Input: 1 3 5
# Output: 5
# Explanation: Answer is 5.Since 5 is greater than 1 and 3.

# Input: 1.123  1.124 1.125
# Output: 1.125
# Explanation: Answer is 1.125. Since 1.125 is greater than 1.123 and 1.124

arr = list(map(int, input("Enter the val of array separated by spaces-> ").split()))

if arr[0] > arr[1] and arr[0] > arr[2]:
    print(arr[0])
elif arr[1] > arr[0] and arr[1] > arr[2]:
    print(arr[1])
else:
    print(arr[2])