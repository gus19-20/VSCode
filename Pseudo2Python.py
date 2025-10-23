words = input("Enter your a string in lowercase: ")

while words.isdigit() or words != words.lower():
    words = input("Invalid input, please try again: ")

print(words.upper())