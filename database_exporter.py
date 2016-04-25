import sqlite3


def create_table():
    conn = sqlite3.connect('websites.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE websites (id integer primary key autoincrement, websites TEXT)''')
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect('websites.db')
    c = conn.cursor()
    file = open ('List-of-all-sites.txt','rt')
    for lines in file:
        print (lines)
        c.execute("INSERT INTO websites (websites) VALUES (?)",(lines,))
        break
    conn.commit()
    conn.close()
insert_data()
