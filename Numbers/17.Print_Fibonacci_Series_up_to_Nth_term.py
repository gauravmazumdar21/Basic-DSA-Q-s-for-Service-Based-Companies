# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

# Input: 6
# Output: 0 1 1 2 3 5 8
# Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)

n = int(input("Enter number: "))

first_value = 0
second_value = 1

print(first_value, end=" ")
print(second_value, end=" ")

for i in range(n-1):
    nextNum = first_value + second_value
    print(nextNum, end=" ")
    first_value = second_value
    second_value = nextNum