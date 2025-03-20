import pytest
from main import BooksCollector


class TestBooksCollector:

    # успешное добавление книги с валидной длиной названия в books_genre
    def test_add_new_book_valid_length_successfully_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и вафельщик')
        assert 'Гордость и вафельщик' in collector.books_genre

    # книги с невалидной длиной не добавляются в books_genre: 0, 41 и 42 символов
    @pytest.mark.parametrize('name', ['', 'abcabcabcabcabcabcabcabcabcabcabcabcabcab', 'abcabcabcabcabcabcabcabcabcabcabcabcabcabc'])
    def test_add_new_book_invalid_length_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # успешное добавление жанра из genre созданной книге
    def test_set_book_genre_successfully_setted(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и вафельщик')
        collector.set_book_genre('Гордость и вафельщик', 'Комедии')
        assert collector.books_genre['Гордость и вафельщик'] == 'Комедии'

    # успешное получение жанра после его присвоения созданной книге
    def test_get_book_genre_successfully_returns_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и вафельщик')
        collector.set_book_genre('Гордость и вафельщик', 'Комедии')
        assert collector.get_book_genre('Гордость и вафельщик') == 'Комедии'

    # успешное получение списка книг только одного определенного жанра
    def test_get_books_with_specific_genre_successfully_returns_specific_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и вафельщик')
        collector.add_new_book('Yet Another Comedy Book')
        collector.add_new_book('Книга ужасов')
        collector.set_book_genre('Гордость и вафельщик', 'Комедии')
        collector.set_book_genre('Yet Another Comedy Book', 'Комедии')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == ['Гордость и вафельщик', 'Yet Another Comedy Book']

    # успешное получение текущего словаря books_genre
    def test_get_books_genre_successfully_returns_books_genre_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Yet Another Comedy Book')
        collector.set_book_genre('Yet Another Comedy Book', 'Комедии')
        assert collector.get_books_genre() == {'Yet Another Comedy Book': 'Комедии'}

    # успешное получение списка books_for_children без книг возрастного жанра
    def test_get_books_for_children_successfully_returns_books_only_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Анекдоты для детей')
        collector.add_new_book('Yet Another Comedy Book')
        collector.add_new_book('Книга ужасов')
        collector.add_new_book('Очень остросюжетный детектив')
        collector.set_book_genre('Анекдоты для детей', 'Комедии')
        collector.set_book_genre('Yet Another Comedy Book', 'Комедии')
        collector.set_book_genre('Книга ужасов', 'Ужасы')
        collector.set_book_genre('Очень остросюжетный детектив', 'Детективы')
        assert collector.get_books_for_children() == ['Анекдоты для детей', 'Yet Another Comedy Book']

    # успешное получение списка favorites с любимыми книгами
    def test_add_book_in_favorites_successfully_adds_book_to_favorites_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Люблю эту книгу')
        collector.add_new_book('А эту не люблю')
        collector.add_book_in_favorites('Люблю эту книгу')
        assert collector.favorites == ['Люблю эту книгу']

    # успешное удаление книги из списка favorites
    def test_delete_book_from_favorites_successfully_removes_book_from_favorites_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Люблю эту книгу')
        collector.add_book_in_favorites('Люблю эту книгу')
        collector.delete_book_from_favorites('Люблю эту книгу')
        assert collector.favorites == []

    # успешное получение списка favorites с избранными книгами
    def test_get_list_of_favorites_books_successfully_returns_favorites_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Люблю эту книгу')
        collector.add_new_book('И эту книгу люблю')
        collector.add_new_book('А эту не люблю')
        collector.add_book_in_favorites('Люблю эту книгу')
        collector.add_book_in_favorites('И эту книгу люблю')
        assert collector.get_list_of_favorites_books() == ['Люблю эту книгу', 'И эту книгу люблю']
