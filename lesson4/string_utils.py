class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """
    
    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
        Пример: `capitalize("skypro") -> "Skypro"`
        """
        if len(string) == 0:
            return string
        return string[0].upper() + string[1:]
    
    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        if len(string) == 0:
            return string
        while string.startswith(" "):
            string = string[1:]
        return string
    
    def to_list(self, string: str, delimiter: str = ",") -> list:
        """
        Принимает на вход текст с разделителем и возвращает список строк
        Параметры:
            string: строка для обработки
            delimiter: разделитель (по умолчанию запятая)
        Пример: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
        """
        if len(string) == 0:
            return []
        return string.split(delimiter)
    
    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ и `False` - если нет
        Параметры:
            string: строка для поиска
            symbol: искомый символ
        Пример: `contains("SkyPro", "S") -> True`
        """
        return symbol in string
    
    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        Параметры:
            string: строка для обработки
            symbol: искомый символ для удаления
        Пример: `delete_symbol("SkyPro", "k") -> "SyPro"`
        """
        return string.replace(symbol, "")
    
    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
        Параметры:
            string: строка для проверки
            symbol: искомый символ
        Пример: `starts_with("SkyPro", "S") -> True`
        """
        return string.startswith(symbol)
    
    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
        Параметры:
            string: строка для проверки
            symbol: искомый символ
        Пример: `end_with("SkyPro", "o") -> True`
        """
        return string.endswith(symbol)
    
    def is_empty(self, string: str) -> bool:
        """
        Возвращает `True`, если строка пустая и `False` - если нет
        Пример: `is_empty("") -> True`
        """
        return len(string) == 0
    
    def list_to_string(self, lst: list, joiner: str = ", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем
        Параметры:
            lst: список элементов
            joiner: разделитель (по умолчанию запятая с пробелом)
        Пример: `list_to_string(["a", "b", "c"]) -> "a, b, c"`
        """
        return joiner.join(map(str, lst))