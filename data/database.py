import sqlite3
from dataclasses import dataclass

class Database:

    def __init__(self, file):
        self.conn = sqlite3.connect(file + '.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT DEFAULT NULL, content TEXT NOT NULL);')

    def add(self, note):
        self.conn.execute("INSERT INTO note (title, content) VALUES (%s, %s);" % ("'{}'".format(note.title) if note.title else "''", "'{}'".format(note.content)))
        self.conn.commit()

    def get_all(self):
        notes = []
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            notes.append(Note(id, title, content))
        return notes

    def update(self, entry):
        self.conn.execute("UPDATE note SET title = %s, content = '%s' WHERE id = '%s'" % ("'{}'".format(entry.title) if entry.title else "NULL", entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = %s" % (note_id))
        self.conn.commit()

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''



# k = Note(5, content='asdf')
# print("INSERT INTO note (title, content) VALUES (%s, %s);" % ("'{}'".format(k.title) if k.title else "'NULL'", "'{}'".format(k.content)))
