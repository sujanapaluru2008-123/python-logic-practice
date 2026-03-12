# Program to check whether a number is prime
num = int(input("Enter a number: "))

is_prime = True

# Check divisibility
for i in range(2, num):
  if num % i == 0:
    is_prime = False
    break

if num > 1 and is-prime:
  print("Prime number")
else:
  print("Not a prime number")

# Example output
# Enter a number: 23
# Prime number
