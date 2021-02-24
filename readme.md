 ## BATTLESHIPS
 
 ## To run the program please place both battleship.py and extension.py in the same folder and run extension.py
 
 
 ## General idea of the program

This program is based on the well-known game. Battleship is usually a two-player game, where each player has a fleet and an ocean (hidden from the other player), and tries to be the first to sink the other player's fleet. This is just a solo version, where the computer places the ships, and the human attempts to sink them. Designed to look similar to the retro minesweeper game. 

This program is built using test driven development.

The Ocean is a field of 10 x 10 squares. The squares are numbered from 0 to 9 in each dimension with numbers increasing from top to bottom and from left to right. 
![ocean](https://github.com/yatu360/Battleship-with-Python/blob/main/ocean.png)

The fleet consists of 10 ships. The fleet is made up of 4 different types of ships, each of different size as follows:

- One battleship, occupying 4 squares
- Two cruisers, each occupying 3 squares
- Three destroyers, each occupying 2 squares
- Four submarines, each occupying 1 square

![ships](https://github.com/yatu360/Battleship-with-Python/blob/main/battleships.png)

To begin the game, the computer places all the 10 ships of the fleet in the ocean randomly. Each ship can be placed either horizontally (as shown in the figure above) or vertically. Moreover, no ships may be immediately adjacent to each other, either horizontally, vertically, or diagonally. Examples of legal and illegal arrangements are shown below:
![legal and illegal arrangements](https://github.com/yatu360/Battleship-with-Python/blob/main/arrangement.png)

