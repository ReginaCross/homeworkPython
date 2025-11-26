import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestSauceDemo:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        
    def teardown_method(self):
        self.driver.quit()
        
    def test_complete_purchase_flow(self):
        
        login_page = LoginPage(self.driver)
        inventory_page = login_page.open() \
            .enter_username("standard_user") \
            .enter_password("secret_sauce") \
            .click_login()
            
        
        inventory_page.add_item_to_cart("Sauce Labs Backpack") \
            .add_item_to_cart("Sauce Labs Bolt T-Shirt") \
            .add_item_to_cart("Sauce Labs Onesie")
            
        
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.click_checkout()
        
        
        checkout_page.fill_customer_info("John", "Doe", "12345") \
            .click_continue()
            
       
        total_price = checkout_page.get_total_price()
        
       
        assert total_price == 58.29, f"Expected total $58.29, but got ${total_price}"
        
        
        checkout_page.finish_checkout()