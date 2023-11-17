# Input: min = 10 , max = 50
# Output: 11 22 33 44 
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.

# Input: min = 100 , max = 150
# Output: 101 111 121 131 141 
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.

min = int(input("Eneter the min value: "))
max = int(input("Eneter the max value: "))

for i in range(min,max):
    dummy = i
    reverse_of_dummy = 0

    while dummy > 0:
        digit = dummy % 10

        reverse_of_dummy = reverse_of_dummy * 10 + digit

        dummy = dummy // 10
    
    if i == reverse_of_dummy:
        print(i,end=" ")