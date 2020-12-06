import pytest
from battleships import *

#new commit 06122020
def test_is_sunk1():
    s = "A"
    assert is_sunk(s) == True
    

def test_ship_type1():
    s = "A"
    assert ship_type(s) == True

def test_is_open_sea1():
    assert is_open_sea(3, 4, "A") == True

def test_ok_to_place_ship_at1():
    assert ok_to_place_ship_at(3, 4, 6, 3, "B") == True

def test_place_ship_at1():
    assert place_ship_at(3, 4, 6, 3, "B") == True

def test_check_if_hits1():
    assert check_if_hits(3, 4, "A") == True

def test_hit1():
    assert hit(3, 4, "A") == True

def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left("A") == True
    
