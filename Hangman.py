import random
from os import system

def hangman(point):
    if point == 5:
        print("    ")
        print("|||            ")
        print("|||             ")          
        print("|||             ")         
        print("|||             ")     
        print("|||  FIVE LIFE LEFT TO HANG")                  
        print("|||              ") 
    elif point == 4:
        print("    ____________")
        print("|||            |")
        print("|||             ")          
        print("|||             ")         
        print("|||             ")     
        print("|||  FOUR LIFE LEFT TO HANG")                  
        print("|||              ")   
    elif point == 3:
        print("    ____________")
        print("|||            |")
        print("|||            O  ")          
        print("|||            |  ")         
        print("|||               ")     
        print("|||  THREE LIFE LEFT TO HANG ")                  
        print("|||              ") 
    elif point == 2:
        print("    ____________")
        print("|||            |")
        print("|||            O  ")          
        print("|||           /|\  ")         
        print("|||                ")     
        print("|||   TWO LIFE LEFT TO HANG ")                  
        print("|||              ")
    elif point == 1:
        print("    ____________")
        print("|||            |")
        print("|||            O  ")          
        print("|||           /|\  ")         
        print("|||           / \     ")     
        print("|||    ONE LIFE LEFT TO HANG ")                  
        print("|||              ") 
    elif point == 0:
        print("    ____________")
        print("|||            |")
        print("|||            O  ")          
        print("|||           /|\  ")         
        print("|||          _/ \_     ")     
        print("|||        GAME OVER ")                  
        print("|||              ") 
    elif point == 45:
        print("   ")
        print("         ")
        print("         ")
        print("   O  ")          
        print("  /|\  ")         
        print(" _/ \_  WON YOU ARE FREE   ")     
        print("     ")                  




word_list = ["Nobel","Retired","Polyman","Lolipop","Police","File","Over","Safe","Kidnap","World","Saga"]

word = random.choice(word_list)

print(list(word))

tree_word = []

list_word = list(word)
for i in range(len(list_word)):
    tree_word.insert(i,'_')



che = True

point = 5

entered = True

while che:
    system('cls')
    hangman(point)
    print(str(tree_word))
    entered = True
    letter = input("Guess the letter and press 'Enter' \n")
    for i in range(len(list_word)):
        if letter in list_word[i]:
            tree_word[i] = letter
            entered = False
    if entered:
        point-=1
    if '_' not in tree_word:
        system('cls')
        che = False
        hangman(45)
    if point == 0:
        system('cls')
        che = False
        hangman(point)

