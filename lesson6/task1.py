from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome() 

driver.get("http://uitestingplayground.com/ajax")
    
blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()
    

wait = WebDriverWait(driver, 15)
green_banner = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    

banner_text = green_banner.text
    

print(banner_text)


driver.quit()