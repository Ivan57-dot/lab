# Простой декоратор с опциональным параметром
def decorator(prefix=""):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(prefix + "Вызов", func.__name__)
            result = func(*args, **kwargs)
            print(prefix + "Результат:", result)
            return result
        return inner
    return wrapper

# Ваша функция с замыканием
@decorator(">>> ")
def make_zamikanie():
    items = []
    
    @decorator("     ")
    def zamikanie(x):
        if x == "стоп":
            result = items.copy()
            items.clear()
            return result
        else:
            items.append(x)
    
    return zamikanie

# Проверка
c = make_zamikanie()
c(1)
c(2)
c(3)
print(c("стоп"))
c(4)
c(5)
print(c("стоп"))