import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from pages import main_page
from utilities.logger import Logger


class BasketPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators

    product_name_basket = "//span[@data-entity='basket-item-name']"
    product_price_basket = "//span[contains(@id,'basket-item-price')]"
    order_button = "//button[@data-entity='basket-checkout-button']"

    # Getters

    def get_product_name_basket(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_name_basket)))

    def get_product_price_basket(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_price_basket)))

    def get_order_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions

    def save_product_name_basket(self):
        global product_name_basket_text
        product_name_basket_text = self.get_product_name_basket().text
        return product_name_basket_text

    def save_product_price_basket(self):
        global product_price_basket_text
        product_price_basket_text = self.get_product_price_basket().text
        return product_price_basket_text

    def click_order_button(self):
        self.get_order_button().click()
        print("Click on the order button")


    # Methods

    def check_basket_info_and_continue(self):
        with allure.step('Checking basket info and continuing'):
            Logger.add_start_step(method='check_basket_info_and_continue')
            self.get_current_url()
            self.assert_url("https://tomsk.znaemigraem.ru/cart/")
            product_name_basket_text = self.save_product_name_basket()
            print(f"Product name in the basket: {product_name_basket_text}")
            product_price_basket_text = self.save_product_price_basket()
            print(f"Product price in the basket: {product_price_basket_text}")
            self.assert_title(main_page.product_name_on_main_page, product_name_basket_text)
            self.assert_price(main_page.product_price_on_main_page, product_price_basket_text)
            self.click_order_button()
            Logger.add_end_step(url=self.driver.current_url, method='check_basket_info_and_continue')
















