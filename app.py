from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'my_database.db'

def get_books_from_database():
    with sqlite3.connect(app.config['DATABASE']) as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT b.id, b.[Название книги], b.[Ссылка книги], a.[Автор книги], a.[Ссылка автора]
                          FROM Book_link b
                          JOIN Author_link a ON b.id = a.id''')
        books = cursor.fetchall()
    # Преобразовать результаты в список словарей для удобства
    return [{'id': row[0], 'title': row[1], 'link': row[2], 'author': row[3], 'author_link': row[4]} for row in books]

@app.route('/')
def index():
    order = request.args.get('order')  # Получаем параметр сортировки из URL
    books = get_books_from_database()  # Получение книг из базы

    # Сортируем книги по необходимости
    if order == 'title.asc':
        books.sort(key=lambda x: x['title'])  # Сортировка по названию
    elif order == 'title.desc':
        books.sort(key=lambda x: x['title'], reverse=True)  # Обратная сортировка по названию
    elif order == 'author.asc':
        books.sort(key=lambda x: x['author'])  # Сортировка по автору
    elif order == 'author.desc':
        books.sort(key=lambda x: x['author'], reverse=True)  # Обратная сортировка по автору

    return render_template('index.html', books=books)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)  #i love you