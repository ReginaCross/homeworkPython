from selenium.webdriver.common.by import By

class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа SauceDemo.
    """
    
    def __init__(self, driver):
        """
        Инициализирует страницу оформления заказа.
        
        Параметры:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
    
    def fill_first_name(self, first_name: str) -> None:
        """
        Заполняет поле имени.
        
        Параметры:
            first_name: str - имя пользователя
        
        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
    
    def fill_last_name(self, last_name: str) -> None:
        """
        Заполняет поле фамилии.
        
        Параметры:
            last_name: str - фамилия пользователя
        
        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
    
    def fill_postal_code(self, postal_code: str) -> None:
        """
        Заполняет поле почтового индекса.
        
        Параметры:
            postal_code: str - почтовый индекс
        
        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    
    def click_continue(self) -> None:
        """
        Нажимает кнопку Continue.
        
        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "continue").click()
    
    def get_total_price(self) -> str:
        """
        Получает итоговую стоимость заказа.
        
        Возвращает:
            str - итоговая стоимость
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text