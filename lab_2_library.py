BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages:int):
        """
        Создание и подготовка к работе объекта Книга

        :param id_: идентификационный номер книги
        :param name: название книги
        :param pages: количество страниц в книге

        Примеры:
        #>>> book_1 = Book(3, "Не самое главное", 360) # закомментила, так как мешал автоматиеской проверке задания
        """
        if not isinstance(id_, int):
            raise TypeError("Id должен быть типа int")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library

class Library:
    def __init__(self, books: list = []):
        """
        Создание и подготовка к работе объекта Библиотека

        :param books: Список книг
        """
        if not isinstance(books, list):
            raise TypeError("Список книг должен быть типа list")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.

        :return: идентификатор для добавления новой книги в библиотеку
        """
        if len(self.books) == 0:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param id: идентификатор запрашиваемой книги
        :return: индекс книги в списке книг библиотеки
        """
        for i, book in enumerate(self.books):
            if book.id_ == id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
