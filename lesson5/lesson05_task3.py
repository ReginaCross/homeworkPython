from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть браузер Firefox
driver = webdriver.Firefox()

    # Перейти на страницу
driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Небольшая пауза для загрузки страницы
time.sleep(2)
    
    # Найти поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")
    
    # Ввести в поле текст "Sky"
input_field.send_keys("Sky")
    
    # Небольшая пауза для наглядности
time.sleep(1)
    
    # Очистить поле
input_field.clear()
    
    # Небольшая пауза для наглядности
time.sleep(2)
    
    # Ввести в поле текст "Pro"
input_field.send_keys("Pro")
    
    # Небольшая пауза чтобы увидеть результат
time.sleep(2)

    # Закрыть браузер
driver.quit()