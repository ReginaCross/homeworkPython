from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        
        # Кнопки калькулятора
        self.buttons = {
            '0': (By.XPATH, "//span[text()='0']"),
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '*': (By.XPATH, "//span[text()='×']"),
            '/': (By.XPATH, "//span[text()='÷']"),
            '=': (By.XPATH, "//span[text()='=']"),
            'C': (By.XPATH, "//span[text()='C']")
        }
    
    def open(self, url):
        """Открыть страницу калькулятора"""
        self.driver.get(url)
    
    def set_delay(self, delay_value):
        """Установить значение задержки"""
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))
    
    def click_button(self, button):
        """Нажать на кнопку калькулятора"""
        if button in self.buttons:
            button_element = self.driver.find_element(*self.buttons[button])
            button_element.click()
        else:
            raise ValueError(f"Кнопка '{button}' не найдена")
    
    def enter_calculation(self, expression):
        """Ввести математическое выражение (последовательность нажатий кнопок)"""
        for char in expression:
            self.click_button(char)
    
    def get_result(self, timeout=50):
        """Получить результат вычислений с ожиданием"""
        wait = WebDriverWait(self.driver, timeout)
        result_element = wait.until(
            EC.text_to_be_present_in_element(self.result_display, "")
        )
        return self.driver.find_element(*self.result_display).text
    
    def get_current_display(self):
        """Получить текущее значение на дисплее"""
        return self.driver.find_element(*self.result_display).text