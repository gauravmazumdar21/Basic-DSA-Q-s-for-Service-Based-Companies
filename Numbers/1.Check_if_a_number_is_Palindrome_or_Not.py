# Input: N = 123
# Output: Not Palindrome Number
# Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

# Input: N =  121 
# Output: Palindrome Number
# Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.

num = int(input("Enter a number: "))

dummy = num

reverse_num = 0

while dummy > 0:
    # last didgit
    digit = dummy % 10

    # adding to the reverse number
    reverse_num = reverse_num * 10 + digit

    # shrink the last value
    dummy = dummy // 10

if num == reverse_num:
    print(f"Palindrome Number because {num} is same as {reverse_num}")
else:
    print(f"Not Palindrome Number because {num} is different from {reverse_num}")
