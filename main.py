from menu import menu
import sys
from stud_log import stud_log
from teach_log import teach_log

print('')
choice = menu()
while choice in ('1', '2', '9'):
    #choice = menu()
    if choice == '1':
        stud_log()
    elif choice == '2':
        teach_log()
    elif choice == '9':
        sys.exit('До скорых встреч!')