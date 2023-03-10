import os.path
import sys
import winreg

# Адрес текущей директории
pth = os.path.dirname(os.path.realpath(__file__))


# Ф-ия добавления файла master в реестр автозагрузки
def add_master_reg(key, name_reg, address):
    try:

        # Получения значения в реестре элемента с именем name_reg
        # если там нет такого ключа - добавим его,
        # если есть - ничего не меняем
        _ = winreg.QueryValueEx(key, name_reg)
    except:
        # Установить программу "master" в автозагрузку
        winreg.SetValueEx(key, name_reg, 0, winreg.REG_SZ, address)


# Ф-ия удаления файла master из реестра автозагрузки
def del_master_reg(key, name_reg):
    try:

        # Получения значения в реестре элемента с именем name_reg
        _ = winreg.QueryValueEx(key, name_reg)

        # Удалить программу "master" из автозагрузки
        winreg.DeleteValue(key, name_reg)
    except Exception as e:
        print("Произошла ошибка при удалении из автозагрузки - " + str(e))


# Ф-ия открытия ключа реестра
def open_key_reg(autoload):
    # Имя файла master, который нужно удалить из автозагрузки реестра
    name_file = "\master.py"

    # Имя в реестре программы автозапуска - master
    name_reg = "master"

    # Соединяет адрес Python.exe и исполняемого текущего файла
    address = f'{sys.executable} {(str(pth)) + name_file}'

    # Открытие ключа, прописываем путь в реестре до автозагрузки
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
        0,
        winreg.KEY_ALL_ACCESS
    )

    if autoload == 1:

        # Добавление мастера в автозагрузку
        add_master_reg(key, name_reg, address)
        print("Добавлен в автозагрузку")

    elif autoload == 0:

        # Удаление мастера из автозагрузки
        del_master_reg(key, name_reg)
        print("Удален из автозагрузки")

    # Закрыть реестр
    winreg.CloseKey(key)


# Основная ф-ия входа.
def index():
    autoload = 0

    try:
        autoload = int(input("Введите 0 или 1: 1-добавить в автозагрузку, 0-удалить: "))
    except:
        print("Введите число: 1-добавить в автозагрузку, 0-удалить")

    # Ф-ия открытия ключа реестра
    open_key_reg(autoload)


index()
