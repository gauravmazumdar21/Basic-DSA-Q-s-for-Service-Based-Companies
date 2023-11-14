# Input:
#  Nums = [1,2,-1,1,3,1]
# Output:
#  2,-1,3
# Explanation:
#  1 is the only element in the given array which occurs thrice in the array. 
#  -1,2,3 occurs only once and hence, these are non-repeating elements of the given array.

arr = list(map(int, input("Enter the array: ").split()))

repeated_arr = []

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            if arr[i] in repeated_arr:
                continue
            else:
                repeated_arr.append(arr[i])
            
non_repeated_arr = []

for element in arr:
    if element not in repeated_arr:
        non_repeated_arr.append(element)

print(non_repeated_arr)