#You have to define a function named isGreaterThan20 in which you have to pass two parameters to the 
#function and the first parameter by default should be 20.
def isGreaterThan20(a,b=20):
    x=a>b
    print(x)
isGreaterThan20(30)