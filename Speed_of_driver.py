#Define a function that checks the speed of drivers. This function will take a 
#parameter named speed, and will satisfy the following conditions:
#1.If speed if less than 70, print 70.
#2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
#3. If points are more than 12, print “License suspended”
def speed_of_driver(speed):
    if speed<70:
        print("70")
    else:
        speed1=speed-70
        point=speed1//5
        if point<=12:
            print("point is",point)
        else:
            print("point",point,"-","License suspended")
speed=int(input("enter the speed:"))
speed_of_driver(speed)