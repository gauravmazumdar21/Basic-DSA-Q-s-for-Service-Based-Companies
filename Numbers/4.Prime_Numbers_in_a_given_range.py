# Input: 2 10
# Output: 2 3 5 7 
# Explanation: Prime Numbers b/w 2 and 10 are 2,3,5 and 7.

# Input: 10 16
# Output: 11 13 
# Explanation: Prime Numbers b/w 10 and 16 are 11 and 13.

min_max = list(map(int, input("Enter min and max value: ").split()))

for i in range(min_max[0],min_max[1]):
    check = 0
    for j in range(2,i):
        if i % j == 0:
            check += 1
    if check == 0:
        print(i,end=" ")