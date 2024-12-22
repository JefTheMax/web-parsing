# web-parsing
Сервис для сортировки по именам Авторов и названиям книг.
# Как запустить проект?
1. Для запуска необходим предустановленных Docker.
2. Клонировать репозиторий git с github.com
'''git clone git@github.com:JefTheMax/web-parsing.git'''
3. Запуск проекта через build.sh
4. Перейти по ссылке
<font color='#gray'>http://localhost:5000/
#Описание проекта
С помощью этого сервиса можно настроить фильтры для алфавитного порядка или в обратно порядке как по названию товара, так и по автору(если он имеется).
# Как работает проект
1. Скрапинг происходит по каталогу сайта https://book24.ru/catalog
2. Полученные названия и ссылки на них хранятся в базе данных SQLite
3. Интерфейс состоит из товара и возможности выбора фильтра в зависимости от надобности
