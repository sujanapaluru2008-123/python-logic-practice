# Program to find the second largest number in a list
numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]
second = numbers[0]

for num in numbers: 
    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Second largest number: ", second)

# Output:
# Second largest number: 56
