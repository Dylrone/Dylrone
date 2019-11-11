def qdns():
    q=int(input("Enter # of Quarters: "))
    d=int(input("Enter # of Dimes: "))
    n=int(input("Enter # of Nickels: "))
    s=int(input("Enter # of Pennies: "))
    total=float(((q*25)+(d*10)+(n*5)+(s*1))/100)
    print("You have $",total,)
qdns()
