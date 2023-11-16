# Input:
#  Nums = [1,2,3,4,5,0]
# Output:
#  120
# Explanation:
#  In the given array, we can see 1×2×3×4×5 gives maximum product value.


# Input:
#  Nums = [1,2,-3,0,-4,-5]
# Output:
#  20
# Explanation:
#  In the given array, we can see (-4)×(-5) gives maximum product value.

arr = list(map(int, input("Enter the array: ").split()))

products_arr = []


# Whenever find all the subarrays use 3 loops

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        product = 1
        for k in range(i,j+1):
            product *= arr[k]
        products_arr.append(product)     

print(max(products_arr))