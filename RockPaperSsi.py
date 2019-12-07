from six.moves import input
import random
from random import randint

list = ["Rock","Paper", "Siscors"]



while True:
    while True:
        Computer = list[randint(0,2)]
        print(Computer)
        input2 = str(input("Enter here: "))
        if input2 == Computer:
            print("draw")  
            break    
        elif input2 == "Rock" and Computer == "Paper":
            print("Computer wins!")
            break
        elif input2 == "Rock" and Computer == "Siscors":
            print("You win!")   
            break   
        elif input2 == "Paper" and Computer == "Siscors":
            print("Computer wins!")  
            break
        elif input2 == "Paper" and Computer == "Rock":
            print("You win!")     
            break
        elif input2 == "Siscors" and Computer == "Rock":
            print("Computer wins!")
            break
        elif input2 == "Siscors" and Computer =="Paper":
            print("You win!")
            break
        else: 
            if input2 == "":
                print("Enter a valid value and try again ")
                del input2
                break

    Computer = list[randint(0,2)]
    print(Computer)        
    input = str(input("Enter here: "))
    if input == Computer:
        print("draw")  
        break    
    elif input == "Rock" and Computer == "Paper":
        print("Computer wins!")
        break
    elif input == "Rock" and Computer == "Siscors":
        print("You win!")    
        break   
    elif input == "Paper" and Computer == "Siscors":
        print("Computer wins!")  
        break
    elif input == "Paper" and Computer == "Rock":
        print("You win!")     
        break
    elif input == "Siscors" and Computer == "Rock":
        print("Computer wins!")
        break
    elif input == "Siscors" and Computer =="Paper":
        print("You win!")
        
        break
    else: 
        if input == "":
            print("Enter a valid value and try again ")
            del input 
            break 

print("GameOver")

#Add total Number of wins in the future. 


            
            