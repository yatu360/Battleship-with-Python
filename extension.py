from tkinter import*
from functools import partial
import battleships


current_fleet = battleships.randomly_place_all_ships()
root = Tk() 
root.title("Battleship Game by Yathurshen Muralitharan") #Set window title
label2= Label(root, text="")                                              #Creates a label widget using the label class
label2.grid(row=11, column=1, columnspan=10)                              #Set its position on the form using the grid function and provides it the location
label3= Label(root, text="")
label3.grid(row=12, column=1, columnspan=10)
label4= Label(root, text="")g
label4.grid(row=13, column=1, columnspan=10)
label5= Label(root, text="")
label5.grid(row=14, column=1, columnspan=10)
label6 = Label(root, text="Hit Key: Grey = Not Attempted ", fg="black")
label6.grid(row=15, column=0, columnspan=9)
label6 = Label(root, text="Blue = Miss ", fg="blue")
label6.grid(row=15, column=2, columnspan=10)
label6 = Label(root, text="Red = Hit ", fg="red")                          ##Set its position on the form using the grid function, provides it the location and other attributes like colour
label6.grid(row=15, column=5, columnspan=10)
label9 = Label(root, text="Ship Key: B = Battleship (4 shots), C = Cruiser(3 shots), D = Destroyer (2 shots), S = Submarine (1 shot) ", fg="blue")
label9.grid(row=16, column=1, columnspan=10)
shots = 0
game_over = False


def button_click(number):
    '''
    This function is called when a button is clicked and sends the cordinates (row and column) to the battleship program where the information is processed and
    gets returned if the shot has hit a ship or not. This function also checks if the shot ship has been sunk and if there are any remaining ships left to be sunked. When a ship
    is sunked, ship_hit is passed to ship_reveal.
    '''
    global shots
    global current_fleet
    global game_over
    if game_over==False:
        shots +=1
        row = number[0]
        col = number[1]
        if battleships.check_if_hits(row, col, current_fleet):
            if battleships.check_if_not_already_hit(row, col, current_fleet):
                label2.config(text = "You have a hit!")
                Button(root, text=" ", bg="red", height=1, width=1, padx=20, pady=10, command=partial(button_click, (row, col)), relief="sunken").grid(column=col+1, row=row+1, sticky=W) #changes the attributes of the existing buttons to sunken to make the player aware this is already hit and red (because fire is read) 
                (current_fleet, ship_hit) = battleships.hit(row, col, current_fleet)
                if battleships.is_sunk(ship_hit):
                    ship_reveal(ship_hit)
                    disptext = ("You sank a " + battleships.ship_type(ship_hit) + "!")
                    label3.config(text= disptext)
            else:
                label2.config(text = "You missed!")
                label3.config(text = " ")
        else:
            label2.config(text = "You missed!")
            Button(root, text=" ", bg="blue",height=1, width=1, padx=20, pady=10, command=partial(button_click, (row, col)), relief="sunken").grid(column=col+1, row=row+1, sticky=W) #changes the attributes of the existing buttons to sunken to make the player aware this is already hit and blue (because sea/ocean is blue) 
            label3.config(text = " ")

        shotstaken= ("Shots taken: "+ str(shots))
        label4.config(text=shotstaken)
        if not battleships.are_unsunk_ships_left(current_fleet): 
            label5.config(text= "Game over! You required: " + str(shots) +" shots.")
            game_over=True
    

def ship_reveal(ship_hit):
    '''
    This function is called when a ship is sunked to reveal the type of ship on the board. It receives ship_hit from button_click function, then changes the attributes of the cell buttons
    to contain the respective ship identifier.
    '''
    ship_dict = {4: "B", 3: "C", 2: "D", 1: "S"}
    for coordinate in sorted(ship_hit[4]):
        Button(root, text=ship_dict[ship_hit[3]], bg="red", fg="white",height=1, width=1, padx=20, pady=10, command=partial(button_click, (coordinate[0], coordinate[1])), relief="sunken").grid(column=coordinate[1]+1, row=coordinate[0]+1, sticky=W)
    
def close_window(): 
    '''
    This function is called when the player clicks exit game button.
    '''
    root.destroy()  # Terminates the mainloop and deletes all widgets.

def new_game():
    '''
    This function is an extra to create a proper game feel, where it's called when the player clicks the 'New Game' button
    '''
    global current_fleet
    global shots
    global game_over
    game_over = False
    shots = 0
    current_fleet = battleships.randomly_place_all_ships()
    button_placement()
    label2.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")

    
def button_placement():
    '''
    This function creates the 10x10 visual grid buttons and assigns each button to its respective cordinates, ex: top left is (0, 0) and bottow right is (9, 9)
    '''
    for x in range(1, 11): #For loop for row iteration 
        for y in range(1, 11):  #For loop for column iteration
    
            btn = Button(root, text=" ", height=1, width=1, padx=20, pady=10, command=partial(button_click, (x-1, y-1)))
            btn.grid(column=y, row=x, sticky=W)
    
    Button(root, text="Exit", fg="red", padx=20, pady=10, command=partial(close_window)).grid(column=11, row=12, rowspan=3, sticky=W)
    Button(root, text="New Game", fg="blue", padx=20, pady=10, command=partial(new_game)).grid(column=0, row=12, columnspan=3, rowspan=3, sticky=W)

def grid_placement():
    '''
    This function creates the row and column labels which is a requirement in the spec.
    '''
    for y in range(10):
        label1= Label(root, text=y, padx=20, pady=10)
        label1.grid(row=0, column=y+1)

    for x in range(10): 
        label1= Label(root, text=x, padx=20, pady=10)
        label1.grid(row=x+1, column=0)


def main():
    '''
    The main function which starts the execution of all the functions.
    '''
    grid_placement()
    button_placement() 

    root.mainloop()



if __name__ == '__main__': 
   main()
