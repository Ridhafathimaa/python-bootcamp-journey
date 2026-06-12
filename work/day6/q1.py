import random
num = random.randint(1,20)
attempts = 0

while True:
    guess = int(input("enter your guess(1-20): "))
    attempts += 1

    if guess == num:
        print("congratulations it is correct!")
        print("attempts: ",attempts)
    else:
        print("try again")