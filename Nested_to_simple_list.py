# a=[1,2,[3,4[5,6],7,8,[9,[10]]]]
# a=[1,2,3,[4,[5,6,[7]],8],[9]]
# b=[]
# def fun(a):
#     for i in a:
#         if type(i)==list:
#             fun(i)
#         else:
#             b.append(i)
# print(a)
# fun(a)
# print(b) 


def items(a):
    new_list=[]
    i=0
    while i<len(a):
        if type(a[i]) is list:
            new_list.extend(a[i])
        else:
            new_list.append(a[i])
        i+=1
    print(new_list)
a=[1,2,[3,4],[5,6],7,8,[9,10]]
items(a) 

# def simple(a):
#     i=0
#     b=[]
#     while i<len(a):
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#         i+=1
#     print(b)
# a=[1,2,[3,4,[5,6],7,8,[9,[10]]]]
# simple(a)