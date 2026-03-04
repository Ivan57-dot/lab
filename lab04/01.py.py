def validate(condition1, condition2):
    def decorator(func):
        def wrapper(a, b):
            if not condition1(a):
                print("Ошибка: первый аргумент неправильный")
                return
            if not condition2(b):
                print("Ошибка: второй аргумент неправильный")
                return
            return func(a, b)
        return wrapper
    return decorator

@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def test(x, y):
    print(x, y)

test(5, "привет")    
test(-1, "привет")  
test(5, 123)         
