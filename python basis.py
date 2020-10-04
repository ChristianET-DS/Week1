import random
num_coconuts = 0
print('I have ' + str(num_coconuts) + ' coconuts')

num_coconuts = 'banana'
print('My coconuts turned into ' + num_coconuts)

num_bananas = 3
print('What is happening to my coconuts? ' + num_coconuts*num_bananas)

#delete variables
#del num_coconuts
#print('My coconuts don\'t exist anymore ' + str(num_coconuts))


"""
IF
ELIF
ELSE 
"""

number = random.randint(1, 11)
guess = int(input('Guess a number between 1 and 10: '))

if guess == number:
    print(f"You're right! it was {number}")
elif guess - 2 <= number <= guess + 2:
    print(f"Close! It's {number}")
else:
    print(f"Nope, it's {number}")