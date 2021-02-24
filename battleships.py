#Name: Yathurshen Muralitharan
#Student ID: 13193494
#Github username & email: yatu360 -- yatu360@gmail.com
#BBK email: ymural01@student.bbk.ac.uk

import random

#19022021

def is_sunk(ship):
    '''
    Returns Boolean value, which is True if ship is sunk and False otherwise
    '''
    if ship[3]==len(ship[4]):   
        return True
    else:
        return False

def ship_type(ship):
    '''
    Returns one of the strings "battleship", "cruiser", "destroyer", or "submarine" identifying the type of ship
    '''
    ship_dict = {4: "battleship", 3: "cruiser", 2: "destroyer", 1: "submarine"}
    return ship_dict[ship[3]]   #Checks with the dictionary and returns the type of ship using the length of the ship stored in the data set..

def is_open_sea(row, column, fleet):
    '''
    Checks if the square given by row and column neither contains nor is adjacent (horizontally, vertically, 
    or diagonally) to some ship in fleet. Returns Boolean True if so and False otherwise
    '''
    for x in range(len(fleet)):
        r = fleet[x][0] #Iterates the already placed ships initial row location to r
        c = fleet[x][1] #Iterates the already placed ships initial row location to c
        if fleet [x][2] == False and row >= r-1 and row <= (r+fleet[x][3]) and column >= c-1 and column <= c+1: #Checks to see if the ship to be placed is outside the illegal zones 
                return False
        if fleet [x][2] == True and row >= r-1 and row <= r+1 and column >= c-1 and column <= (c+fleet[x][3]): #Same as above but when placed ships are horizontal
                return False 
    return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    '''
    Checks if addition of a ship, specified by row, column, horizontal, and length as in ship 
    representation above, to the fleet results in a legal arrangement (see the figure above). If so, the function returns Boolean True and it returns False otherwise. 
    This function makes use of the function is_open_sea
    '''
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
                        return True
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
                        return True
                else:
                    return False


def place_ship_at(row, column, horizontal, length, fleet):
    '''
    Returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, 
    and length as in ship representation above, to fleet. It may be assumed that the resulting arrangement of the new fleet is legal.
    '''
    s = []
    s.append(row)
    s.append(column)
    s.append(horizontal)
    s.append(length)
    s.append(set())
    fleet.append(tuple(s))    
    return fleet

def randomly_place_all_ships():
    '''
    Returns a fleet that is a result of a random legal arrangement of the 10 ships in the ocean. This function makes use of the 
    functions ok_to_place_ship_at and place_ship_at
    '''
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
        if (ok_to_place_ship_at (row, col, horizontal, length, fleet))==True:
            place_ship_at (row, col, horizontal, length, fleet)
    return fleet


def check_if_hits(row, column, fleet):
    '''
    Returns Boolean value, which is True if the shot of the human player at the square represented by row and column hits any 
    of the ships of fleet, and False otherwise.
    '''
    for x in range(len(fleet)):
        r = fleet[x][0]
        c = fleet[x][1]
        if fleet [x][2] == False and row >= r and row <= (r+(fleet[x][3]-1)) and column == c:   #Iterates to check if there is any hit
             return True 
        if fleet [x][2] == True and row == r  and column >= c and column <= (c+(fleet[x][3])-1):    #Iterates to check if there is any hit
            return True 
    return False


def hit(row, column, fleet):
    '''
    Returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that receives a hit by the shot at the square represented by 
    row and column, and fleet1 is the fleet resulting from this hit. It may be assumed that shooting at the square row, column results in hitting of some ship in fleet.
    Note that ship must represent the ship after the hit.
    '''
    z = 0
    fleet1 = fleet #Creates a shallow copy of fleet
    for x in range(len(fleet)):
        r = fleet[x][0]
        c = fleet[x][1]
        if fleet [x][2] == False and row >= r and row <= (r+(fleet[x][3]-1)) and column == c:
            fleet1[x][4].add((row, column))
            z = x
            break
        if fleet [x][2] == True and row == r  and column >= c and column <= (c+(fleet[x][3])-1):
            fleet1[x][4].add((row, column))
            z = x
            break
    return (fleet1, fleet1[z])

def are_unsunk_ships_left(fleet):
    '''
    Returns Boolean value, which is True if there are ships in the fleet that are still not sunk, and False otherwise
    '''
    for x in range(len(fleet)):
        if fleet[x][3]!=len(fleet[x][4]):   
            return True
    return False

def check_if_not_already_hit(row, column, fleet):
    '''
    Returns Boolean value, which is true if the location has not been hit before and false if it has.
    '''
    for x in range(len(fleet)):
        if (row, column) in fleet [x][4]:  #Iterates to check if there is any hit
            return False
    return True
            
def main():
    '''
    Where the program starts the execution of all the functions
    '''
    current_fleet = randomly_place_all_ships()
    game_over = False
    shots = 0
    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space) of Enter End to exit game: ")
        if loc_str == "End" or loc_str =="end":
            break
        try: #Catches any error for illegal entries (Only legal inputs will be counted as a shot)
            loc_str = loc_str.split()
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            if current_row<10 and current_column<10: #Forbids entry of out of bound entries
                shots += 1
                if check_if_hits(current_row, current_column, current_fleet):
                    if check_if_not_already_hit(current_row, current_column, current_fleet):
                        print("You have a hit!")
                        (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                        if is_sunk(ship_hit):
                            print("You sank a " + ship_type(ship_hit) + "!")
                    else:
                        print("You missed!")
                else:
                    print("You missed!")
            else:
                print("You tried to hit outside the allowed area, please try again within 0 to 9")
        except: #handles the error
            print("Enter valid input please, which is in range of 0 to 9 for row and column, separated by space ex: 1 5 ....or 'End' or 'end' to Exit")
        if not are_unsunk_ships_left(current_fleet): game_over = True
    if game_over == True:
        print("Game over! You required", shots, "shots.")
    else:
        print("Game over, you lost! You exited the game after", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()