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

product = 1
for i in range(len(arr)):
    j = i
    for j in range(len(arr)):
        product *= arr[j]
        products_arr.append(product)     

print(products_arr)