import pytest
from battleships import *

K = [(6, 2, True, 4, {(6,2), (6,5),(6,4)}), (5, 9, False, 3, {(5,9),(6,9)}), (4, 5, True, 3, {(4,5),(4,6),(4,7)}), (8, 1, True, 2,{(8,1),(8,2)}), (2, 9, False, 2, {(2,9), (3,9)}), (8, 5, True, 2, {(8,5), (8,6)}), \
        (1, 2, False, 1, {(1,2)}), (6, 7, True, 1, {(6,7)}), (2, 4, False, 1, {(2,4)}), (0, 6, False, 1, {(0,6)})] #This global list is used for the additional function check_if_not_already hit

s = (2, 3, False, 3, {(2,3), (3,3), (4,3)}) 


def test_is_sunk1():
    assert is_sunk(s) == True
    
def test_ship_type1():
    assert ship_type(s) == "cruiser"


s1_t1 = (5, 3, False, 3, set())
s2_t1 = (6, 9, False, 4, set())
f_t1 = [s1_t1, s2_t1]

def test_is_open_sea1(): 
    assert is_open_sea(5,8,f_t1) == False #Test to check illegal top right diagonal placement

    
def test_ok_to_place_ship_at1():
    assert ok_to_place_ship_at(5,7, True, 2, f_t1) == False #Test to check adjacent illegal placement

def test_place_ship_at1():
    actual = place_ship_at(5,6, True, 2, f_t1)
    actual.sort() #Sort required to use == safely
    expected = [s1_t1, s2_t1, (5,6, True, 2, set())]
    expected.sort()
    assert expected == actual

f1 = [(3, 2, True, 4, set()), (9, 2, True, 3, {(9,2), (9,4)}), (5, 3, True, 3, set()), (8, 7, True, 2, set()), (0, 6, True, 2, set()), (5, 1, False, 2, set()), \
        (1, 0, False, 1, set()), (1, 2, True, 1, set()), (7, 3, True, 1, set()), (7, 5, False, 1, set())]

    
def test_check_if_hits1():
    assert check_if_hits(9,4,f1) == True #check for hit

def test_check_if_not_already_hit1():
    assert check_if_not_already_hit(6,7,K) == False #check if its not already hit


def test_hit1():
    (actual,s) = hit(9,3,f1)
    actual.sort()
    expected = [(3, 2, True, 4, set()), (9, 2, True, 3, {(9,2), (9,3), (9,4)}), (5, 3, True, 3, set()), (8, 7, True, 2, set()), (0, 6, True, 2, set()), (5, 1, False, 2, set()), \
        (1, 0, False, 1, set()), (1, 2, True, 1, set()), (7, 3, True, 1, set()), (7, 5, False, 1, set())] 
    expected.sort()
    assert (actual, s) == (expected, (9, 2, True, 3, {(9,2), (9,3), (9,4)}))

def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left(f1)==True



#Test Case 2
s2 = (1, 2, True, 4, {(1,2), (1,3), (1,4), (1,5)}) 

def test_is_sunk2():
    assert is_sunk(s2) == True
    
def test_ship_type2():
    assert ship_type(s2) == "battleship"

s1_t2 = (2, 3, False, 3, set())
s2_t2 = (6, 1, False, 2, set())
f_t2 = [s1_t2, s2_t2]

def test_is_open_sea2(): 
    assert is_open_sea(3,2,f_t2) == False #Test to check illegal left side placement

def test_ok_to_place_ship_at2():
    assert ok_to_place_ship_at(3,1, True, 4, f_t2) == False #Test to check if a new ship will overlap with existing (illegal placement)

def test_place_ship_at2():
    actual = place_ship_at(0,5, True, 3, f_t2)
    actual.sort() #Sort required to use == safely
    expected = [s1_t2, s2_t2, (0,5, True, 3, set())]
    expected.sort()
    assert expected == actual

f2 = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]

    
def test_check_if_hits2():
    assert check_if_hits(6,6,f2) == False #check for miss

