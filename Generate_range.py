#Implement a function named generateRange(min, max, step), which takes three arguments and generates a 
#range of integers from min to max, with the step. The first integer is the minimum value, the second
#is maximum of the range and the third is the step(min < max).
# def generateRange(min,max,step):
#     list=[]
#     if min<max:
#         for i in range(min,max+1,step):
#             list.append(i)
#         print(list)
#     else:
#         print("min is greater than max")
# min=int(input("enter min value:"))
# max=int(input("enter max value:"))
# step=int(input("enter no. of step:"))
# generateRange(min,max,step)

num = 1
def func():
    global num
    num = num + 3
    print(num)

func()
print(num)