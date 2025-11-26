import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    try:
        
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        
        
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        
        
        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
        
        
        wait = WebDriverWait(driver, 46)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        
        
        actual_result = result_element.text
        assert actual_result == "15", f"Ожидался результат '15', но получено '{actual_result}'"
        
        print("Тест пройден успешно! Результат 15 отобразился корректно.")
        
    finally:
        
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()