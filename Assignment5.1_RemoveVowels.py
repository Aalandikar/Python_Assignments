userString=input("Enter Your String: ")
print("Given String is: " ,userString)
userString=userString.lower()

print("Input String After removing VOWELS:-> " )
for i in userString:
    if i=='a' or i=='e' or i=='i'or i=='o' or i=='u':
        continue
    else:
        print(i,end="")