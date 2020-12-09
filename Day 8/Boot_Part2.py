data = []

with open("Boot.txt") as f:
    data=[line.strip()for line in f]

def get_acc_endOfFile():
    acc = 0
    line = 0
    instructions = []

    while line not in instructions:
        instructions.append(line)
        currentInstruction = data[line]
        #print(currentInstruction)
        currentInstruction=currentInstruction.split()
        cmd = currentInstruction[0]
        #print (cmd)
        num = int(currentInstruction[1])
        #print(num)

        if cmd == "acc":
            acc += num
            line += 1
        elif cmd == "jmp":
            line += num
        elif cmd  == "nop":
            line += 1
        
        if line >= len(data):
            return acc, True

    return acc, False


for i in range(len(data)):
    if "jmp" in data[i]:
        data[i]=data[i].replace("jmp", "nop")
        acc, found = get_acc_endOfFile()

        if found:
            print (acc)
            break
        else: 
            data[i] = data[i].replace ("nop", "jmp")

