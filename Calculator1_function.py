#Create a function named Calculator which takes three arguments - number_x, number_y, operation. number_x and number_y we will take two integers and operation parameter defines the type of mathematical operation to be performed on the two integers.
def calculator(numberX,numberY,operator):
    if operator=="add":
        result=numberX+numberY
    elif operator=="subtract":
        result=numberX-numberY
    elif operator=="multiply":
        result=numberX*numberY
    elif operator=="divide":
        result=numberX/numberY
    return result

add=calculator(20,25,"add")
print("sum:",add)
subtract=calculator(40,3,"subtract")
print("difference:",subtract)
multiply=calculator(10,4,"multiply")
print("product:",multiply)
divide=calculator(40,4,"divide")
print("divide:",divide)

# number_1=calculator(20,24,"add")
# number_2=calculator(50,60,"multiply")
# number_3=calculator(80,120,"divide")
# number_4=calculator(90,23,"subtract")
# print("add",number_1)
# print("multiply",number_2)
# print("divide",number_3)
# print("substract",number_4)
