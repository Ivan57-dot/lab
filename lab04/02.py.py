def validate(arg1):
    def decorator(f):
        def proverka(arg):
            if arg == "стоп":
                return f(arg)
            if not arg1(arg):
                print(f"Ошибка: аргумент {arg} неправильный")
                return None
            return f(arg)
        return proverka
    return decorator

def make_zamikanie():
    items = []

    @validate(lambda x: isinstance(x, (int, str)) and not isinstance(x, bool))
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