import random
score=0
while True:
    num=random.randint(1,6)
    guess=int(input("Guess the roll,0 to quit game:"))
    if guess==0:
        print("Thank you for playing the game. Your score is:",score)
        exit()
    elif(0<guess<7):
        if guess==num:
            score+=1
            print("Right guess!!","Your score is:",score)
        else:
            print("Opps! Better luck next time")
    else:
        print("Guess a number between 1 and 6 only")

# 