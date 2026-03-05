def validate(arg1, arg2):
    def decorator(f):
        def proverka(a, b):
            if not arg1(a):
                print("Ошибка: первый аргумент неправильный")
                return
            if not arg2(b):
                print("Ошибка: второй аргумент неправильный")
                return
            return f(a, b)
        return proverka
    return decorator

@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def test(x, y):
    print(x, y)

test(5, "привет")    
test(-1, "привет")  
test(5, 123)         


