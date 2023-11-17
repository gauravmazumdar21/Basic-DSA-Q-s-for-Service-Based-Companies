# Input:
# n=4
# a=2
# d=2
# Output: 20
# Explanation: 2+4+6+8 = 20

# Input:
# n=8
# a=-2
# d=5
# Output: 124
# Explanation: -2 +3 + 8 + 13 + 18 + 23 + 28 + 33 = 124

# What is A.P. (Arithmetic Progression)?

# A.P. is the series of terms having the first term as a and d, common difference. Every next term in the A.P. is greater than the previous term by d units.
# a = first term of A.P.
# d= common Difference of A.P.
# n= Number of Terms in  A.P.

n = int(input("Enter Number of Terms of A.P.: "))
a = int(input("Enter first term of A.P. : "))
d = int(input("Enter common Difference of A.P. : "))

sum_of_num = a

for i in range(n-1):
    a += d
    sum_of_num += a

print(sum_of_num)



