# Input: N = 3
# Output: Prime
# Explanation: 3 is a prime number

# Input: N = 26
# Output: Non-Prime
# Explanation: 26 is not prime

n = int(input("Enter number: "))

check = 0

for i in range(2,n):
    if n % i == 0:
        check += 1

if check == 0:
    print("prime")
else:
    print("not prime")
