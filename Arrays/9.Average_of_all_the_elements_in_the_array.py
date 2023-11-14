n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

sum = 0

for i in range(n):
    sum += arr[i]

print(f'Average-> {sum/n}')