n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

arr.sort()

if n % 2 == 0:
    ind1 = arr[n // 2]
    ind2 = arr[n // 2 - 1]
    median = (ind1 + ind2) / 2
else:
    median = arr[n // 2]

print(f'Median -> {median}')
