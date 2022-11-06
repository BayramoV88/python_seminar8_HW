import student_info as si
import cabinet_info as cab
import sys


def option():
    print('\nДобро пожаловать!')
    ch = int(input('Введите действие: \n \
    1: Поиск ID ученика по фамилии \n \
    2: Посмотреть класс и место, которое занимает ученик \n \
    9: Выход\n \
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
            print('-'*30)
            print(f'ученик: {si.stud_card["Имя"][index]} {si.stud_card["Фамилия"][index]}')
            print(f'сидит в классе - {cab.cabinet_card["Предмет"][index]}\nномер варианта - {cab.cabinet_card["Вариант"][index]}, это {cab.cabinet_card["Ряд"][index]}, парта - {cab.cabinet_card["Вид парты"][index]}, успеваемость ученика: {si.stud_card["Успеваемость"][index]}')
            print('\nПланируете повторить поиск? Y или N: ')
            num = input()
            if num == 'Y' or 'y':
                option()
            exit()
    elif ch == 9:
        print('-'*5, 'До скорых встреч!', '-'*5)
        sys.exit()
    else:
        print('повторите попытку')
    exit()

#option()