#Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(string):
    string_list=list(string)
    i=-1
    a=[]
    while i>=-len(string):
        a.append(string[i])
        i=i-1
    if string_list==a:
        print(string,"is palindrome")
    else:
        print(string,"in not palindrome")
string=input("enter the string:")
palindrome(string)