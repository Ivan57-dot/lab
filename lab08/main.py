from abc import ABC, abstractmethod
from .exceptions import GameOver

class GameObject(ABC):
    def __init__(self, x, y): 
        self.x, self.y = x, y
        self._alive = True  # managed attribute для демонстрации
    
    @property
    def alive(self):
        return self._alive
    
    @alive.setter
    def alive(self, value):
        self._alive = value
    
    @abstractmethod
    def update(self, *args, **kwargs): 
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
    
    @property
    def head(self): 
        return self.body[0]
    
    def move(self, grow):
        self.body.insert(0, (self.head[0]+self.dx, self.head[1]+self.dy))
        if not grow: 
            self.body.pop()
    
    def change_dir(self, dx, dy):
        if (dx,dy) != (-self.dx,-self.dy): 
            self.dx, self.dy = dx, dy
    
    def check(self):
        if self.head in self.body[1:] or not (0<=self.head[0]<20 and 0<=self.head[1]<20):
            raise GameOver()
    
    def update(self, grow=False):
        """ПОЛИМОРФИЗМ: змейка двигается и проверяет столкновения"""
        old_head = self.head
        self.move(grow)
        print(f"🐍 Змейка: голова была {old_head}, стала {self.head}")  # Демонстрация
        return self.head
    
    def __len__(self): 
        return len(self.body)
    
    def __contains__(self, p): 
        return p in self.body

class Food(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._nutrition = 1  # питательность
    
    @property
    def nutrition(self):
        return self._nutrition
    
    @nutrition.setter
    def nutrition(self, value):
        self._nutrition = value if value > 0 else 1
    
    def update(self):
        """ПОЛИМОРФИЗМ: еда обновляет свою ценность (например, становится вкуснее)"""
        self.nutrition += 0.1  # каждое обновление еда становится чуть ценнее
        print(f"🍎 Еда: питательность увеличилась до {self.nutrition:.1f}")  # Демонстрация
        return self.nutrition
    
    def __repr__(self): 
        return f"🍎({self.x},{self.y}) nutr={self.nutrition:.1f}"
    
    def __add__(self, n): 
        return int(n + self.nutrition)