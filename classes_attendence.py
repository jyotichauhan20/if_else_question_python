held=int(input("enter the number"))
attendence=int(input("enter the number"))
classes_persantage =held/attendence*100
if classes_persantage>=75:  
    print("allow to sit exaim")
else:
    print("no allow to sit exaim")