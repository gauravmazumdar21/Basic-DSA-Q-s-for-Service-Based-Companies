# Input: array[] = {1,2,3,4,5} k=3  
# Output: 2                      
# Explanation: The answer is 2 because 3 is present at 2nd index.

arr = list(map(int, input("Enter the array: ").split()))

find_Ind_OF = int(input("Enter the element you want the index of: "))

for i in range(len(arr)):
    if find_Ind_OF == arr[i]:
        print(i)