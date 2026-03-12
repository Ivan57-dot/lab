import os

print("Текущая папка:", os.getcwd())  # показываем где мы
print("Содержимое папки:")
for item in os.listdir('.'):
    print(f"  {item}")

def find_files(path):
    count = 0
    for root, dirs, files in os.walk(path):
        print(f"\nПапка: {root}")
        print(f"Файлы тут: {files}")
        for file in files:
            if file.endswith('.txt'):
                print(f"  ✓ Найден .txt: {file}")
                yield os.path.join(root, file)
                count += 1
                if count >= 3:
                    return

files = list(find_files('.'))

if files:
    print(f"\nИтого найдено: {len(files)}")
else:
    print("\n❌ Файлы .txt не найдены!")