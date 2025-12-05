from app import greet, add, mul, gif

def test_greet():
    assert greet("Bob") == "Hi! Bob" 

def test_add():
    assert add (2, 3) == 5

def test_mul():
    assert mul(2, 5) == 10    
def test_gif():
    assert gif(10, 5) == 2          