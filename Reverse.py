#Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Output : "dcba4321".
# def reverse(string):
#     print(string[::-1])
# string="dcba4321"
# reverse(string)

def reverse(list):
    list=[1,2,3,4]
    i=-1
    a=[]
    while i>=-len(list):
        a.append(list[i])
        i=i-1
    return a
print(reverse(list))