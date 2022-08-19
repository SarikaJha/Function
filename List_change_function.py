#Write the code of a function named list_change which take 2 lists as integer
#arguments and then multiply the items of those lists which are on the same index
#number (order) and get them to return a new list.
def list_change(list1,list2):
    i=0
    a=[]
    while i<len(list1 and list2):
        list=list1[i]*list2[i]
        a.append(list)
        i=i+1
    print(a)
list_change([5, 10, 50, 20], [2, 20, 3, 5])