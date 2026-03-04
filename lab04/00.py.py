def make_collector():
    items = []
    def collector(x):
        if x == "стоп":
            result = items.copy()
            items.clear()
            return result
        else:
            items.append(x)
    
    return collector

c = make_collector()
c(1)
c(2)
c(3)
print(c("стоп"))
c(4)
c(5)
print(c("стоп"))