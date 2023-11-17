# Input: a=1 , r=0.5 , n=3
# Output: 1.75
# Explanation: The sum of given GP Series is 1.75

# Input: a=3 , r=5 , n=2
# Output: 18
# Explanation: The sum of the given GP Series is 18

# a, first term
# r, common ratio
# n, number of terms


a = int(input("Enter first term of G.P. : "))
r = int(input("Enter common ratio of G.P. : "))
n = int(input("Enter Number of Terms of G.P.: "))


sol = (a * ( r**n - 1)) / (r-1)

print(sol)