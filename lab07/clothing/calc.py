from .models import Jacket, Trousers, ThreePieceSuit


class Calculator:
    
    items = {
        "Пиджак": Jacket,
        "Брюки": Trousers,
        "Костюм-тройка": ThreePieceSuit
    }
    
    def __init__(self):
        self.result = None
    
    def calc(self, name, size):
        obj = self.items[name](size)
        f = obj.fabric()
        c = obj.cost()
        self.result = (name, size, f, c, obj)
        return f, c
    
    def __call__(self, name, size):
        return self.calc(name, size)
    
    def __len__(self):
        return len(self.items)