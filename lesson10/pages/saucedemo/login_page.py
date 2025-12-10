from selenium.webdriver.common.by import By

class LoginPage:
    """
    Класс для работы со страницей авторизации SauceDemo.
    """
    
    def __init__(self, driver):
        """
        Инициализирует страницу авторизации.
        
        Параметры:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
    
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле ввода.
        
        Параметры:
            username: str - имя пользователя
        
        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
    
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле ввода.
        
        Параметры:
            password: str - пароль пользователя
        
        Возвращает:
            None
        """
        self.driver.find_element(By.ID, "password").send_keys(password)
    
    def click_login(self):
        """
        Нажимает кнопку входа.
        
        Возвращает:
            ProductsPage - объект страницы товаров
        """
        from pages.saucedemo.products_page import ProductsPage
        self.driver.find_element(By.ID, "login-button").click()
        return ProductsPage(self.driver)