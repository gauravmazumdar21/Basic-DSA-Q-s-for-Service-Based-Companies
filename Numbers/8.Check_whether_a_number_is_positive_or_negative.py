# Input: n=5
# Output: Positive

# Input: n=-6
# Output: Negative

num = int(input("Enter number: "))

if(num > 0):
    print("Positive")
elif(num == 0):
    print("Zero")
else:
    print("Negative")