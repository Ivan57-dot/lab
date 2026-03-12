import os

def find_files(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                yield os.path.join(root, file)
                count += 1
                if count >= 3:
                    return

files = list(find_files('.'))
print("Найдено:", [os.path.basename(f) for f in files])

big_files = list(filter(lambda f: os.path.getsize(f) > 100, files))
print("Большие (>100 байт):", [os.path.basename(f) for f in big_files])

sizes = list(map(os.path.getsize, files))  

for i, f in enumerate(files, 1):
    os.rename(f, os.path.join(os.path.dirname(f), f"file_{i}.txt"))
print("Переименовано")
