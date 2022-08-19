def string(list):
    i=0
    a=""
    while i<len(list):
        if list[i]!=list[i-1]:
            a=a+list[i]
        i=i+1
    # a=a+list[i]
    print("\""+a+"\"")
list=['a','b','b','c','c','d','e','e','e','f','g'] 
string(list)
