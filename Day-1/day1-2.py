#opening the file and storing into a variable called x
f = open("input.txt")
x = f.read()

x = x.splitlines() #splitting the lines of the file into a list



#initializing an empty list and then appending the values of the list x into the list y after converting them into integers and if it isnt a integer we continue
y = []
for i in x:
    if i!="":
        y.append(int(i))
    else:
        y.append(i)
        


#initialising and empty list called cal and  calculating the sum of calories for each elf until an empty string is encountered after which we append the sum to the cal list and then reset the sum to 0
sum = 0
cal = []
for i in y: 
    if i !="":
        sum += i
    else:
        cal.append(sum)
        sum = 0
cal.append(sum)

#we reverse sort the cal list with the sum of the calories of each elf
sort_cal= sorted(cal,reverse=True)

#then we print out the top 3 calories 
print(sort_cal[0]+sort_cal[1]+sort_cal[2])
