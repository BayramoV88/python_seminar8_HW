from read_data import get_data
from cabinet_info import cabinet_card
import pandas as pd
import sys


def stud_log():
   while True:
        print('')
        print('1 - Просмотреть информацию по учебному классу')
        print('9 - Выход')
        choise = input('Введите команду: ')
        if choise == '1':
            c = input('Введите свой ID: ')
            if c in cabinet_card['ID']:
                index = cabinet_card['ID'].index(c)
                print('-'*30)
                print(f'номер варианта - {cabinet_card["Вариант"][index]}, это {cabinet_card["Ряд"][index]}, парта - {cabinet_card["Вид парты"][index]}')
        if choise == '9':
            sys.exit('До скорых встреч!')