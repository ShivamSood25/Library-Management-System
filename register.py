import sqlite3
class MEMBERS:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            f TEXT,
            l TEXT,
            fees TEXT default 0,
            a TEXT,
            p TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, f, l, a, p):
        self.cur.execute('INSERT INTO members (f, l,fees, p, a) VALUES (?, ?,0, ?, ?)', (f, l, p, a))
        self.con.commit()

    def update(self,id, f, l, a, p):
        self.cur.execute('UPDATE members SET f=?, l=?, p=?, a=? WHERE id=?', (f, l, p, a, id))
        self.con.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM members')
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute('DELETE FROM members WHERE id=?', (id,))
        self.con.commit()

    def showid(self):
        self.cur.execute('SELECT id FROM members')
        rows = self.cur.fetchall()
        return rows  

    def showmemid(self, id):
        id_pattern = id + '%'
        self.cur.execute('SELECT * FROM members WHERE id LIKE ?', (id_pattern,))
        rows = self.cur.fetchall()
        return rows  
    
    def update_fine(self, mem_id, fine):
        self.cur.execute('SELECT fine FROM members WHERE id=?', (mem_id,))
        current_fine = self.cur.fetchone()[0]

        total_fine = int(current_fine) + int(fine)
        self.cur.execute('UPDATE members SET fine=? WHERE id=?', (total_fine, mem_id))
        self.con.commit()
