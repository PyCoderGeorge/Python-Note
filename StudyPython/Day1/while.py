# Author: Junting

age_of_oldMan = 56
guess_num = 0

while guess_num < 3:
    guess_age = int(input("Guess age: "))
    if age_of_oldMan == guess_age:
        print("Yes, you got it!")
        break
    elif age_of_oldMan < guess_age:
        print("Think bigger")
    else:
        print("Think smaller")
    guess_num += 1
else:
    print('Yout have tried too many times...fuck off')


