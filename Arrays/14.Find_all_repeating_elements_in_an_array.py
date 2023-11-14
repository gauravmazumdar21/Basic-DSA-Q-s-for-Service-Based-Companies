# Arr[] = [1,1,2,3,4,4,5,2]
# Output:
#  1,2,4
# Explanation:
#  1,2 and 4 are the elements which are occurring more than once.

arr = list(map(int, input("Enter the array: ").split()))

repeated_arr = []

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            if arr[i] in repeated_arr:
                continue
            else:
                repeated_arr.append(arr[i])
            

print(repeated_arr)