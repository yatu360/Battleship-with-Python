import random

def is_sunk(ship):
    #remove pass and add your implementation
    pass

def ship_type(ship):
    #remove pass and add your implementation
    pass

def is_open_sea(row, column, fleet):
    check = (row, column)
    for x in range(len(fleet)):
        if check in fleet[x][4]:
            return False
        else: 
            for coord in fleet[x][4]:
                r = coord[0]
                c = coord[1]
                if check == (r+1, c) or check ==(r, c+1) or check==(r-1, c) or check==(r, c-1) or check == (r-1, c-1) or check==(r+1, c+1) or check==(r+1, c-1) or check == (r-1, c+1):
                    return False
    #print(check)
    return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    row1 = 0
    col1 = 0
    count = 0
    for x in range(length):
        if horizontal == True:
            if (column+length)>9:
                return fleet
            else:
                col1 = column + x
                if is_open_sea(row, col1, fleet) == True:
                    count +=1
                    if count == length:
                        place_ship_at (row, column, horizontal, length, fleet)
     
        else:
            if (row+length)>9:
                return fleet
            else:
                row1 = row + x
                if is_open_sea(row1, column, fleet) == True:
                    count +=1
                    if count == length:
                        place_ship_at (row, column, horizontal, length, fleet)

def place_ship_at(row, column, horizontal, length, fleet):
    ship = []
    s = []
    for x in range(length):
        if horizontal == True:
            ship_cod = (row, column+x)
        else:
            ship_cod = (row+x, column)
        ship.append(ship_cod)
    s.append(row)
    s.append(column)
    s.append(horizontal)
    s.append(length)
    s.append(set(ship))
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
    #remove pass and add your implementation
    pass

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

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