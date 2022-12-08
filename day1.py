#this is the function to open and print the contents of a text file 
f = open("input.txt")
x = f.read()

#seperating the input based on whitespaces
x = x.splitlines()
print(x)

#converting string to int
y = []
for i in x:
    if i!="":
        y.append(int(i))
    else:
        y.append(i)
        
# print(y)
    


sum = 0
cal = []
for i in y: 
    if i !="":
        sum += i
    else:
        cal.append(sum)
        sum = 0
        

    
print(max(cal))