import random

jackpot = random.randint(1,110)
guess = int(input("Enter your number: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Enter higher number")
    else:
        print("Enter lower number")

    guess = int(input("Enter your new number: "))
    counter += 1

print("You've Got It Right")
print("You took", counter, "Attempts")