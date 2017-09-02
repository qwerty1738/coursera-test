#word = lion
from turtle import *
t = Turtle()

t.fd(100)
t.fd(100)
t.back(100)
t.lt(90)
t.fd(100)
t.rt(90)
t.circle(50)
t.rt(90)
t.fd(200)
t.rt(60)
t.fd(100)
t.back(100)
t.lt(120)
t.fd(100)

attempts = 5
print("Welcome to hangman, you have to figure out a random word by guessing letters that could be in that word.")
print("Your first word has 4 letters, and it is an animal. Don't repeat letters.")
print("Every wrong guess removes body parts from your human. If you lose all your body parts you lose the game. You can only make 5 mistakes, good luck.")
unneccesary = input("Press anything to continue")
print("|-------------------------------------|")
print("|        |||||||||   |||||||||        |")
print("|        |           |       |        |")
print("|        |           |       |        |")
print("|        |           |       |        |")
print("|        |           |       |        |")
print("|        |    ||||   |       |        |")
print("|        |      ||   |       |        |")
print("|        |||||||||   |||||||||        |")
print("|-------------------------------------|")  

lcount = 0
icount = 0
ocount = 0
ncount = 0

messagel = " _"
messagei = " _"
messageo = " _"
messagen = " _"

guessed = False
while not guessed:   
    answer = input("What letter do you guess?")
    if answer == ("l"):
        print("Correct, there is one L in the word. L " + messagei + messageo + messagen)
        lcount += 1
        messagel = "L "
        
    if answer == ("i"):
        print("Correct, there is one I in the word. " + messagel + " I" + messageo + messagen)
        icount += 1
        messagei = "I"
        
    if answer == ("o"):
        print("Correct, there is one O in the word. " + messagel + messagei + " O" + messagen)
        ocount += 1
        messageo = " O"
        
    if answer == ("n"):
        print("Correct, there is one N in the word. " + messagel + messagei + messageo + " N")
        ncount += 1
        messagen= " N"

    if answer == ("a") or (answer == "b") or (answer == "c") or (answer == "d") or (answer == "e") or (answer == "f") or (answer == "g") or (answer == "h") or (answer == "j") or (answer == "k") or (answer == "m") or (answer == "p") or (answer == "q") or (answer == "r") or (answer == "s") or (answer == "t") or (answer == "u") or (answer == "v") or (answer == "w") or (answer == "x") or (answer == "y") or (answer == "z"):
        attempts -= 1
        if attempts == 4:
            print("You lost your right leg!")
            t.undo()

        if attempts == 3:
            print("You lost your left leg!")
            t.undo()
            t.undo()
            t.undo()

        if attempts == 2:
            print("You lost your lower body and head!")
            t.undo()
            t.undo()
            t.undo()
            t.undo()

        if attempts == 1:
            print("You lost your neck and right arm!")
            t.undo()
            t.undo()
            t.undo()
            t.undo()
            t.undo()

        if attempts == 0:
            print("You lost your left arm, all your body parts are gone!")
            t.undo()
            print("You ran out of attempts, the word was lion, the game is over.")
            guessed = True
            exit()
                
        attempts = str(attempts)
        print("Wrong guess, the amount of attempts left: " + attempts)
        attempts = int(attempts)


    if lcount >= 1 and icount >= 1 and ocount >= 1 and ncount >= 1:
        print("You got all the letters. The word is lion, you won!")
        exit()



