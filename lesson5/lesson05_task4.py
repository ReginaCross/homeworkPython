from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть браузер FireFox
driver = webdriver.Firefox()

    # Перейти на страницу
driver.get("http://the-internet.herokuapp.com/login")
    
    # Найти поле username и ввести значение
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
    
    # Найти поле password и ввести значение
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
    
    # Нажать кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
    
    # Дождаться появления зеленой плашки и получить текст
wait = WebDriverWait(driver, 10)
success_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    
    # Вывести текст с зеленой плашки в консоль
print("Текст с зеленой плашки:", success_message.text)
    

    # Закрыть браузер
driver.quit()