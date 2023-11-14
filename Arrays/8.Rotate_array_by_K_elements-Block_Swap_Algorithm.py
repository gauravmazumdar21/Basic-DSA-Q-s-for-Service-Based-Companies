n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

k = int(input("Enter the Kth element: "))

# Block Swap Algo.

first_half = []
second_half =[]

for i in range(n):
    if(i < k):
        second_half.append(arr[i])
    else:
        first_half.append(arr[i])

final_arr = first_half + second_half

print(final_arr)