file= open("E:\Python Assignments\hello.txt", 'r') 
file1= open("E:\Python Assignments\copyHello.txt", 'w') 
for line in file:
    file1.write(line)
print("Data copied Successfully.....!")