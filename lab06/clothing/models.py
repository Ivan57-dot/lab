class Jacket:
    def __init__(self, razmer):
        self.razmer = razmer
    def get_fabric(self):
        return 1.8 + self.razmer * 0.04 
    def get_cost(self):
        return self.get_fabric() * 2000 + 500
class Trousers:
    def __init__(self, razmer):
        self.razmer = razmer
    def get_fabric(self):
        return 1.0 + self.razmer * 0.025
    def get_cost(self):
        return self.get_fabric() * 2000 + 300
class ThreePieceSuit:
    def __init__(self, razmer):
        self.razmer = razmer
    def get_fabric(self):
        p = Jacket(self.razmer)
        b = Trousers(self.razmer)
        return p.get_fabric() + b.get_fabric() + 0.6
    def get_cost(self):
        p = Jacket(self.razmer)
        b = Trousers(self.razmer)
        return p.get_cost() + b.get_cost() + 800