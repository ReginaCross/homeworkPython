import pytest 
from string_utils import StringUtils

class TestStringUtils:
    
    @pytest.fixture
    def utils(self):
        return StringUtils()
    
    # Тесты для функции capitalize
    def test_capitalize_positive(self, utils):
        """Позитивные тесты для capitalize"""
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("a") == "A"
        assert utils.capitalize("Skypro") == "Skypro"
    
    def test_capitalize_negative(self, utils):
        """Негативные тесты для capitalize"""
        assert utils.capitalize("") == ""
        assert utils.capitalize("123") == "123"
        assert utils.capitalize(" skypro") == " skypro"
    
    # Тесты для функции trim
    def test_trim_positive(self, utils):
        """Позитивные тесты для trim"""
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello  ") == "hello  "
        assert utils.trim(" sky pro ") == "sky pro "
        assert utils.trim("a") == "a"
        assert utils.trim("") == ""
    
    def test_trim_negative(self, utils):
        """Негативные тесты для trim"""
        assert utils.trim("skypro   ") == "skypro   "
        assert utils.trim("  ") == ""
    
    # Тесты для функции to_list
    def test_to_list_positive(self, utils):
        """Позитивные тесты для to_list"""
        assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
        assert utils.to_list("1;2;3", ";") == ["1", "2", "3"]
        assert utils.to_list("hello") == ["hello"]
        assert utils.to_list("") == []
        assert utils.to_list("a,b,c,d", "-") == ["a,b,c,d"]
    
    def test_to_list_negative(self, utils):
        """Негативные тесты для to_list"""
        assert utils.to_list("a,b,c,d", ";") == ["a,b,c,d"]
        assert utils.to_list("   ") == ["   "]
    
    # Тесты для функции contains
    def test_contains_positive(self, utils):
        """Позитивные тесты для contains"""
        assert utils.contains("SkyPro", "S") == True
        assert utils.contains("SkyPro", "y") == True
        assert utils.contains("SkyPro", "Pro") == True
        assert utils.contains("hello", "h") == True
    
    def test_contains_negative(self, utils):
        """Негативные тесты для contains"""
        assert utils.contains("SkyPro", "U") == False
        assert utils.contains("", "a") == False
        assert utils.contains("hello", "H") == False
        assert utils.contains("test", "test1") == False
    
    # Тесты для функции delete_symbol
    def test_delete_symbol_positive(self, utils):
        """Позитивные тесты для delete_symbol"""
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("hello", "l") == "heo"
        assert utils.delete_symbol("banana", "a") == "bnn"
        assert utils.delete_symbol("test", "x") == "test"
    
    def test_delete_symbol_negative(self, utils):
        """Негативные тесты для delete_symbol"""
        assert utils.delete_symbol("", "a") == ""
        assert utils.delete_symbol("hello", "") == "hello"
        assert utils.delete_symbol("aaa", "a") == ""
    
    # Тесты для функции starts_with
    def test_starts_with_positive(self, utils):
        """Позитивные тесты для starts_with"""
        assert utils.starts_with("SkyPro", "S") == True
        assert utils.starts_with("hello", "h") == True
        assert utils.starts_with(" test", " ") == True
        assert utils.starts_with("123", "1") == True
    
    def test_starts_with_negative(self, utils):
        """Негативные тесты для starts_with"""
        assert utils.starts_with("SkyPro", "s") == False
        assert utils.starts_with("", "a") == False
        assert utils.starts_with("hello", "H") == False
        assert utils.starts_with("test", "est") == False
    
    # Тесты для функции end_with
    def test_end_with_positive(self, utils):
        """Позитивные тесты для end_with"""
        assert utils.end_with("SkyPro", "o") == True
        assert utils.end_with("hello", "o") == True
        assert utils.end_with("test ", " ") == True
        assert utils.end_with("123", "3") == True
    
    def test_end_with_negative(self, utils):
        """Негативные тесты для end_with"""
        assert utils.end_with("SkyPro", "O") == False
        assert utils.end_with("", "a") == False
        assert utils.end_with("hello", "H") == False
        assert utils.end_with("test", "tes") == False
    
    # Тесты для функции is_empty
    def test_is_empty_positive(self, utils):
        """Позитивные тесты для is_empty"""
        assert utils.is_empty("") == True
        assert utils.is_empty(" ") == False
        assert utils.is_empty("hello") == False
        assert utils.is_empty("   ") == False
    
    def test_is_empty_edge_cases(self, utils):
        """Граничные случаи для is_empty"""
        assert utils.is_empty("\t") == False
        assert utils.is_empty("\n") == False
    
    # Тесты для функции list_to_string
    def test_list_to_string_positive(self, utils):
        """Позитивные тесты для list_to_string"""
        assert utils.list_to_string(["a", "b", "c"]) == "a, b, c"
        assert utils.list_to_string([1, 2, 3]) == "1, 2, 3"
        assert utils.list_to_string(["a", "b", "c"], "-") == "a-b-c"
        assert utils.list_to_string([]) == ""
        assert utils.list_to_string(["single"]) == "single"
    
    def test_list_to_string_negative(self, utils):
        """Негативные тесты для list_to_string"""
        assert utils.list_to_string(["a", "b", "c"], "") == "ab c"
        assert utils.list_to_string([""]) == ""
        assert utils.list_to_string([" ", " "]) == " ,  "
    
    # Параметризованные тесты для более комплексного покрытия
    @pytest.mark.parametrize("input_str,expected", [
        ("test", "Test"),
        ("TEST", "TEST"),
        ("123test", "123test"),
        (" test", " test"),
    ])
    def test_capitalize_parametrized(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected
    
    @pytest.mark.parametrize("input_str,symbol,expected", [
        ("hello", "l", "heo"),
        ("mississippi", "s", "miiippi"),
        ("abc", "d", "abc"),
        ("", "a", ""),
    ])
    def test_delete_symbol_parametrized(self, utils, input_str, symbol, expected):
        assert utils.delete_symbol(input_str, symbol) == expected