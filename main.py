import work_data as wd
import os

if os.path.exists("settings.db") is False:
    print("ОШИБКА!!! Отсутствует файл со складами")
    exit()
if os.path.exists("input") is False:
    print("Отсутствует папка input")
    input("\nРабота программы окончена.Нажмите любую клавишу")
    exit()
list_files = wd.get_list_files()
if len(list_files) == 0:
    print("Отсутствуют файлы в папке input")
    input("\nРабота программы окончена.Нажмите любую клавишу")
    exit()
stores = wd.get_stores()
print("Обрабатываем файлы...")
list_stores_fact = wd.process(list_files, stores)
print("Проверяем склады!!!")
wd.check_avail_stores(list_stores_fact, stores)
input("\nРабота программы окончена.Нажмите любую клавишу")
