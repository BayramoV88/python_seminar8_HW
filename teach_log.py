import sys
from teach_function import option

def teach_log():
    while True:
        print('1 - Просмотреть данные учеников')
        print('9 - Выход')
        choice = input("Введите команду: ")
        print('')
        if choice == '1':
            option()
        if choice == '9':
            sys.exit('До скорых встреч!')