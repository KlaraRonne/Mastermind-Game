
import random
import time

print("⚪ 🔴 🔵 🟤 🟢 🟣 🟡 🟠"[::-1])
print("   WELCOME TO MASTERMIND")
print("⚪ 🔴 🔵 🟤 🟢 🟣 🟡 🟠\n")

time.sleep(1)
print("The Code Maker is selecting the code\n\t.......")
time.sleep(2)

options=["B", "Y", "G", "R", "P", "T", "O", "C"]

def codemaking():
    '''The function generates random code of 4 colors. Outputs a list of strings'''
    result=random.sample(options,4)
    return result
code=codemaking()
print("The code has been chosen.\n\n")

time.sleep(1)
print("\t GOOD LUCK!\n")
time.sleep(1)
print("These are the colors:\n B=🔵 Y=🟡 G=🟢 R=🔴 P=🟣 T=🍀 O=🟠 C=🟤\n")
time.sleep(1)
print("If you do not wish to play anymore, type 'quit' any time\n")
time.sleep(1)

attempts=0
max_attempts=10
guess=[]
while attempts < max_attempts:
    print("You have 10 valid guesses!")
    guess=input("Choose your guess. Pick 4 different colors. e.g. BYGR  ")
    if guess=="quit":
        print("The player ended the game")
        break

    '''Valitadion check'''
    if len(guess)!=4:
        print("Please select exactly 4 colors!")
        continue
    if len(set(guess)) != 4:
        print("Please enter 4 different colors!")
        continue
    if not all(letter in options for letter in guess):
        print(f"Invalid colors! Use only: {options}")
        continue

    '''Increment attempts only if input was valid'''
    attempts+=1

    white=0
    red=0

    '''Function checks if color and position are the same'''
    for i in range(4):
        if guess[i]==code[i]:
            red+=1 
        elif guess[i] in code:
            white+=1


    if red==4:
        print(f"YOU WON!!\nThis was the code: {code}")
        break        

    print(f"Your guess: {guess}   R: {red}  W:{white} ")

   
else:
    print (f"You lost... The correct code was:  {code}")