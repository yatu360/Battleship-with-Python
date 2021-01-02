import random
import copy

def is_sunk(ship):
   if ship[3]==len(ship[4]):    return True
   else:    return False

def ship_type(ship):
    #remove pass and add your implementation
    pass

def is_open_sea(row, column, fleet):
    for x in range(len(fleet)):
        r = fleet[x][0]
        c = fleet[x][1]
        if fleet [x][2] == False and row >= r-1 and row <= (r+fleet[x][3]) and column >= c-1 and column <= c+1:
                return False
        if fleet [x][2] == True and row >= r-1 and row <= r+1 and column >= c-1 and column <= (c+fleet[x][3]):
                return False 
    return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    row1 = 0
    col1 = 0
    count = 0
    for x in range(length):
        if horizontal == True:
            if (column+length)>9:
                return False
            else:
                col1 = column + x
                if is_open_sea(row, col1, fleet) == True:
                    count +=1
                    if count == length:
                        place_ship_at (row, column, horizontal, length, fleet)
                else:
                    return False
     
        else:
            if (row+length)>9:
                return False
            else:
                row1 = row + x
                if is_open_sea(row1, column, fleet) == True:
                    count +=1
                    if count == length:
                        place_ship_at (row, column, horizontal, length, fleet)
                else:
                    return False

def place_ship_at(row, column, horizontal, length, fleet):
    s = []
    s.append(row)
    s.append(column)
    s.append(horizontal)
    s.append(length)
    s.append(set())
    fleet.append(tuple(s))    
    return fleet

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

def check_if_hits(row, column, fleet):
    for x in range(len(fleet)):
        r = fleet[x][0]
        c = fleet[x][1]
        if fleet [x][2] == False and row >= r and row <= (r+(fleet[x][3]-1)) and column == c:
                return True
        if fleet [x][2] == True and row == r  and column >= c and column <= (c+(fleet[x][3])-1):
                return True 
    return False


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

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
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

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()