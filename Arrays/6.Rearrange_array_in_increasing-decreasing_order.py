n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

arr.sort()

inc_dec_arr = []

for i in range(n):
    if(i < n/2):
        inc_dec_arr.append(arr[i])
    else:
        continue


# first -1 is to the range till 0
# Second -1 is the steps 

for i in range(n-1,-1,-1):
    if(i >= n/2):
        inc_dec_arr.append(arr[i])
    else:
        continue

print(inc_dec_arr)