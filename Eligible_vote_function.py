#Create a funciton named eligibleforvote which tell the user if he/she is eligible to vote or not.( Consider minimum age of voting to be 18.
def eligibleforvote():
    age=int(input("enter the age:"))
    if age>=18:
        print("You are eligible.")
    else:
        print("You are not eligible.")
eligibleforvote()
