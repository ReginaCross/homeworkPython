import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.saucedemo.login_page import LoginPage

@allure.feature("SauceDemo Tests")
@allure.severity(allure.severity_level.CRITICAL)
class TestSauceDemo:
    """
    Тесты для интернет-магазина SauceDemo.
    """
    
    @allure.title("Test complete purchase flow")
    @allure.description("Test complete purchase flow with multiple products")
    @allure.step("Setup: initialize driver and login")
    def setup_method(self):
        """
        Подготавливает тестовое окружение.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
        # Авторизация
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        self.products_page = login_page.click_login()
    
    @allure.step("Teardown: close driver")
    def teardown_method(self):
        """
        Завершает тестовое окружение.
        """
        self.driver.quit()
    
    @allure.step("Test complete purchase workflow")
    def test_complete_purchase(self):
        """
        Проверяет полный процесс покупки.
        
        Шаги:
        1. Добавляем товары в корзину
        2. Переходим в корзину
        3. Оформляем заказ
        4. Проверяем итоговую стоимость
        """
        with allure.step("Add products to cart"):
            products_to_add = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]
            
            for product in products_to_add:
                with allure.step(f"Add {product} to cart"):
                    self.products_page.add_product_to_cart(product)
        
        with allure.step("Go to cart"):
            cart_page = self.products_page.go_to_cart()
        
        with allure.step("Click checkout"):
            checkout_page = cart_page.click_checkout()
        
        with allure.step("Fill checkout form"):
            checkout_page.fill_first_name("John")
            checkout_page.fill_last_name("Doe")
            checkout_page.fill_postal_code("12345")
            checkout_page.click_continue()
        
        with allure.step("Verify total price"):
            total_price_text = checkout_page.get_total_price()
            assert "$58.29" in total_price_text, \
                f"Expected $58.29 but got {total_price_text}"