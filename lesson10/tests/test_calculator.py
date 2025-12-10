import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@allure.feature("Calculator Tests")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """
    Тесты для калькулятора.
    """
    
    @allure.title("Test calculator with delay")
    @allure.description("Test that calculator shows correct result after delay")
    @allure.step("Setup: initialize driver and calculator page")
    def setup_method(self):
        """
        Подготавливает тестовое окружение.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator = CalculatorPage(self.driver)
    
    @allure.step("Teardown: close driver")
    def teardown_method(self):
        """
        Завершает тестовое окружение.
        """
        self.driver.quit()
    
    @allure.step("Test calculation 7 + 8 with 45 seconds delay")
    def test_calculator_with_delay(self):
        """
        Проверяет работу калькулятора с задержкой.
        
        Шаги:
        1. Устанавливаем задержку 45 секунд
        2. Выполняем операцию 7 + 8
        3. Проверяем результат через 45 секунд
        """
        with allure.step("Set delay to 45 seconds"):
            self.calculator.set_delay(45)
        
        with allure.step("Perform calculation: 7 + 8"):
            self.calculator.click_number(7)
            self.calculator.click_operator('+')
            self.calculator.click_number(8)
            self.calculator.click_equals()
        
        with allure.step("Wait for result and verify it equals 15"):
            result = self.calculator.wait_for_result("15", timeout=46)
            assert result == "15", f"Expected 15 but got {result}"