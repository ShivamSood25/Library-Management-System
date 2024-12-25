import sqlite3
from datetime import datetime
from register import MEMBERS
class ISSUE_RET:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS Issue (
            Tid INTEGER PRIMARY KEY AUTOINCREMENT,
            doi TEXT,
            mem_id TEXT,
            book TEXT,
            dor TEXT,
            fine TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, doi, mem_id, book, dor, fine='0'):
        self.cur.execute('INSERT INTO Issue (doi, mem_id, book, dor, fine) VALUES (?, ?, ?, ?, ?)', (doi, mem_id, book, dor, fine))
        self.con.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM Issue')
        rows = self.cur.fetchall()
        return rows

    def remove(self, Tid):
        self.cur.execute('DELETE FROM Issue WHERE Tid=?', (Tid,))
        self.con.commit()
        
    def update(self, Tid, dor,fine):
        self.cur.execute('SELECT doi FROM Issue WHERE Tid=?', (Tid,))
        result = self.cur.fetchone()

        if result:
            doi = result[0]
            fine = self.calculate_fine(doi, dor)
            self.cur.execute('UPDATE Issue SET dor=?, fine=? WHERE Tid=?', (dor, fine, Tid))
            self.con.commit()
        else:
            print(f"No record found for Tid: {Tid}")

    def calculate_fine(self, doi, dor):
        date_format = "%Y-%m-%d"
        issue_date = datetime.strptime(doi, date_format)
        return_date = datetime.strptime(dor, date_format)
        delta = (return_date - issue_date).days
        if delta > 15:
            return '100'
        else:
            return '0'
        
    def return_book(self, member_id, calculated_fine):
        member_data = MEMBERS('members.db')
        member_data.update_fine(member_id, calculated_fine)


    def showmemid(self, mem_id):
        memID_pattern = mem_id + '%'
        self.cur.execute('SELECT * FROM Issue WHERE mem_id LIKE ?', (memID_pattern,))
        rows = self.cur.fetchall()
        return rows
