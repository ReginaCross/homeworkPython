from selenium.webdriver.common.by import By

class CartPage:
    """
    Класс для работы со страницей корзины SauceDemo.
    """
    
    def __init__(self, driver):
        """
        Инициализирует страницу корзины.
        
        Параметры:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
    
    def get_cart_items_count(self) -> int:
        """
        Получает количество товаров в корзине.
        
        Возвращает:
            int - количество товаров
        """
        cart_badge = self.driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
        return int(cart_badge[0].text) if cart_badge else 0
    
    def click_checkout(self):
        """
        Нажимает кнопку Checkout.
        
        Возвращает:
            CheckoutPage - объект страницы оформления заказа
        """
        from pages.saucedemo.checkout_page import CheckoutPage
        self.driver.find_element(By.ID, "checkout").click()
        return CheckoutPage(self.driver)