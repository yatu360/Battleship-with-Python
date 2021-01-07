import random
import copy

'''
is_sunk-- Returns Boolean value, which is True if ship is sunk and False otherwise
'''
def is_sunk(ship):
   if ship[3]==len(ship[4]):    return True #checks if all the coordinates of the ship has been identified by the player
   else:    return False


'''
ship_type(ship) -- returns one of the strings "battleship", "cruiser", "destroyer", or "submarine" identifying the type of ship
'''
def ship_type(ship):
    ship_dict = {4: "battleship", 3: "cruiser", 2: "destroyer", 1: "submarines"}
    return ship_dict[ship[3]]   #Checks with the dictionary and returns the type of ship using the length of the ship stored in the data set.


'''
is_open_sea(row, column, fleet) -- checks if the square given by row and column neither contains nor is adjacent (horizontally, vertically, 
or diagonally) to some ship in fleet. Returns Boolean True if so and False otherwise
'''
def is_open_sea(row, column, fleet):
    for x in range(len(fleet)):
        r = fleet[x][0] #Iterates the already placed ships initial row location to r
        c = fleet[x][1] #Iterates the already placed ships initial row location to c
        if fleet [x][2] == False and row >= r-1 and row <= (r+fleet[x][3]) and column >= c-1 and column <= c+1: #Checks to see if the ship to be placed is outside the illegal zones 
                return False
        if fleet [x][2] == True and row >= r-1 and row <= r+1 and column >= c-1 and column <= (c+fleet[x][3]): #Same as above but when placed ships are horizontal
                return False 
    return True


'''
ok_to_place_ship_at(row, column, horizontal, length, fleet)-- checks if addition of a ship, specified by row, column, horizontal, and length as in ship 
representation above, to the fleet results in a legal arrangement (see the figure above). If so, the function returns Boolean True and it returns False otherwise. 
This function makes use of the function is_open_sea
'''
def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    row1 = 0
    col1 = 0
    count = 0
    for x in range(length):
        if horizontal == True:
            if (column+length)>9: #Restriction to not allow ships to be place outside grid from the y-axis(column)
                return False
            else:
                col1 = column + x
                if is_open_sea(row, col1, fleet) == True:
                    count +=1 
                    if count == length: #check to ensure all the coordinates of the ship is verified as legal
                        place_ship_at (row, column, horizontal, length, fleet)
                else:
                    return False
     
        else:
            if (row+length)>9: #Restriction to not allow ships to be place outside grid from the x-axis(row)
                return False
            else:
                row1 = row + x
                if is_open_sea(row1, column, fleet) == True:
                    count +=1
                    if count == length:
                        place_ship_at (row, column, horizontal, length, fleet)
                else:
                    return False


'''
place_ship_at(row, column, horizontal, length, fleet) -- returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, 
and length as in ship representation above, to fleet. It may be assumed that the resulting arrangement of the new fleet is legal.
'''
def place_ship_at(row, column, horizontal, length, fleet):
    s = []
    s.append(row)
    s.append(column)
    s.append(horizontal)
    s.append(length)
    s.append(set())
    fleet.append(tuple(s))    
    return fleet


'''
randomly_place_all_ships() -- returns a fleet that is a result of a random legal arrangement of the 10 ships in the ocean. This function makes use of the 
functions ok_to_place_ship_at and place_ship_at
'''
def randomly_place_all_ships():
    fleet = []
    while len(fleet) < 10:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        horizontal = bool(random.getrandbits(1))
        if len(fleet)<1:
            length = 4
        elif len(fleet)<3:
            length = 3
        elif len(fleet)<6:
            length = 2
        elif len(fleet) < 10:
            length = 1
        (ok_to_place_ship_at (row, col, horizontal, length, fleet))
    return fleet


'''
check_if_hits(row, column, fleet) -- returns Boolean value, which is True if the shot of the human player at the square represented by row and column hits any 
of the ships of fleet, and False otherwise.
'''
def check_if_hits(row, column, fleet):
    for x in range(len(fleet)):
        r = fleet[x][0]
        c = fleet[x][1]
        if fleet [x][2] == False and row >= r and row <= (r+(fleet[x][3]-1)) and column == c:   return True #Iterates to check if there is any hit
        if fleet [x][2] == True and row == r  and column >= c and column <= (c+(fleet[x][3])-1):    return True #Iterates to check if there is any hit
    return False


'''
hit(row, column, fleet) -- returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that receives a hit by the shot at the square represented by 
row and column, and fleet1 is the fleet resulting from this hit. It may be assumed that shooting at the square row, column results in hitting of some ship in fleet.
Note that ship must represent the ship after the hit.
'''
def hit(row, column, fleet):
    z = 0
    fleet1 = copy.deepcopy(fleet) 
    for x in range(len(fleet)):
        r = fleet[x][0]
        c = fleet[x][1]
        if fleet [x][2] == False and row >= r and row <= (r+(fleet[x][3]-1)) and column == c:
            fleet1[x][4].add((row, column))
            z = x
        if fleet [x][2] == True and row == r  and column >= c and column <= (c+(fleet[x][3])-1):
            fleet1[x][4].add((row, column))
            z = x
    return (fleet1, fleet1[z])


'''
are_unsunk_ships_left(fleet) -- returns Boolean value, which is True if there are ships in the fleet that are still not sunk, and False otherwise
'''
def are_unsunk_ships_left(fleet):
    for x in range(len(fleet)):
        if fleet[x][3]!=len(fleet[x][4]):   return True
    return False


'''
main -- Where the program starts the execution of all the functions
'''
def main():
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space) of Enter End to exit game: ")
        if loc_str == "End" or loc_str =="end":
            game_over=True
            break
        loc_str = loc_str.split()
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_ships_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()