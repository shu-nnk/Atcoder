def operate():
    print("Enter a number")
    x=int(input())

    if x==0:
        print("0 is entered")
        operate()
    elif x==1:
        print("1 is entered")
        operate()
    elif x ==2:
        print("2 is entered")
        operate()
    
    elif x==9:
        print("Exit")
        

    
operate()
    