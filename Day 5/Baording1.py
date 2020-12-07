"""
RWilliams written 05/12/2020
"""

with open("BoardingLocation.txt") as f:
     PassData=[]
     PassData = [x.strip() for x in f] 
    # print(PassData)


def CalculateValue(c,lower, upper):	
	if c == "F" or c == "L":
		lower = lower
		upper = lower + (upper - lower) // 2
	elif c == "B" or c == "R":
		lower = lower + (upper - lower) //2 + 1
		upper = upper
	return lower, upper

def SeatNumbers(seat_list):
	id_list = list()
	for seat in seat_list: #look at every seat independently
		
		row_lower = 0
		row_upper = 127
		column_lower = 0
		column_upper = 7
		seat_id = 0

		for Character in seat[0:7]: #check the row of the seat in the plane
			row_lower, row_upper = CalculateValue(Character, row_lower, row_upper)

		for Character in seat[7:]: # check the column of the seat in the plane
			column_lower, column_upper = CalculateValue(Character, column_lower, column_upper)

		seat_id = row_lower * 8 + column_lower # calculate the seat id accourding to the website
		
		id_list.append(seat_id) # add seat id to list of seat id's 
	id_list.sort()	# sort the list of seat id's
	return(id_list)


def Seat_Identify (id_list):
	Bottom_Seat_Counter = int(id_list[0])
	for seat in range(len(id_list)):
		if id_list[seat] == Bottom_Seat_Counter:
			Bottom_Seat_Counter +=1
		else:
			if id_list[seat] == Bottom_Seat_Counter+1:
				return Bottom_Seat_Counter


Result = SeatNumbers(PassData)
#print ("Identifed Seats",Result)

Check = Seat_Identify(Result)
#print("My Seat",Check)