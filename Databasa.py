import sqlite3

# Создаем подключение к базе данных (файл my_books_database.db будет создан)

def create():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book_link (
    id INTEGER PRIMARY KEY,
    [Название книги] TEXT NOT NULL,
    [Ссылка книги] TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Author_link (
    id INTEGER PRIMARY KEY,
    [Автор книги] TEXT NOT NULL,
    [Ссылка автора] TEXT NOT NULL
    )
    ''')
    connection.commit()

def add_books(id, labels, links_book):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Book_link WHERE id == ?', (id,))
    results = cursor.fetchall()
    if not results:
        cursor.execute('INSERT INTO Book_link (id, [Название книги], [Ссылка книги]) VALUES(?, ?, ?)', (id, labels, links_book))
    else:
        cursor.execute('UPDATE Book_link SET [Название книги] = ?, [Ссылка книги] = ? WHERE id = ?',(labels, links_book, id))
    connection.commit()
    connection.close()

def add_authors(id, authors, links_authors):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Author_link WHERE id == ?', (id,))
    results = cursor.fetchall()
    if not results:
        cursor.execute('INSERT INTO Author_link (id, [Автор книги], [Ссылка автора]) VALUES(?, ?, ?)', (id, authors, links_authors))
    else:
        cursor.execute('UPDATE Author_link SET [Автор книги] = ?, [Ссылка автора] = ? WHERE id = ?',
                       (authors, links_authors, id))
    connection.commit()
    connection.close()