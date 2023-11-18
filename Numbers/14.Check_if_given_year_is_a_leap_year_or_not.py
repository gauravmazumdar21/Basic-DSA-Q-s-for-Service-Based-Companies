# Input: 1996
# Output: Yes
# Explanation: Since 1996 is a leap year answer is “Yes”.

# Input: 2001
# Output: No
# Explanation: Since 2000 is a leap year answer is “Yes”.

year = int(input("Enter Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yes")
else:
    print("No")