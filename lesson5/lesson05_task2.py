from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

    # Открыть браузер Google Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
        # Переход на страницу
driver.get("http://uitestingplayground.com/dynamicid")
        
        # Небольшая пауза для загрузки страницы
time.sleep(2)
        
        # Поиск синей кнопки по классу (так как ID динамический)
        # Кнопка имеет класс 'btn btn-primary'
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        
        # Клик по кнопке
blue_button.click()
        

        # Небольшая пауза чтобы увидеть результат
time.sleep(4)