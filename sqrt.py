from math import sqrt
def square(x=0,y=0):

        for i in range(x,y+1):
            num=int(i*i)
            if (num>x and num<y):
                print (num)


x=int(input("enter frist number : "))
y=int(input("enter second number : "))
square(x,y)










