import random
'''#1
words = input("Enter your a string in lowercase: ")

while words.isdigit() or words != words.lower():
    words = input("Invalid input, please try again: ")

print(words.upper())
'''
'''#2
number1 = input("Input a number: ")
while not number1.isdigit():
    number1 = input("Invalid input, please try again: ")

number2 = input("Input a 2nd number: ")
while not number2.isdigit():
    number2 = input("Invalid input, please try again: ")

number1 = int(number1)
number2 = int(number2)

print(number1 + number2)'''

'''#3
total = []
totalNum = 0
exit = False
while exit == False:
    numInput = input("Enter a number: ")
    while not numInput.isdigit():
        numInput = input("Invalid input, please try again: ")
    total.append(int(numInput))

    numInput = input("Would you like to add another number? (y/n): ")
    while numInput != 'n' and numInput != 'y':
        numInput = input("Invalid input, please try again: ")
    
    if numInput == 'n':
        exit = True

for num in total:
    totalNum = totalNum + num

print(totalNum)'''
'''
#4       
random.random()
exit = False
while exit == False:
    maxNum = input("Assign a maximum integer: ")
    while not maxNum.isdigit():
        maxNum = input("Invalid input, please try again: ")
    print(random.randint(1, int(maxNum)))
    
    maxNum = input("Would you like to add another number? (y/n): ")
    while maxNum != 'n' and maxNum != 'y':
        maxNum = input("Invalid input, please try again: ")
    
    if maxNum == 'n':
        exit = True
'''
'''
#5
leftCount = 0
rightCount = 0
for x in range(0, 10):
    randNum = random.randint(1, 100)
    if randNum % 2 == 0:
        rightCount = rightCount + 1
    else:
        leftCount = leftCount + 1

print(f"Right: {rightCount}\nLeft: {leftCount}")
'''

