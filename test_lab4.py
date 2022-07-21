import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    
    def subtract(self, a,b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

@pytest.fixture

def base_calculator():
    return Calculator("Base Calculator")
    
def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    #change calcu's name
    base_calculator.name = "Changed calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True
    
def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True

def test_subtract(base_calculator):
    assert base_calculator.subtract(2, 1) == 1
    assert base_calculator.subtract(5, 3) == 2
    assert base_calculator.subtract(-10.5, 1.5) == -12 
    
    print(base_calculator.subtract(2, 1))
    print(base_calculator.subtract(5, 3))
    print(base_calculator.subtract(-10.5, 1.5))
    
def test_multiply(base_calculator):
    assert base_calculator.multiply(-22, -10) == 220
    assert base_calculator.multiply(5.5, 310.72) == 1708.96
    assert base_calculator.multiply(10, 10) == 100
    
    print(base_calculator.multiply(-22, -10))
    print(base_calculator.multiply(5.5, 310.72))
    print(base_calculator.multiply(10, 10))
    
    








#calc = Calculator("Calc 1")

#def test_lab4():
    #print("This calculator's name is " + calc.name)
    
    # Change the calculator's name
    #calc.name = "Calc 2"
    #print("This calculator's name is " + calc.name)

    #print(calc.add(1, 1))
    
    #assert True

