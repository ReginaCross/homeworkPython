from selenium.webdriver.common.by import By

class ProductsPage:
    """
    Класс для работы со страницей товаров SauceDemo.
    """
    
    def __init__(self, driver):
        """
        Инициализирует страницу товаров.
        
        Параметры:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
    
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.
        
        Параметры:
            product_name: str - название товара
        
        Возвращает:
            None
        """
        # Находим родительский элемент товара по названию
        product_element = self.driver.find_element(
            By.XPATH, 
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']"
        )
        # Нажимаем кнопку добавления в корзину
        product_element.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
    
    def go_to_cart(self):
        """
        Переходит в корзину покупок.
        
        Возвращает:
            CartPage - объект страницы корзины
        """
        from pages.saucedemo.cart_page import CartPage
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        return CartPage(self.driver)