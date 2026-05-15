# **ХОД ВЫПОЛНЕНИЯ** 

## **1. Установка и запуск Docker Desktop**

## **2. Создание файла docker-compose.yml в корневой папке проекта**
<img width="308" height="233" alt="image" src="https://github.com/user-attachments/assets/cf9b32c1-2bfc-414b-af0d-598a86a1c13f" />

image: postgres:15 — используется официальный образ PostgreSQL версии 15

container_name — имя контейнера для удобного управления

POSTGRES_USER / PASSWORD — учётные данные для доступа к БД

POSTGRES_DB — имя базы данных, которая создастся автоматически

ports: "5432:5432" — проброс порта, чтобы приложение на Python могло подключиться к БД

## **3. Запуск PostgreSQL в Docker**
<img width="971" height="129" alt="image" src="https://github.com/user-attachments/assets/fcbb3ce4-77fb-406f-a3ae-c2597ee467da" />

## **3.1 Проверка работы контейнера**
<img width="972" height="90" alt="image" src="https://github.com/user-attachments/assets/a0517e2e-88f3-4a83-8c0c-8c640f9e05a9" />

## **4. Подключение к базе данных из терминала**
<img width="836" height="97" alt="image" src="https://github.com/user-attachments/assets/7ae9789b-0135-4746-9ba5-0a0d804664e7" />

## **5. Установка библиотеки psycopg2-binary**
<img width="696" height="28" alt="image" src="https://github.com/user-attachments/assets/8182751a-af93-4568-b903-ca9e3dae6830" />

## **6. Создание модуля clothing/db.py**
<img width="789" height="191" alt="image" src="https://github.com/user-attachments/assets/378df4fe-837d-4d7d-8d9c-6274b46ed037" />

Подключается к базе данных

Создаёт таблицу calc (если её нет)

Вставляет в неё данные о расчёте

## **7. Изменение main.py**
Импорт функции:

<img width="282" height="21" alt="image" src="https://github.com/user-attachments/assets/43bf2ec3-ff58-4135-ad59-6d1945322c5b" />

Вызов сохранения в функцию calc():

<img width="331" height="21" alt="image" src="https://github.com/user-attachments/assets/cb0b7462-b410-4168-b9fe-b552d1e47db7" />

## **8. Проверка работы**
<img width="629" height="327" alt="image" src="https://github.com/user-attachments/assets/f283434a-aa07-44f3-ad45-ab0292e26e49" />









