list = []
n = int(input("Enter the size of list:->  "))
mul=1
print("Enter",n , "Numbers in List")
for i in range(0, n):
    item = int(input())
    list.append(item)
    mul=mul*item
print("List is:-> ", list)
print("Multiplication of Elements in List is:-> ",mul)