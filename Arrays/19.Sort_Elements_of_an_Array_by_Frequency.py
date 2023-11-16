# Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
# Output: 2 2 2 1 1 3 3 4 
# Explanation: Since  2 is present 3 times in an array , so print it 3 times ,then print ‘1’ 2 times and then ‘3’ 2 times and 4 has least frequency, it will be printed at last.

n = int(input("Enter the size of an array: "))

arr = list(map(int, input("Enter the array: ").split()))[:n]

my_dict = {}

for i in arr:
    # Check if the i is already in the dictionary
    if i in my_dict:
        # If yes, increment the value by 1
        my_dict[i] += 1
    else:
        # If no, add the key to the dictionary with a value of 1
        my_dict[i] = 1

# Sort the dictionary according to the values
sorted_dict = dict(sorted(my_dict.items(),key=lambda item: item[1],reverse=True))

for key, value in sorted_dict.items():
    # Print the key repeated 'value' times
    print((str(key) + ' ') * value, end="")


    