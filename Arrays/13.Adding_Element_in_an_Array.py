# Input: N = 5, array[] = {1,2,3,4,5}
# insertbeginning(6)
# insertending(7)
# insertatpos(8,4)
# Output: 6,1,2,8,3,4,5,7
# Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4

arr = list(map(int, input("Enter the array: ").split()))

begining = int(input("Element insert at beginning: "))
atPos = list(map(int, input("Enter value and position: ").split()))
ending = int(input("Element insert at ending: "))

new_arr = []

new_arr.append(begining)

for i in range(len(arr)):
    if i == (atPos[1]-2):
        new_arr.append(atPos[0])
    new_arr.append(arr[i])

new_arr.append(ending)

print(new_arr)