f = open("input.txt")
x = f.read()

x = x.splitlines()
# print(x)



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
cal.append(sum)
# print(cal)
sort_cal= sorted(cal,reverse=True)
# print(sort_cal)

print(sort_cal[0]+sort_cal[1]+sort_cal[2])
