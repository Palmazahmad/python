# use exit() to leave terminal 
import random 
global input 
guess = random.randrange(0, 10)
print(guess)

input = int(input("enter guess: "))

if input == guess:
    print("correct")
elif input > guess:
    print("too high")
elif input < guess:
        print("too low")

