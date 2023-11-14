#  Brute Force Approch

n = int(input("Enter the size of an array -> "))

arr = list(map(int, input("Enter the val of array separated by spaces-> ").split()))[:n]

arr.sort()

print(f'{arr[1]} {arr[n-2]}')
