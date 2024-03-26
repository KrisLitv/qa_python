
import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book(collector):
    # добавляем новую книгу
    collector.add_new_book("Book1")
    assert "Book1" in collector.get_books_genre()

def test_add_new_book_add_two_books(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    assert len(collector.get_books_genre()) == 2

def test_set_book_genre(collector):
    # устанавливаем книге жанр
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_book_genre("Book1") == "Фантастика"

@pytest.mark.parametrize("genre, expected_books", [("Фантастика", ["Book1", "Book2"]),
                                                   ("Ужасы", ["Book3"]),
                                                   ("Детективы", [])])
def test_get_books_with_specific_genre(collector, genre, expected_books):
    # выводим список книг с определённым жанром
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.add_new_book("Book3")
    collector.set_book_genre("Book1", "Фантастика")
    collector.set_book_genre("Book2", "Фантастика")
    collector.set_book_genre("Book3", "Ужасы")
    assert collector.get_books_with_specific_genre(genre) == expected_books

def test_get_books_genre(collector):
    # получаем жанр книги по её имени
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_books_genre() == {"Book1": "Фантастика"}

def test_get_books_for_children(collector):
    # Добавляем книги различных жанров, включая жанры с возрастным рейтингом
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.add_new_book("Book3")
    collector.add_new_book("Book4")
    collector.set_book_genre("Book1", "Фантастика")
    collector.set_book_genre("Book2", "Ужасы")
    collector.set_book_genre("Book3", "Детективы")
    collector.set_book_genre("Book4", "Мультфильмы")
    # Проверяем, что книги с возрастным рейтингом не попали в список книг для детей
    assert collector.get_books_for_children() == ["Book1", "Book4"]

def test_add_book_in_favorites(collector):
    # добавляем книгу в Избранное
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    collector.add_book_in_favorites("Book1")
    assert collector.get_list_of_favorites_books() == ["Book1"]

def test_delete_book_from_favorites(collector):
    # удаляем книгу из Избранного
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    collector.add_book_in_favorites("Book1")
    collector.delete_book_from_favorites("Book1")
    # Проверяем, что метод delete_book_from_favorites удаляет книгу из списка избранных книг
    assert collector.get_list_of_favorites_books() == []

def test_get_list_of_favorites_books(collector):
    # Добавляем несколько книг в избранное
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.add_new_book("Book3")
    collector.add_book_in_favorites("Book1")
    collector.add_book_in_favorites("Book3")
    # Проверяем, что метод get_list_of_favorites_books возвращает правильный список избранных книг
    assert collector.get_list_of_favorites_books() == ["Book1", "Book3"]
