# **ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ №7 ВАРИАНТА 10**

## **Задача:** 
Откорректировать код для работы #7 с учетом дополнительных требований.

## **Ход работы:**
1. Реализованы:
     - Абстрактный класс - ClothingItem(ABC);
     - Абстрактные методы - @abstractmethod для fabric() и cost();
     - Наследование - Jacket, Trousers, ThreePieceSuit наследуют ClothingItem;
     - Managed-фтрибут - @prtopery size + @size.setter с проверкой диапозона 44-60;
     - Dunder-методы - __str__, __repr__, __eq__, и другие.
2. Графический интерфейс переделан с помощью PySimpleGUI

## **Результат:** 
<img width="245" height="195" alt="image" src="https://github.com/user-attachments/assets/4d4bff24-2792-43b9-afa9-73028009c480" />


## **Используемые материалы:**
[abc](https://docs.python.org/3/library/abc.html)

[PySimpleGUI](https://docs.pysimplegui.com/en/latest/)
