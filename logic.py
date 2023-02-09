import db
import classNote

def add(input):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:
        if classNote.Note.getId(input) == classNote.Note.getId(note):
                classNote.Note.setId(input)
    listOfNotes.append(input)
    db.writeTofileList(listOfNotes, 'a')
    print("Заметка добавлена")    
    
       

def show():
    try:
        listOfNotes = db.readFromFile()
        for note in listOfNotes:
            print(classNote.Note.forShow(note))
    except Exception:
        print ('\nНет ни одной задачи\n')

def showByDate(input):
    isEmpty = True
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
        if input in classNote.Note.getDate(note) :
            print(classNote.Note.forShow(note))
            isEmpty =False
    if isEmpty == True:
        print("Задач не найдено")


def showById(input):
    isEmpty = True
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
       if input == classNote.Note.getId(note):
            print(classNote.Note.forShow(note))
            isEmpty = False
    if isEmpty == True:
        print("Задач не найдено")


def delete(input):
    isDeleted = False
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
        if input == classNote.Note.getId(note) :
            isDeleted = True
            listOfNotes.remove(note)
            print("Заметка удалена")
    db.writeTofileList(listOfNotes, 'a')
    if isDeleted == False :
        print('Такой заметки нет. Возможно вы ввели неверный id')


def edit(input, newTitle, newBody):
    listOfNotes = db.readFromFile()
    for note in listOfNotes:  
        if input == classNote.Note.getId(note) :
            classNote.Note.setTitle(note,newTitle)
            classNote.Note.setBody(note, newBody)
            classNote.Note.setDate(note)
            print('Заметка изменена')
    db.writeTofileList(listOfNotes, 'a')
     