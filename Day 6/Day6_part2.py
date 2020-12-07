
with open("Group_Questionaire.txt") as f:
     GroupData=[]
     GroupData = f.read().split("\n\n")
     #print(GroupData)


# Part 1 logic
any_yes = 0
for group in GroupData:
    any_yes += len(set(group.replace('\n', '')))
    #print(any_yes)

#Part 2 logic
all_yes = 0
for group in GroupData:
    passangers=group.split("\n")
    #print(passangers)
    for letter in passangers[0]:
        yes_correct=[letter for passangers in passangers if letter in passangers]
        #print(letter)
        #print(yes_correct)
        if len(yes_correct) == len(passangers):
            all_yes +=1

print(all_yes)