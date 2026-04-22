# Рекурсивная функция
def find_rec(data, x):
    pos = 0
    for item in data:
        if item == x:
            return pos
        if type(item) == list:
            res = find_rec(item, x)
            if res is not None:
                return pos + res
        pos = pos + 1
    return None

# Нерекурсивная функция 
def find_norec(data, x):
    stack = [(data, 0)]  
    current_list, current_pos = stack.pop()
    i = 0
    
    while True:
        if i >= len(current_list):
            if not stack:
                return None
            current_list, current_pos = stack.pop()
            i = 0
            continue
        
        item = current_list[i]
        
        if item == x:
            return current_pos + i
        
        if type(item) == list:
            stack.append((current_list, current_pos + i + 1))
            current_list = item
            current_pos = current_pos + i
            i = 0
        else:
            i += 1