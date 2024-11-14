1import random

score = total = 0
choice = 'c'

print("WELCOME to Role The DICE Game🎉🎉🎉") 

while choice[0].lower() == 'c':
    a = int(input("Please Enter Input Between 1 to 6: "))
    
    total += 1

    if not 1 <= a <= 6 :
        print('Please Enter Within the Described Range')
        continue
    else:
        print("You have Guessed Wrong,\nbut don't lose hope. You can win next round.")
        
    b = random.randint(1, 6)
    
    if a == b:
        score += 1

        print("CONGRATULATIONS!!!, You have Won this Round")
        choice = input('Would you want to Countinue or Exit: C/E')


print(f"Your Score is {score} out of {total}")
print("Thanks For Playing 🎉🎉🎉")
