# Brutte Force
n = int(input(''))

arr = list(map(int, input('').split()))[:n]

reverse_arr = []

for i in range(n):
    reverse_arr.append(arr[n-i-1])

print(reverse_arr)

# Space-optimized iterative method

p = 0
q = n-1

while(p < q):
    arr[p], arr[q] = arr[q], arr[p]
    p = p+1
    q = q-1
    
print(arr)