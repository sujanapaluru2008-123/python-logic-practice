# Program to count number of words in a sentence

sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Count words
count = len(words)

print("Total words:", count)

# Output
# Enter a sentence: Python is easy to learn comparing to javva
# Total words: 8
