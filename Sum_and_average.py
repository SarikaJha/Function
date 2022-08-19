#Create a function which takes 3 arguments(all integers) and prints their sum and average.
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
def sum_and_average(num1,num2,num3):
    sum=num1+num2+num3
    print(sum)
    avg=sum//3
    print(avg)
sum_and_average(num1,num2,num3)