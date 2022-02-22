from unittest.mock import Mock
from carte_pizzeria import CartePizzeria
from mock import patch, PropertyMock

#test qui pète 1 
def test_carte_pizza_is_not_empty():
    c = CartePizzeria()
    pizza = Mock()
    c.carte = [pizza]
    assert c.is_empty()
    
#test qui marche 1
def test_carte_pizza_is_empty():
    c = CartePizzeria()
    c.carte = []
    assert c.is_empty()

#test qui marche 2
def test_carte_pizza_len_0():
    c = CartePizzeria()
    c.carte = []
    assert c.nb_pizzas() == 0
    
#test qui pète 2
def test_carte_pizza_len_not_0():
    c = CartePizzeria()
    pizza = Mock()
    c.carte = [pizza]
    assert c.nb_pizzas() == 0

#test qui marche 3
def test_carte_pizza_add_pizza_success():
    c = CartePizzeria()
    pizza = Mock()
    c.carte = []
    c.add_pizza(pizza) 
    assert c.carte == [pizza]
