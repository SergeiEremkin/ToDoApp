from datetime import datetime
import uuid


class Note:
    def __init__(self, title, body):
        self.id = uuid.uuid1()
        self.title = title
        self.body = body
        self.date = datetime.now()

    def toString(note):
        return str(note.id) +','+ note.title + ',' + note.body + ',' + str(note.date)
        


