# qa_python

### Тесты: 

1. "test_add_new_book_valid_length_successfully_added":
    * на успешное добавление книги с валидной длиной названия в books_genre.

2. "test_add_new_book_invalid_length_not_added": 
    * на книги с невалидной длиной (0, 41 и 42 символов), который не добавляются в books_genre

3. "test_set_book_genre_successfully_setted":
    * на успешное добавление жанра созданной книге

4. "test_get_book_genre_successfully_returns_genre":
    * на успешное получение жанра после его присвоения созданной книге

5. "test_get_books_with_specific_genre_successfully_returns_specific_books":
    * на успешное получение списка книг только одного определенного жанра

6. "test_get_books_genre_successfully_returns_books_genre_dictionary":
    * на успешное получение текущего словаря books_genre

7. "test_get_books_for_children_successfully_returns_books_only_for_children":
    * на успешное получение списка books_for_children без книг возрастного жанра

8. "test_add_book_in_favorites_successfully_adds_book_to_favorites_dictionary":
    * на успешное получение списка favorites с любимыми книгами

9. "test_delete_book_from_favorites_successfully_removes_book_from_favorites_dictionary":
    * на успешное удаление книги из списка favorites

10. "test_get_list_of_favorites_books_successfully_returns_favorites_dictionary":
    * на успешное получение списка favorites с избранными книгами