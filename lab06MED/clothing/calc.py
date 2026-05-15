from .models import Jacket, Trousers, ThreePieceSuit
def calculate(chto, razmer):
    if chto == "Пиджак":
        obj = Jacket(razmer)
    elif chto == "Брюки":
        obj = Trousers(razmer)
    elif chto == "Костюм-тройка":
        obj = ThreePieceSuit(razmer)
    fabric = obj.get_fabric()
    cost = obj.get_cost()
    return round(fabric, 2), round(cost, 2)