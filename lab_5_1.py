class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        s = f'Название книги: "{self.title}", Автор: {self.author}, Год издания: {self.year}".'
        return s


title = 'Преступление и наказание'
author = 'М. Ф. Достоевский'
year = '1866'
one_book = Book(title, author, year)
print(one_book.get_info())