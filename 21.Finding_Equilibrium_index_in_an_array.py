# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

# Input: nums = [1,-1,4]
# Output: 2
# Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
# The sum of the numbers after index 2 is: 0

arr = list(map(int, input("Enter the array: ").split()))


for i in range(len(arr)):

    left_sum = 0
    for j in range(i):
        left_sum += arr[j]

    right_sum = 0
    for j in range(i+1,len(arr)):
        right_sum += arr[j]

    if(left_sum == right_sum):
        print(i)
    
# Consider two variables leftSum and rightSum initialized to zero.Now for every index, i calculate the leftSum till that index and rightSum till that index.

# At any point if (leftSum == rightSum) return that index i.