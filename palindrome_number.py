# Program to check whether a number is palindrome
# A palindrome number reads the same forward and backward

num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if temp == rev:
  print("Palindrome number")
else:
  print("Not a palindrome number")

# Example output
# Enter a number: 212
# Palindrome number
