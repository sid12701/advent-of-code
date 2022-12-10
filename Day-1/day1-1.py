#this is the function to open and print the contents of a text file 
f = open("input.txt")
x = f.read()

#seperating the input based on whitespaces
x = x.splitlines()
print(x)

#converting the string input in list to int and adding to a new empty list
y = []
for i in x:
    if i!="":
        y.append(int(i))
    else:
        y.append(i) 

#initialising a sum to 0 to help calculate the sum of calories for each elf
sum = 0

#create an empty lit to add the sum of calories for each elf that are seperated by the empty space.
cal = []
for i in y: 
    if i !="":
        sum += i
    else:
        cal.append(sum)
        sum = 0
cal.append(sum) #we append sum again because the final element of the list does not have an empty space after it
        
print(cal)
print(max(cal))