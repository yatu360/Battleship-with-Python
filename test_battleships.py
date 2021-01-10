import pytest
from battleships import *

s = (2, 3, False, 3, {(2,3), (3,3), (4,3)}) 
#we use global variables if certain ships or fleets are used in multiple test functions

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

f1 = [(3, 2, True, 4, set()), (9, 2, True, 3, set()), (5, 3, True, 3, set()), (8, 7, True, 2, set()), (0, 6, True, 2, set()), (5, 1, False, 2, set()), \
        (1, 0, False, 1, set()), (1, 2, True, 1, set()), (7, 3, True, 1, set()), (7, 5, False, 1, set())]

    
def test_check_if_hits1():
    assert check_if_hits(9,4,f1) == True #check for hit


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

f3 = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]


def test_check_if_hits3():
    assert check_if_hits(3,9,f3) == True 

s1_t4 = (2, 2, False, 3, set())
s2_t4 = (5, 6, False, 4, set())
f_t4 = [s1_t4, s2_t4]

def test_is_open_sea4(): 
    assert is_open_sea(4,2,f_t4) == False #Test to check illegal overlap placement

def test_ok_to_place_ship_at4():
    assert ok_to_place_ship_at(4,4, True, 3, f_t4) == False #Test to check if a new ship will occuply illegal i.e cell above existing ship

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

s1_t5 = (2, 3, False, 3, set())
s2_t5 = (6, 9, False, 4, set())
f_t5 = [s1_t5, s2_t5]

def test_is_open_sea5(): 
    assert is_open_sea(5,4,f_t5) == False #Test to check illegal bottom left diagonal placement

def test_ok_to_place_ship_at5():
    assert ok_to_place_ship_at(9,3, False, 2, f_t5) == False #Test to check if new ship can be placed outside the allowed row grid 9<

def test_ok_to_place_ship_at5():
    actual = place_ship_at(9,0, True, 2, f_t5)
    actual.sort() #Sort required to use == safely
    expected = [s1_t5, s2_t5, (9,0, True, 2, set())]
    expected.sort()
    assert expected == actual
    
f5 = [(6, 2, True, 4, set()), (5, 9, False, 3, set()), (4, 5, True, 3, set()), (8, 1, True, 2, set()), (2, 9, False, 2, set()), (8, 5, True, 2, set()), \
        (1, 2, False, 1, set()), (6, 7, True, 1, set()), (2, 4, False, 1, set()), (0, 6, False, 1, set())]


def test_check_if_hits5():
    assert check_if_hits(0,1,f5) == False

    

def test_hit1():
    (actual,s) = hit(5,1,f1)
    actual.sort()
    expected = [(1,1,True, 3, set()), (1,6, False, 2, set()), (2,9, False, 2, set()), (3,0,True, 1, set()), \
                  (3,2,True,3, set()), (5,1,True,2, {(5,2), (5,1)}), (5,4,True,1, set()), (5,7,True,1,set()), (6,9,False,4,set()), (9, 0, True, 1, set()) ] 
    expected.sort()
    assert (actual, s) == (expected, (5,1,True,2, {(5,2), (5,1)}))

def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left(f1)==True
