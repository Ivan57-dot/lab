def make_zamikanie():
    items = []
    def zamikanie(x):
        if x == "стоп":
            result = items.copy()
            items.clear()
            return result
        else:
            items.append(x)
    
    return zamikanie

c = make_zamikanie()
c(1)
c(2)
c(3)
print(c("стоп"))
c(4)
c(5)

print(c("стоп"))
