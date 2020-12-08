data = []

with open("Boot.txt") as f:
    data=[line.strip()for line in f]


def get_acc():
    acc = 0
    line = 0
    instructions = []



    while line not in instructions:
        instructions.append(line)

        currentInstruction = data[line]
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
    return acc


acc = get_acc()
print (acc)
