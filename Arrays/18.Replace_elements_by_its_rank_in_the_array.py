# Input: 20 15 26 2 98 6
# Output: 4 3 5 1 6 2
# Explanation: When sorted,the array is 2,6,15,20,26,98. So the rank of 2 is 1,rank of 6 is 2,rank of 15 is 3 and so…

# arr = list(map(int, input("Enter the array: ").split()))
arr = [20, 15, 26, 2, 98, 6]

sorted_array = sorted(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        if(arr[i] == sorted_array[j]):
            print(j+1, end=" ")

