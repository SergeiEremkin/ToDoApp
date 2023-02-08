import classNote

def writeTofile(note):
    f = open ("db.csv", 'a', encoding='utf-8')
    strNote = classNote.Note.toString(note)
    f.write(strNote)
    f.close

def readFromFile():
    f = open("db.csv", "r")
    f.read
    return notes    