import random 5

print("Welcome to guessing game...")
n=random.randint(1,101)

guess = int(input("Please enter a number between 1-100:"))

while guess != n:
    if guess > n:
        guess = int(input("Decrease your number."))
    else:
        guess = int(input("Increase your number."))
print("Well done, you found the number.")