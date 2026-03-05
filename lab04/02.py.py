def validate(arg1):
    def decorator(func):
        def wrapper(arg):
            if not condition(arg):
                print("Ошибка: аргумент неправильный")
                return None
            return func(arg)
        return wrapper
    return decorator

def make_zamikanie():
    items = []
    
    @validate(lambda x: (isinstance(x, int) and not isinstance(x, bool)) or isinstance(x, str) or x == "стоп")
    def zamikanie(x):
        if x == "стоп":
            result = items.copy()
            items.clear()
            return result
        else:
            items.append(x)
            return None
    
    return zamikanie

c = make_zamikanie()
c(1)              
c("hello")       
c([1, 2, 3])      
c(True)           
c(3.14)          
c(None)   

print(c("стоп")) 
