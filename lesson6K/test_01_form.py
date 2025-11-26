from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_form_validation():
    
    driver = webdriver.Edge()
    
    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        
        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("Иван")
        
        
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Петров")
        
        
        address = driver.find_element(By.ID, "address")
        address.send_keys("Ленина, 55-3")
        
        
        email = driver.find_element(By.ID, "e-mail")
        email.send_keys("test@skypro.com")
        
        
        phone = driver.find_element(By.ID, "phone")
        phone.send_keys("+7985899998787")
        
        
        
        
        city = driver.find_element(By.ID, "city")
        city.send_keys("Москва")
        
        
        country = driver.find_element(By.ID, "country")
        country.send_keys("Россия")
        
        
        job_position = driver.find_element(By.ID, "job-position")
        job_position.send_keys("QA")
        
        
        company = driver.find_element(By.ID, "company")
        company.send_keys("SkyPro")
        
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        
        
        
        zip_code_field = driver.find_element(By.ID, "zip-code")
        zip_code_classes = zip_code_field.get_attribute("class")
        
        assert "is-invalid" in zip_code_classes, "Поле Zip code не подсвечено красным"
        print("✓ Поле Zip code подсвечено красным")
        
        
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", 
            "phone", "city", "country", "job-position", "company"
        ]
        
        for field_id in fields_to_check:
            field = driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")
            
            assert "is-valid" in field_classes, f"Поле {field_id} не подсвечено зеленым"
            print(f"✓ Поле {field_id} подсвечено зеленым")
        
        print("\nВсе проверки пройдены успешно!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise e
        
    finally:
        
        driver.quit()


if __name__ == "__main__":
    test_form_validation()