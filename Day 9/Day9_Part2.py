with open("Day9.txt") as f:
    data=[int(line.strip())for line in f]


def bad_number():
    for i in range(25,len(data)):
        inital = data[i-25:i]
        #print(inital)

        num = data[i]
        #print(num)
        found = False

        for j in range(len(inital)-1):
            for k in range(j+1,len(inital)):
                if inital[j]+inital[k]==num:
                    found = True
                    break
            if found == True:
                break
        if found == True:
            continue

        return num


num = bad_number()
#print(num)


# part 2

def get_key():
    bad_num = bad_number()
    found = False

    for i in range(len(data)-1):
        nums = [data[i]]
        for j in range(i+1, len(data)):
            nums.append(data[j])

            if sum(nums) == bad_num:
                found  = True
                break
            elif sum(nums) > bad_num:
                break

        if found == True:
            break
    return min(nums) + max(nums)


print(get_key())
