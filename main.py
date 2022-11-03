import student_info as si
import cabinet_info as cab
import sys


def option():
    print('\nДобро пожаловать!')
    ch = int(input('Введите действие: \n \
    1: Поиск ID ученика по фамилии \n \
    2: Посмотреть класс и место, которое занимает ученик \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        surname = str(input('Введите фамилию ученика: '))
        if surname in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(surname)
        print(f'ID - {si.stud_card["ID"][index]}, {si.stud_card["Имя"][index]} {si.stud_card["Фамилия"][index]}\nдата рождения - {si.stud_card["Дата рождения"][index]}\nуспеваемость - {si.stud_card["Успеваемость"][index]}')
        print('\nПланируете повторить поиск? Y или N: ')
        num = input()
        if num == 'Y' or 'y':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID ученика: ')
        if c in cab.cabinet_card['ID']:
            index = cab.cabinet_card['ID'].index(c)
            print(f' Сидит в классе - {cab.cabinet_card["Предмет"][index]}\n\, за партой номер - {cab.cabinet_card["Номер парты"][index]}, это {cab.cabinet_card["Ряд"][index]}, парта - {cab.cabinet_card["Вид парты"][index]}, Имя: {si.stud_card["Имя"][index]}, Фамилия - {si.stud_card["Фамилия"][index]}, успеваемость ученика: {si.stud_card["Успеваемость"][index]}')
            print('\nПланируете повторить поиск? Y или N: ')
            num = input()
            if num == 'Y' or 'y':
                option()
            exit()
    elif ch == 3:
        print('-'*5, 'До скорых встреч!', '-'*5)
        sys.exit()
    else:
        print('повторите попытку')
    exit()

option()