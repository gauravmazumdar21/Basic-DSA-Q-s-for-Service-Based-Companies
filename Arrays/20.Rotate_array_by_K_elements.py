# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.

n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

k = int(input("Enter the Kth element: "))

direction = input("Enter direction: ")

# Block Swap Algo.

first_half = []
second_half =[]

if direction == "left":
    for i in range(n):
        if(i < k):
            second_half.append(arr[i])
        else:
            first_half.append(arr[i])
elif direction == "right":
    for i in range(n):
        if(i < n-k):
            second_half.append(arr[i])
        else:
            first_half.append(arr[i])
else:
    print("Enter corret direction, either left or right only")


final_arr = first_half + second_half

print(final_arr)