def test_hit2():
    (actual,s) = hit(2,4,f2)
    actual.sort()
    expected = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, {(2,4)}), (0, 6, False, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (2, 4, False, 1, {(2,4)}))

f2_1 = [(6, 2, True, 4, {(6,2), (6,3), (6,5),(6,4)}), (5, 9, False, 3, {(5,9),(6,9),(7,9)}), (4, 5, True, 3, {(4,5),(4,6),(4,7)}), (8, 1, True, 2,{(8,1),(8,2)}), (2, 9, False, 2, {(2,9), (3,9)}), (8, 5, True, 2, {(8,5), (8,6)}), \
        (1, 2, False, 1, {(1,2)}), (6, 7, True, 1, {(6,7)}), (2, 4, False, 1, {(2,4)}), (0, 6, False, 1, {(0,6)})]

def test_are_unsunk_ships_left2():
    assert are_unsunk_ships_left(f2_1)==False #Checks and returns that all the ships have been sunk

def test_check_if_not_already_hit2():
    assert check_if_not_already_hit(7,9,K) == True #check if its not already hit


#Test Case 3
s3 = (7, 3, False, 2, {(7,3)}) 
#we use global variables if certain ships or fleets are used in multiple test functions

def test_is_sunk3():
    assert is_sunk(s3) == False
    
def test_ship_type3():
    assert ship_type(s3) == "destroyer"

s1_t3 = (2, 3, False, 3, set())
s2_t3 = (6, 9, False, 4, set())
f_t3 = [s1_t3, s2_t3]

def test_is_open_sea3(): 
    assert is_open_sea(5,3,f_t3) == False #Test to check illegal bottom placement

def test_ok_to_place_ship_at3():
    assert ok_to_place_ship_at(3,9, True, 2, f_t3) == False #Test to check if new ship can be placed outside the allowed column grid 9<

def test_place_ship_at3():
    actual = place_ship_at(0,0, True, 1, f_t3)
    actual.sort() #Sort required to use == safely
    expected = [s1_t3, s2_t3, (0,0, True, 1, set())]
    expected.sort()
    assert expected == actual

f3 = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, {(8,2)}), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]

def test_check_if_hits3():
    assert check_if_hits(3,9,f3) == True 

def test_hit3():
    (actual,s) = hit(8,1,f3)
    actual.sort()
    expected = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, {(8,1), (8,2)}), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (8, 1, True, 2, {(8,1), (8,2)}))

f3_1 = [(6, 2, True, 4, {(6,2), (6,3),(6,4)}), (5, 9, False, 3, {(5,9),(6,9),(7,9)}), (4, 5, True, 3, {(4,5),(4,6),(4,7)}), (8, 1, True, 2,{(8,1),(8,2)}), (2, 9, False, 2, {(2,9), (3,9)}), (8, 5, True, 2, {(8,5), (8,6)}), \
        (1, 2, False, 1, {(1,2)}), (6, 7, True, 1, {(6,7)}), (2, 4, False, 1, set()), (0, 6, False, 1, {(0,6)})]

def test_are_unsunk_ships_left3():
    assert are_unsunk_ships_left(f3_1)==True #2 shot remaining for all sunk

def test_check_if_not_already_hit3():
    assert check_if_not_already_hit(5,9,K) == False #check if its not already hit

#Test case 4

s4 = (2, 3, True, 1, set()) 
#we use global variables if certain ships or fleets are used in multiple test functions

def test_is_sunk4():
    assert is_sunk(s4) == False
    
def test_ship_type4():
    assert ship_type(s4) == "submarine"

s1_t4 = (2, 2, False, 3, set())
s2_t4 = (5, 6, False, 4, set())
f_t4 = [s1_t4, s2_t4]
f_t4_1 = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set())]

def test_is_open_sea4(): 
    assert is_open_sea(4,2,f_t4) == False #Test to check illegal overlap placement

