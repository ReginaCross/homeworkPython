from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """
    Класс для работы со страницей калькулятора.
    
    Атрибуты:
        driver: WebDriver - экземпляр веб-драйвера
    """
    
    def __init__(self, driver):
        """
        Инициализирует страницу калькулятора.
        
        Параметры:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
    
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает значение задержки в поле ввода.
        
        Параметры:
            delay: int - значение задержки в секундах
        
        Возвращает:
            None
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))
    
    def click_number(self, number: int) -> None:
        """
        Нажимает кнопку с указанной цифрой.
        
        Параметры:
            number: int - цифра для нажатия (0-9)
        
        Возвращает:
            None
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{number}']").click()
    
    def click_operator(self, operator: str) -> None:
        """
        Нажимает кнопку с указанным оператором.
        
        Параметры:
            operator: str - оператор (+, -, ×, ÷)
        
        Возвращает:
            None
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{operator}']").click()
    
    def click_equals(self) -> None:
        """
        Нажимает кнопку '='.
        
        Возвращает:
            None
        """
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    def get_result(self) -> str:
        """
        Получает текущее значение из поля результата.
        
        Возвращает:
            str - текстовое значение результата
        """
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text
    
    def wait_for_result(self, expected_result: str, timeout: int = 45) -> str:
        """
        Ожидает появления указанного результата.
        
        Параметры:
            expected_result: str - ожидаемый результат
            timeout: int - время ожидания в секундах
        
        Возвращает:
            str - фактический результат
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda driver: self.get_result() == expected_result,
            f"Результат не равен {expected_result} после {timeout} секунд"
        )
        return self.get_result()