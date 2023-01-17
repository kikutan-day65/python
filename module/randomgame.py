from random import randint
#generate a number 1 ~ 10
answer = randint(1,10)

lives = 4


# input from user?
# check that is a number 1 ~ 10
# check if number is the right guess. otherwise ask again

while True:
    try:
        guess = input('guess a number 1 ~ 10: ')
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print("you got it!")
                break
            else:
                lives -= 1
                print(f"miss! you have {lives} chances\n")
        else:
            print("plz enter 1 ~ 10")
        
        if lives == 0:
            print("You lose...")
            break

    except ValueError:
        print("plz enter a number")
        continue # to keep looping
