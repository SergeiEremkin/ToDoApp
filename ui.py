import keyboard
import classNote
import checks

def createNote():
    note = editNote()   
    return classNote.Note(title = note[0], body = note[1])


def editNote():
    title = ''
    body = ''
    while len(title)<=5:
        print('<Заголовок должен быть больше 5 символов>\n')
        title = input('Введите ЗАГОЛОВОК заметки: ')
    while len(body)<=5:
        print('<Заметка должен быть больше 5 символо>\n')
        body = input('\rВведите ОПИСАНИЕ заметки: ')
    return (title, body)


def menu():
    print('\n' * 50)
    print('Добро пожаловать в программу "Заметки"\n')
    print("\n1 - для вывода всех заметок\n2 - для добавления заметки\n3 - для удаления заметки\n4 - для редактирования заметки\n5 - для выборки по дате\n6 - показать элемент по id\n7 - для выхода\n")


def continueWork():
    print('Нажмите пробел для продолжения...')
    keyboard.wait('space')