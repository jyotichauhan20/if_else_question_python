quantity=int(input("enter the number"))
discount=int(input("enter the number"))
total_discount=quantity/100*10
if quantity>=1200:
    total_discount=quantity-discount
    print("total_discount",total_discount)
else:
    print("no_doscount")    