n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

st = set()
    
for i in range(n):
    st.add(arr[i])

new_arr = []

for j in st:
    new_arr.append(j)

new_arr.sort()
print(new_arr)