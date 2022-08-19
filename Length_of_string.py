#Write a Python program to count the number of strings where the string length is 2 or more and the 
#first and last characters are the same from a given list of strings.
#list=['abc', 'xyz', 'aba', '1221']
#result= 2.
def string(list):
    i=0
    count=0
    while i<len(list):
        if list[i][0]==list[i][-1]:
            count=count+1 
        i=i+1
    print(count)
list=['abc', 'xyz', 'aba', '1221']
string(list)