n = int(input("Enter the array length: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

count = {}

for i in range(n):
    if arr[i] in count:
        count[arr[i]] += 1
    else:
        count[arr[i]] = 1

for j in count:
    print(j, count[j])

