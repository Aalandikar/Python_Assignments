List=[10,51,21,20,60,81,61,42,11,68]
evenList=[]
oddList=[]
for i in List:
    if(i %2 == 0):
        evenList.append(i)
    else:
        oddList.append(i)
print("List Elements:-> ",List)
print("List Of Even Elements:-> ",evenList)
print("List Of Odd Elements:-> ",oddList)