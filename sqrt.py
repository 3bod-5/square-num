def square(x=0,y=0):
        for i in range(x,y+1):
            mylist=[]
            num=int(i*i)
            mylist.append(num)
            if(num>x and num<y):
                print(mylist , end=" , ")



x=int(input("enter frist number : "))
y=int(input("enter second number : "))
square(x,y)












