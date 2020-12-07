



with open("Group_Questionaire.txt") as f:
     GroupData=[]
     GroupData = f.read().split("\n\n")
     print(GroupData)


any_yes = 0
for group in GroupData:
    any_yes += len(set(group.replace('\n', '')))
    print(any_yes)
