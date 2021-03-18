#Vincent Ciarcia
#This program is a numbers game
#The objective is for the player to figure out the patern
#and solve the simple math question
def main():
    guess = 0
    count = 0
    key = False
    print("Hi! Welcome to my game!")#Greeting
    while key == False:
        guess = int(input("What is 2+2? "))#minus
        if guess == 5:
            print("You entered: ",guess-1,". Nice job!", sep='')#sep=''
            key = True
            break
        elif guess == 4:
            print("You entered: ",guess-1,". Haven't got it yet? Try again!", sep='')
        else:
            print("You entered: ",guess-1,". Nope. Try again!", sep='')
        guess = int(input("What is 2+2? "))#add
        if guess == 3:
            print("You entered: ",guess+1,". Nice job!", sep='')
            key = True
            break
        elif guess == 4:
            print("You entered: ",guess+1,". Haven't got it yet? Try again!", sep='')
        else:
            print("You entered: ",guess+1,". Nope. Try again!", sep='')
    print("Ok, that was an easy one!", end =' How ')#end=''
    print("about a slightly more challenging one?")
    key=False
    while key == False:
        guess = int(input("What is 3x4? "))#times 2
        if guess == 6:
            print("You entered: ",guess*2,". Nice job!", sep='')
            key = True
            break
        elif guess == 12:
            print("You entered: ",guess*2,". Haven't got it yet? Try again!", sep='')
        else:
            print("You entered: ",guess*2,". Nope. Try again!", sep='')
        guess = int(input("What is 3x4? "))#times 3
        if guess == 4:
            print("You entered: ",guess*3,". Nice job!", sep='')
            key = True
            break
        elif guess == 12:
            print("You entered: ",guess*3,". Haven't got it yet? Try again!", sep='')
        else:
            print("You entered: ",guess*3,". Nope. Try again!", sep='')
    print("Ok, Now for a really hard one!")
    key=False
    while key == False:
        guess = int(input("What is 7x11? "))#odd vs even
        if guess == 154:#divide
            print("You entered: ",int(guess/2),". Nice job!", sep='')
            key = True
            break
        elif guess%2 != 0:#multiply (remainder)
            print("You entered: ",guess*2,". Try an even number.", sep='')
        elif guess == 77:
            print("You entered: ",guess*2,". Haven't got it yet? Try again!",sep='')
        else:
            print("You entered: ",int(guess/2),". Try an odd number.", sep='')
    print("Nice! "*10 + " Happy Birthday")#string multiply/concatenate
    print("Nice! Now another challenge!")
    key=False
    while key == False:
        guess = int(input("What is 25x9? "))#power
        if guess == 15:
            print("You entered: ",guess**2,". Nice job!", sep='')
            key = True
            break
        else:
            print("You entered: ",guess**2,". Try again!", sep='')
        guess = int(input("What is 25x9? "))#floor
        if guess == 2250:
            print("You entered: ",guess//2,". Nice job!", sep='')
            key = True
            break
        else:
            print("You entered: ",guess//2,". Try again!", sep='')
    print("Nice Job! Here's another one!")
    key=False
    while key == False:
        count += 1
        guess = int(input("Guess a number from 1 through 10: "))
        if 1 <= messItUp(guess) <= 10:
            print("You entered: ", messItUp(guess), " Nice Job!", sep='')
            key = True
        elif messItUp(guess) > 10:
            print("You entered: ", messItUp(guess))
            print("Too high! Try again!")
            if count > 9:
                print("what's the ONE number your haven't tried?")
        else:
            print("You entered: ", messItUp(guess))
            print("Too low! How did you even get here?")
    print("Excellent work!")


def messItUp(num): #Vlue returning function
    temp = num**8
    temp = temp%107
    return (temp)

main()
