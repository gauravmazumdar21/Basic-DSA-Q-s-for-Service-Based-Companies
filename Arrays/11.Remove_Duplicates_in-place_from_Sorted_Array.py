# Size of an arr -> 10
# Array-> 1 2 2 3 3 3 4 4 5 5 
# Sample output 1:
# 5
# Explanation of sample input 1:
# The new array will be [1 2 3 4 5].
# So our answer is 5.


n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

st = set()
    
for i in range(n):
    st.add(arr[i])

k = len(st)

print(k)
# A Set in Python programming is an unordered collection data type that is iterable, mutable and 
# has no duplicate elements. 


# Optimal Solution
p = 0

for i in range(1,n):
    if arr[p] != arr[i]:
        p += 1
        arr[p] = arr[i]

print(p+1)