from random import randint


class Budget:
    def __init__(self, categories: str, innitial_balance: float) -> None:   #constructor de la clase
        self.categories = categories  #guargar categories dentro de la clase misma
        self.innitial_balance = innitial_balance
        self.running_balance = innitial_balance #no se define en el constructor porque es un dato calculado
    """
    Arriba se encuentra el constructor de la clase. Los argumentos que estan 
    en el constructor es por que butget no pueden existir sin budget
    """
    def get_running_balance(self) -> float:    #un getter en python. metodos
        return self.run
        pass

    def withdraw(self, amount: float) -> None:      #metodos
        self.running_balance = self.running_balance - amount
        pass

    def deposit(self, amount: float) -> None:   #metodos
        self.running_balance = self.running_balance + amount
        pass
"""
    Acabamos de  crear los metodos de la clase Butget  impementarlos
"""
class User:
    
    def __init__(self, name: str, total_budget: float) -> None:
        self.name = name
        self.total_budget = total_budget
        self.id = randint(1,1000)
        budgets = {}  #diccionario
        pass
    
    def add_budget(self, categories: str, innitial_balance: float) -> None:
        budget = Budget(categories = categories, innitial_balance=innitial_balance) #creando la bolcita chiquita
        self.budget.update({categories: budget}) #bolsa grande. estoy cogiendo la bolcita pequeña y metiendolo en la bolsa grnade

    def transfer_budget(self, amout: float, sender: str, receiver: str) -> None:
        pass