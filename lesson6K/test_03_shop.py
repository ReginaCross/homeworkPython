from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_shopping_cart_total():
    driver = None
    try:
        
        driver = webdriver.Firefox()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        
        
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")
        
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        
        
        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_add_button.click()
        
        
        tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_add_button.click()
        
        
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_add_button.click()
        
        
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        
        
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        
        
        first_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("Иван")
        
        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")
        
        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")
        
        
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
        
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_amount = total_text.replace("Total: $", "")
        
        print(f"Итоговая стоимость: ${total_amount}")
        
        
        expected_total = "58.29"
        assert total_amount == expected_total, f"Ожидалась сумма ${expected_total}, но получена ${total_amount}"
        
        print("Тест пройден успешно! Итоговая сумма корректна.")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise
        
    finally:
        
        if driver:
            driver.quit()

if __name__ == "__main__":
    test_shopping_cart_total()