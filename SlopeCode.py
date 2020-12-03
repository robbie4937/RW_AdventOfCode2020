#entry conditions
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
trees_encountered = []

# Read terrain
with open("Slope_Main.txt") as input_file: 
    tree_lines = [line.strip() for line in input_file] 
    print(tree_lines)
    y_limit=len(tree_lines)
    #print(y_limit)

for slope in slopes:
    trees_on_route = 0
    X_pos = 0 
    Y_pos = 0 

    #within limit of y axis - move along by value and circle around with remainder (length of tree lines will be consistent [31]) - x will move along remained when it gets to end
    while Y_pos + 1 < y_limit: 
        X_pos = (X_pos + slope[0]) % len(tree_lines[0])      
        Y_pos += slope[1] 
        if tree_lines[Y_pos][X_pos] == '#': 
                trees_on_route += 1 
    trees_encountered.append(trees_on_route)
print(trees_encountered)

from functools import reduce
Total = reduce(lambda x,y: x*y,trees_encountered)
print(Total)