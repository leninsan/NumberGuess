myNumber = 4
permission = True
def guessNumber(myNumber):
    num = int(input("Please enter a number from the 1 to 10 for to guess if i have in my number list:\n"))
    if (num > myNumber):
        print(f"My number is less than {num}\n")
        return True
    elif(num < myNumber):
        print(f"My number is greater than {num} \n")
        return True
    else:
        print(f"You have won!!, the {num} is my number\n") 
        return False
    

while(guessNumber(myNumber)):
    pass