# def string(str,str_end):
#     i=0
#     while i<len(str and str_end):
#         if str[i] in str_end[i]:
#             print(True)
#         else:
#             print(False)
#         i=i+1
# str=input("enter the first string:")
# str_end=input("enter second string:")
# string(str,str_end) 


def solution(string, ending):
    i=len(string)-len(ending)
    new_str=""
    while i<len(string):
        new_str=new_str+string[i]
        i+=1
    if new_str==ending:
        print(True)
    else:
        print(False)
string=input("enter the string value:")
ending=input("enter the ending value:")
solution(string, ending)