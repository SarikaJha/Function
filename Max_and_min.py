b=[]
i=0
while i<3:
   
    num=int(input("enter the number:"))
    b.append(num)
    i=i+1
j=0
max=0
while j<len(b):
	if b[j]>max:
		max=b[j]
	j=j+1
a=0
min=b[a]
while a<len(b):
    if b[a]<min:
        min=b[a]
    a=a+1
	
print("max:",max)
print("min:",min)

