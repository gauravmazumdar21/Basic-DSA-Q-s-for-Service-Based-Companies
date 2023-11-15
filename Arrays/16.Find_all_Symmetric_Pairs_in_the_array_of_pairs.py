# Input: (1,2),(2,1),(3,4),(4,5),(5,4)
# Output: (2,1) (5,4)
# Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.

n = 8
arr = [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4],[5,6],[4,3],[2,1]]
symmetric_arr = []


for i in range(n):
    j = i
    for j in range(n):
        if (arr[j][0] == arr[i][1]) and (arr[j][1] == arr[i][0]):
            symmetric_arr.append((arr[i][1],arr[i][0]))
            break

num = len(symmetric_arr)

for k in range(num):
    if(k%2 != 0):
        print(symmetric_arr[k])


# Approach:

# First use a for loop and traverse through every pair in the vector.
# Then use another for loop and check if the symmetric pair of that pair is present in the rest of the vector or not.
# If the symmetric pair is present print the pair and break from the second for loop.so as to avoid repetitive printing of answers in case of duplicate pair.
# If the symmetric pair is not present,move to the next pair.