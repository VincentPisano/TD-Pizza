class CartePizzeria:
    #pizzas = [] pizza prend la valeur par défaut [] si pizza n'est pas passer comme argument
    def __init__(self, pizzas = []):
        self.__carte = pizzas
        pass
    
    def is_empty(self):
        return len(self.__carte) ==0
        
    def nb_pizzas(self):
        return len(self.__carte)
        
    def add_pizza(self, pizza):
        self.__carte.append(pizza)
            
    
    def remove_pizza(self, name):
        try : 
            self.carte.remove(name) 
        except  ValueError : 
              CartePizzeriaExeption("La pizza que vous souhaitez enlever de la carte n'existe pas !")
              
              
class CartePizzeriaExeption(Exception):
    pass