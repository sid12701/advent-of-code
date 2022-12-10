#opening the file
#initializing two empty lists which will store mychoice and the opponent's choice
#splitting the contents of the file and storing the opponent's choice in the first list and my choice in the second list
with open("input-2.txt") as file:
    opponent =[]
    my_choice = []
    for line in file:
       (mine, them) = line.split()
       my_choice.append(them)
       opponent.append(mine)

#the values for choosing a certain choice and for loss,win or draw added together into seperare variables
win_rock = 7
draw_rock = 4
lose_rock = 1
win_paper = 8
draw_paper = 5
lose_paper = 2
win_sci = 9
draw_sci = 6
lose_sci= 3

#X=lose
#Y=draw
#Z=win
#A=rock
#B=paper
#C=scissor

score = 0

#using a zip function to iterate through the list.The first choice which is m here defines whethere if its a win,loss or draw for me
for m,o  in zip(my_choice,opponent): 
    if m=="X" and o=="A":
        score += lose_sci
    elif m=="X" and o=="B":
        score += lose_rock
    elif m=="X" and o=="C":
        score += lose_paper
    elif m=="Y" and o=="A":
        score += draw_rock
    elif m=="Y" and o=="B":
        score += draw_paper
    elif m=="Y" and o=="C":
        score += draw_sci
    elif m=="Z" and o=="A":
        score += win_paper
    elif m=="Z" and o=="B":
        score += win_sci
    elif m=="Z" and o=="C":
        score += win_rock
        
print(score)