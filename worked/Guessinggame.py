import random

def game(): #define methods/blocks for the function
    print("You're playing the game") #I just lost it
    try:
        endnumber=int(input("Enter end boundary: "))
    except:
        print("Enter a number this time...")
        game()

    ans=random.randint(0,endnumber)
    ask=str.upper(input("Do you want hints? Y/N "))

    if ask=="Y":
        hints=1
    else:
        print("No hints for you")
        hints=0
    print("You have 10 tries...")
    for i in range(1,11):
        user=int(input("Your guess: "))
        if user == ans:
            print("Correct")
            end()
        else:
            print("Incorrect")
            if hints==1:
                if user>ans:
                    print("You're too high")
                elif user<ans:
                    print("You're too low")
    print("No more guesses")
    end()

def end():
    ask=str.upper(input("Do you want redo? Y/N "))
    if ask=="Y":
        game()
    else:
        quit()

game()
