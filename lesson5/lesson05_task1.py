from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

    
        # 1. Открыть браузер Google Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        # 2. Перейти на страницу
driver.get("http://uitestingplayground.com/classattr")

        
        # 3. Кликнуть на синюю кнопку
        # Синяя кнопка имеет класс 'btn-primary'
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

        
        # Небольшая пауза чтобы увидеть результат
time.sleep(2)