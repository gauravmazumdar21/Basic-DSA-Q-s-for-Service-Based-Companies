n = int(input("Enter the size of an array -> "))

arr = list(map(int, input("Enter the value separated by spaces -> ").split()))[:n]

max_val = arr[0]

for i in range(n):
    if max_val < arr[i]:
        max_val = arr[i]

print(f"The largest value is {max_val}")