# Program to remove duplicate elements from a list

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List without duplicates: ", unique_numbers)

# Output
# List wihtout duplicates: [1, 2, 3, 4, 5] 
