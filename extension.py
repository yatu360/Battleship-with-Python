from tkinter import*
from functools import partial

import battleships


current_fleet = battleships.randomly_place_all_ships()
root = Tk()
root.title("Battleship Game")
label2= Label(root, text="")
label2.grid(row=11, column=0, columnspan=10)
label3= Label(root, text="")
label3.grid(row=12, column=0, columnspan=10)



def button_click(number):

    global current_fleet
    row = number[0]
    col = number[1]
    if battleships.check_if_hits(row, col, current_fleet):
        label2.config(text = "You have a hit!")
        Button(root, text="", bg="red", padx=20, pady=10, command=partial(button_click, (row, col)), relief="sunken").grid(column=col+1, row=row+1, sticky=W)
        (current_fleet, ship_hit) = battleships.hit(row, col, current_fleet)
        if battleships.is_sunk(ship_hit):
                disptext = ("You sank a " + battleships.ship_type(ship_hit) + "!")
                label3.config(text= disptext)
    else:
        label2.config(text = "You missed!")
        Button(root, text="", bg="blue", padx=20, pady=10, command=partial(button_click, (row, col)), relief="sunken").grid(column=col+1, row=row+1, sticky=W)
        label3.config(text = " ")
    
    




def main():
   
    for y in range(10): #use this as row count
        label1= Label(root, text=y, padx=20, pady=10)
        label1.grid(row=0, column=y+1)

    for x in range(10): #use this as row count
        label1= Label(root, text=x, padx=20, pady=10)
        label1.grid(row=x+1, column=0)

    for x in range(1, 11): #use this as row count
        for y in range(1, 11):
    
            btn = Button(root, text="", padx=20, pady=10, command=partial(button_click, (x-1, y-1)))
            btn.grid(column=y, row=x, sticky=W)

    root.mainloop()

if __name__ == '__main__': #keep this in
   main()
