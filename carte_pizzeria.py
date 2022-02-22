class CartePizzeria:
    
   
    
    def __init__():
        carte = []
        pass
    
    def is_empty(self):
        if len(self.carte) == 0:
            return True
        return False 
        
    
    def nb_pizzas(self):
        return len(self.carte)
        
    def add_pizza(self, pizza):
        self.carte.append(pizza)
            
    
    def remove_pizza(self, name):
        try : 
            self.carte.remove(name) 
        except  ValueError : 
              print("La pizza que vous souhaitez enlever de la carte n'existe pas !")