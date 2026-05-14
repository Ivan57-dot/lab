from abc import ABC, abstractmethod
from .exceptions import GameOver

class GameObject(ABC):
    def __init__(self, x, y): 
        self.x, self.y = x, y
    
    @abstractmethod
    def update(self): 
        pass
    
    def __str__(self): 
        return f"{self.__class__.__name__}({self.x},{self.y})"
    
    def __eq__(self, o): 
        return self.x == o.x and self.y == o.y

class Snake(GameObject):
    def __init__(self):
        super().__init__(10,10)
        self.body = [(10,10), (10,11), (10,12)]
        self.dx, self.dy = 0, -1
        self._grow_flag = False  # managed attribute
    
    @property
    def head(self): 
        return self.body[0]
    
    @property
    def grow_flag(self):
        return self._grow_flag
    
    @grow_flag.setter
    def grow_flag(self, value):
        self._grow_flag = value
    
    def move(self):
        self.body.insert(0, (self.head[0]+self.dx, self.head[1]+self.dy))
        if not self._grow_flag:
            self.body.pop()
        else:
            self._grow_flag = False
    
    def change_dir(self, dx, dy):
        if (dx,dy) != (-self.dx,-self.dy): 
            self.dx, self.dy = dx, dy
    
    def check(self):
        if self.head in self.body[1:] or not (0<=self.head[0]<20 and 0<=self.head[1]<20):
            raise GameOver()
    
    def update(self, grow=False):
        """ПОЛИМОРФИЗМ: змейка двигается"""
        self._grow_flag = grow
        self.move()
        self.check()
    
    def __len__(self): 
        return len(self.body)
    
    def __contains__(self, p): 
        return p in self.body

class Food(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._value = 1  # managed attribute
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, v):
        self._value = v if v > 0 else 1
    
    def update(self):
        """ПОЛИМОРФИЗМ: еда увеличивает свою ценность"""
        self._value += 0.1
    
    def __repr__(self): 
        return f"🍎({self.x},{self.y}) value={self._value:.1f}"
    
    def __add__(self, n): 
        return n + int(self._value)