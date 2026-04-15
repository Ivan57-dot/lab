from abc import ABC, abstractmethod


class ClothingItem(ABC):
    
    def __init__(self, size):
        self.size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value < 44 or value > 60:
            raise ValueError("Размер от 44 до 60")
        self._size = value
    
    @abstractmethod
    def fabric(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.size}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.size})"


class Jacket(ClothingItem):
    
    def fabric(self):
        return round(1.8 + self.size * 0.04, 2)
    
    def cost(self):
        return round(self.fabric() * 2000 + 500, 2)
    
    def __eq__(self, other):
        return isinstance(other, Jacket) and self.size == other.size
    
    def __hash__(self):
        return hash(self.size)


class Trousers(ClothingItem):
    
    def fabric(self):
        return round(1.0 + self.size * 0.025, 2)
    
    def cost(self):
        return round(self.fabric() * 2000 + 300, 2)
    
    def __lt__(self, other):
        return isinstance(other, Trousers) and self.size < other.size
    
    def __hash__(self):
        return hash(self.size)


class ThreePieceSuit(ClothingItem):
    
    def fabric(self):
        j = Jacket(self.size)
        t = Trousers(self.size)
        return round(j.fabric() + t.fabric() + 0.6, 2)
    
    def cost(self):
        j = Jacket(self.size)
        t = Trousers(self.size)
        return round(j.cost() + t.cost() + 800, 2)
    
    def __len__(self):
        return 3
    
    def __contains__(self, item):
        return item in ["пиджак", "брюки", "жилет"]