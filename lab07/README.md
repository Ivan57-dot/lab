# **ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ №7 ВАРИАНТА 10**

## **Задача:** 
Откорректировать код для работы #7 с учетом дополнительных требований.

## **Ход работы:**
1. Реализованы:
     - Абстрактный класс ClothingItem(ABC): запрещает создавать элемент "просто одежда";
     - Абстрактные методы @abstractmethod, который обязаны наследовать fabric() и cost();
     - Наследование - Jacket, Trousers, ThreePieceSuit наследуют ClothingItem;
     - Managed-атрибут - @properеy size + @size.setter с проверкой диапозона 44-60;
     - Dunder-методы.
            1. __str__: красивый вывод;
            2. __repr__: вывод для отладки;
            3. __eq__: сравнение пиджаков;
            4. __hash__: хэш для множеств/словарей;
            5. __len__: количество предметов;
            6. __contains__: проверка вхождения;
            7. __lt__: сравнение <.
2. Графический интерфейс переделан с помощью PySimpleGUI

## **Результат:** 
<img width="245" height="195" alt="image" src="https://github.com/user-attachments/assets/4d4bff24-2792-43b9-afa9-73028009c480" />


## **Используемые материалы:**
[абстрактные классы и методы](https://metanit.com/python/tutorial/7.8.php)

[PySimpleGUI](https://docs.pysimplegui.com/en/latest/)

[dunder-методы](https://timeweb.cloud/tutorials/python/dunder-metody-v-python)

[наследование](https://metanit.com/python/tutorial/7.3.php)
