'''
Lesson 26 - Database
sqlite3
database
table
sql
'''
import sqlite3

def create_contact(cur, conn, name, phone, email, address, active=1):
    cur.execute('''
        INSERT INTO contacts(name, phone, email, address, active)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, phone, email, address, active))
    conn.commit()

def read_contacts(cur):
    return cur.execute('''
        SELECT *
        FROM contacts
    ''').fetchall()

def update_contact(cur, conn, id, name, phone, email, address, active):
    cur.execute('''
        UPDATE contacts
        SET name=?, phone=?, email=?, address=?, active=?
        WHERE id=?
    ''', (name, phone, email, address, active, id))
    conn.commit()

def delete_contact(cur, conn, id):
    cur.execute('''
        DELETE FROM contacts WHERE id=?
    ''', (id,))
    conn.commit()

def make_contacts_table(cur, conn):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                email TEXT,
                address TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active INTEGER DEFAULT 1
                )
    ''')
    conn.commit()

def main():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    make_contacts_table(cursor, conn)

    create_contact(cursor, conn, 'Red', '123456', 'red@mail.com', 'London')
    create_contact(cursor, conn, 'Tea', '222222', 'tea@mail.com', 'Paris')
    update_contact(cursor, conn, 3, 'Bob', '333333', 'bob@mail.com', 'Berlin', 1)
    delete_contact(cursor, conn, 1)

    for c in read_contacts(cursor):
        print(c)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()