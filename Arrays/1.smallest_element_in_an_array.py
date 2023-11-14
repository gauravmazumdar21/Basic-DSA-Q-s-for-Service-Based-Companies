# 1. method of taking an list input in single line

# arr = input("Enter the val of array separated by spaces-> ").split()

# arr_length = len(arr)

# for i in range(arr_length):
#     arr[i] = int(arr[i])

# print(arr)



# 2. method of taking an list input in single line

# size_of_arr = int(input("Enter the size of an array -> "))

# arr = list(map(int, input("Enter the val of array separated by spaces-> ").split()))[:size_of_arr]

# print(arr)


size_of_arr = int(input("Enter the size of an array -> "))

arr = list(map(int, input("Enter the val of array separated by spaces-> ").split()))[:size_of_arr]

min_val = arr[0]

for i in range(size_of_arr):
    if min_val > arr[i]:
        min_val = arr[i]

print(f'The smallest value in an array is -> {min_val}')


