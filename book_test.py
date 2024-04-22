import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedźmin", "Sapkowski", 1997)
    def test_get_info(self):
        text_correct = 'Tytuł: Wiedźmin Autor: Sapkowski Rok: 1997'
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)
    def test_change_title(self):
        self.book.change_title("Miecz przeznaczenia")
        # można tak sprawdzić zmianę
        #text_correct = 'Tytuł: Miecz przeznaczenia Autor: Sapkowski Rok: 1997'
        #text_result = self.book.get_info()
        #self.assertEqual(text_correct, text_result)
        # można tak, najpierw pobrać dane i następnie je podać do asercji
        #text_correct = "Miecz przeznaczenia"
        #text_result = self.book.title
        #self.assertEqual(text_correct, text_result)
        self.assertEqual("Miecz przeznaczenia", self.book.title)
    def test_change_author(self):
        self.book.change_author("Tolkien")
        self.assertEqual("Tolkien", self.book.author)
    def test_change_year(self):
        self.book.change_year(2024)
        self.assertEqual(2024, self.book.year)

if __name__ == '__main__':
    unittest.main()