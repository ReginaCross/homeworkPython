import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

class TestCalculator:
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Chrome()  
        self.driver.implicitly_wait(10)
        self.calculator_page = CalculatorPage(self.driver)
    
    def teardown_method(self):
        """Завершение после каждого теста"""
        self.driver.quit()
    
    def test_slow_calculator_addition(self):
        """Тест сложения с задержкой"""
        
        self.calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        
        self.calculator_page.set_delay(45)
        
        
        self.calculator_page.enter_calculation("7+8=")
        
        
        result = self.calculator_page.get_result(timeout=50)
        assert result == "15", f"Ожидался результат '15', но получено '{result}'"