#Write a Python function that accepts a string and calculate the number of upper case letters and 
# lower case letters.
def alphabets(string):
    i=0
    count_UPPER=0
    count_lower=0
    while i<len(string):
        if string[i]>="A" and string[i]<="Z":
            count_UPPER=count_UPPER+1
        elif string[i]>="a" and string[i]<="z":
            count_lower=count_lower+1
        i=i+1
    print("Number of UPPER case:",count_UPPER)
    print("Number of lower case:",count_lower)
string=input("enter the string:")
alphabets(string)