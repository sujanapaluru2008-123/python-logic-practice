# program to count vowels in a strimg

str = input("Enter a string: ")
count = 0

for char in str:
   if char.lower() in "aeiou":
       count += 1

print("Number of vowels: ", count)

# Output
# Enter a string: github
# Number of vowels: 2
