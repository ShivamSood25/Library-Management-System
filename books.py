import sqlite3

class Books:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            t TEXT,
            a TEXT,
            l TEXT,
            p INTEGER,
            n INTEGER,
            b TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, t, a, l, p, n, b):
        self.cur.execute('INSERT INTO books (t, a, l, p, n, b) VALUES (?, ?, ?, ?, ?, ?)', (t, a, l, p, n, b))
        self.con.commit()

    def update(self, id, t, a, l, p, n, b):
        self.cur.execute('UPDATE books SET t=?, a=?, l=?, p=?, n=?, b=? WHERE id=?', (t, a, l, p, n, b, id))
        self.con.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM books')
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute('DELETE FROM books WHERE id=?', (id,))
        self.con.commit()

    def select(self, a):
        self.cur.execute('SELECT * FROM books WHERE a=?', (a,))
        rows = self.cur.fetchall()
        return rows
    
    def selectA(self, l=0):
        self.cur.execute('SELECT * FROM books WHERE l=?', (l,))
        rows = self.cur.fetchall()
        return rows

    def select2(self, a,l):
        self.cur.execute('SELECT * FROM books WHERE a=? and l=?', (a,l))
        rows = self.cur.fetchall()
        return rows
    def showbookid(self):
        self.cur.execute('SELECT id FROM books')
        rows = self.cur.fetchall()
        return rows
    def showdata(self, t):
        name_pattern = t + '%'
        self.cur.execute('SELECT * FROM books WHERE t LIKE ?', (name_pattern,))
        rows = self.cur.fetchall()
        return rows
    def fetch_unique_authors(self):
        self.cur.execute('SELECT DISTINCT a FROM books')
        rows = self.cur.fetchall()
        return [row[0] for row in rows]

    def fetch_unique_languages(self):
        self.cur.execute('SELECT DISTINCT l FROM books')
        rows = self.cur.fetchall()
        return [row[0] for row in rows]
