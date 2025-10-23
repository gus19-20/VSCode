'''
print('hello')

myVariable = 5

def myFunction(x, y):
    return x * y

print(myFunction(myVariable, 52))

mylist = [4, 2, 6, 5,"bob"]

for value in mylist:
    print(value)

mydictionary = {"name": "George", "age": "37", "job": "programmer"}

for value in mydictionary:
    print(f"{value}: {mydictionary[value]}")

print(mylist[0])

somewords = "YEELLLLIIIINNNGGGG"

print(somewords.lower())

for x in range(5):
    print(x)

if myVariable % 2 == 1:
    print("odd")

answer = input("What is your age?: ")

while not answer.isdigit():
    answer = input("Invalid input, please try again: ")

print("yay awesome")
answer = int(answer)
print(f"You will be {answer + 5} in 5 years")
'''
words = input("Enter your a string in lowercase: ")

while words.isdigit() or words != words.lower():
    words = input("Invalid input, please try again: ")

print(words.upper())