def test_ok_to_place_ship_at4():
    assert ok_to_place_ship_at(2,4, False, 1, f_t4_1) == True #Test to check if a new ship can be placed after placement of 8 other ships.

def test_place_ship_at4():
    actual = place_ship_at(0,9, False, 1, f_t4)
    actual.sort() #Sort required to use == safely
    expected = [s1_t4, s2_t4, (0,9, False, 1, set())]
    expected.sort()
    assert expected == actual


f4 = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]


def test_check_if_hits4():
    assert check_if_hits(1,2,f4) == True

def test_check_if_hits4():
    (actual,s) = hit(0,6,f4)
    actual.sort()
    expected = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, {(0,6)})]
    expected.sort()
    assert (actual, s) == (expected, (0, 6, False, 1, {(0,6)}))

f4_1 = [(6, 2, True, 4, {(6,2), (6,3), (6,5),(6,4)}), (5, 9, False, 3, {(5,9),(6,9)}), (4, 5, True, 3, {(4,5),(4,6),(4,7)}), (8, 1, True, 2,{(8,1),(8,2)}), (2, 9, False, 2, {(2,9), (3,9)}), (8, 5, True, 2, {(8,5), (8,6)}), \
        (1, 2, False, 1, {(1,2)}), (6, 7, True, 1, {(6,7)}), (2, 4, False, 1, {(2,4)}), (0, 6, False, 1, {(0,6)})]

def test_are_unsunk_ships_left4():
    assert are_unsunk_ships_left(f4_1)==True #Test for One shot remaining for all sunk --Cruiser only has been shot twice

def test_check_if_not_already_hit4():
    assert check_if_not_already_hit(6,3,K) == True #check if its not already hit

#Test case 5

s5 = (2, 0, True, 4, {(2,0), (2,1), (2,2), (2,3)}) 
#we use global variables if certain ships or fleets are used in multiple test functions

def test_is_sunk5():
    assert is_sunk(s5) == True
    
def test_ship_type5():
    assert ship_type(s5) == "battleship"

s1_t5 = (2, 3, False, 3, set())
s2_t5 = (6, 9, False, 4, set())
f_t5 = [s1_t5, s2_t5]

def test_is_open_sea5(): 
    assert is_open_sea(5,4,f_t5) == False #Test to check illegal bottom left diagonal placement

def test_ok_to_place_ship_at5():
    assert ok_to_place_ship_at(9,3, False, 2, f_t5) == False #Test to check if new ship can be placed outside the allowed row grid 9<

def test_place_ship_at5():
    actual = place_ship_at(9,0, True, 2, f_t5)
    actual.sort() #Sort required to use == safely
    expected = [s1_t5, s2_t5, (9,0, True, 2, set())]
    expected.sort()
    assert expected == actual
    
f5 = [(6, 2, True, 4, {(6,2), (6,3), (6,5)}), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]


def test_check_if_hits5():
    assert check_if_hits(0,1,f5) == False

def test_check_if_hits5():
    (actual,s) = hit(6,4,f5)
    actual.sort()
    expected = [(6, 2, True, 4, {(6,2), (6,3), (6,4), (6,5)}), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (6, 2, True, 4, {(6,2), (6,3), (6,4), (6,5)}))    

f5_1 = [(6, 2, True, 4, set()), (5, 9, False, 3, {(5,9),(6,9),(7,9)}), (4, 5, True, 3, {(4,5),(4,6),(4,7)}), (8, 1, True, 2,{(8,1),(8,2)}), (2, 9, False, 2, {(2,9), (3,9)}), (8, 5, True, 2, {(8,5), (8,6)}), \
        (1, 2, False, 1, {(1,2)}), (6, 7, True, 1, {(6,7)}), (2, 4, False, 1, {(2,4)}), (0, 6, False, 1, {(0,6)})]

def test_are_unsunk_ships_left5():
    assert are_unsunk_ships_left(f5_1)==True

def test_check_if_not_already_hit5():
    assert check_if_not_already_hit(8,2,K) == False #check if its not already hit