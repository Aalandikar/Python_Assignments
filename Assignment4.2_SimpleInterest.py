i=1
while(i<4):
    p=float(input("Enter Principle Amount:->"))
    n=int(input("Enter Number Of Years:->"))
    r=float(input("Enter Rate of Interest:->"))
    si=(p*n*r)/100
    print("Simple Interest => ",si)
    i+=1

"""for i in range(1, 6):
    print(str(i) * i)"""