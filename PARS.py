import requests
from bs4 import BeautifulSoup
from Databasa import add_books, add_authors, create

create()
def database_url():
    id = -1
    for i in range(1,199):
        if i == 1:
            url = 'https://book24.ru/catalog/'
        else:
            url = 'https://book24.ru/catalog/' + f'page-{i}/'
        page = requests.get(url, timeout=7)
        if page.status_code != 200:
            raise Exception(f"Не удалось загрузить книгу: {page.status_code}")
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(page.text, 'html.parser')
        allLabelsAuthors = soup.find_all('div', class_='product-card__content')
        for label_author in allLabelsAuthors:
            id += 1
            find_label = label_author.find('a', class_='product-card__name')
            label_link = "https://book24.ru" + find_label.get('href')
            find_authors = label_author.find('a', class_='author-list__item smartLink')
            if find_authors:
                author_link = 'https://book24.ru' + find_authors.get('href')
            else:
                author_link = 'Ссылка не найдена'
            if find_label is not None:
                add_books(id, find_label.text.strip(), label_link)
            if find_authors is not None:
                add_authors(id, find_authors.text.strip(), author_link)

database_url()