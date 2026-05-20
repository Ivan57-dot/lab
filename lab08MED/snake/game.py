import random
from .objects import Snake, Food
from .exceptions import GameOver

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = None
        self.score = 0
        self._spawn_food()
    
    def _spawn_food(self):
        while True:
            x, y = random.randint(0,19), random.randint(0,19)
            if (x,y) not in self.snake:
                self.food = Food(x,y)
                break
    
    def update(self):
        grow = self.snake.head == (self.food.x, self.food.y)
        self.snake.move(grow)
        self.snake.check()
        if grow:
            self.score += 1
            self._spawn_food()
    
    def change_dir(self, dx, dy): self.snake.change_dir(dx, dy)
    def __str__(self): return f"Score: {self.score}"
    def __len__(self): return len(self.snake)