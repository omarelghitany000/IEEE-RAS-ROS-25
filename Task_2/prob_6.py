# Read a word from user input
word = input("Enter a word: ")

# Check if the word is palindrome
if word == word[::-1]:
    print("The word is a Palindrome.")
else:
    print("The word is NOT a Palindrome.")