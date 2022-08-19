#Define a function which takes two arguments(strings) and returns the string with
# length. If both the strings have equal length, print both the strings one below the other.
#Hint :- use len() builtin function..
first=input("enter first string:")
second=input("enter second tring:")
def string(first,second):
    if len(first)>len(second):
        print(first)
    elif len(second)>len(first):
        print(second)
    elif len(first)==len(second):
        print(first)
        print(second)
string(first,second)