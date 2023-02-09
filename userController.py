import logic
import ui
import checks



def start():
    userInput ='0'
    while userInput != '7':
        ui.menu() 
        userInput =input('Введите номер задачи: ')
        if userInput == '1':
           logic.show()
           ui.continueWork()
        if userInput == '2':
            note =ui.createNote()
            logic.add(note)
        if userInput == '3':
            logic.show()
            print("\n")
            logic.delete(input("Введите id заметки: "))
        if userInput == '4':
            logic.show()
            print("\n")
            userInput = input("Введите id заметки: ")
            if checks.checkInList(userInput):
                editNote = ui.editNote()
                logic.edit(userInput, editNote[0], editNote[1])
        if userInput == '5':
            logic.showByDate(input('Введите дату в формате dd.mm.yyyy: '))
        if userInput == '6':
            logic.show()
            print("\n")
            logic.showById(input("Введите id заметки: "))
        if userInput == '7':
            break
        