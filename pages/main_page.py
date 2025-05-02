import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.action = ActionChains(self.driver)
        self.min_players = '1'
        self.max_players = '1'
        self.min_age = '4'
        self.max_age = '5'
        self.min_time = '15'
        self.max_time = '20'


    # Locators

    filter_icon = "(//i[@class='material-icons' and @data-icon='expand_more'])[1]"
    filter_num_players_min = "//input[@id='catalogFilter_193_MIN']"
    filter_num_players_max = "//input[@id='catalogFilter_193_MAX']"
    filter_age_min = "//input[@id='catalogFilter_195_MIN']"
    filter_age_max = "//input[@id='catalogFilter_195_MAX']"
    filter_time_min = "//input[@id='catalogFilter_198_MIN']"
    filter_time_max = "//input[@id='catalogFilter_198_MAX']"
    filter_producer = "//span[@title='Стиль жизни']"
    set_filter_button = "//button[@name='set_filter']"
    buy_button = "(//a[contains(text(),'КУПИТЬ')])[1]"
    product_name_on_main_page = "(//a[@class='name'])[1]"
    product_price_on_main_page = "(//span[@class='catalog-item__price'])[1]"
    basket_button = "//span[@class='product-label']"

    # Getters

    def get_filter_icon(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_icon)))

    def get_filter_num_players_min(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_num_players_min)))

    def get_filter_num_players_max(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_num_players_max)))

    def get_filter_age_min(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_age_min)))

    def get_filter_age_max(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_age_max)))

    def get_filter_time_min(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_time_min)))

    def get_filter_time_max(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_time_max)))

    def get_filter_producer(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filter_producer)))

    def get_set_filter_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.set_filter_button)))

    def get_buy_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_product_name_on_main_page(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_name_on_main_page)))

    def get_product_price_on_main_page(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_price_on_main_page)))

    def get_basket_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))

    # Actions

    def click_filter_icon(self):
        self.get_filter_icon().click()
        print("Click on the filter")

    def input_filter_num_players_min(self, min_players):
        self.get_filter_num_players_min().send_keys(min_players)
        print("Input min number of players")

    def input_filter_num_players_max(self, max_players):
        self.get_filter_num_players_max().send_keys(max_players)
        print("Input max number of players")

    def input_filter_age_min(self, min_age):
        self.get_filter_age_min().send_keys(min_age)
        print("Input min age")

    def input_filter_age_max(self, max_age):
        self.get_filter_age_max().send_keys(max_age)
        print("Input max age")

    def input_filter_time_min(self, min_time):
        self.get_filter_time_min().send_keys(min_time)
        print("Input min time")

    def input_filter_time_max(self, max_time):
        self.get_filter_time_max().send_keys(max_time)
        print("Input max time")

    def scroll_and_click_filter_producer(self):
        self.action.move_to_element(self.get_filter_producer()).click().perform()
        print("Choose a game producer")

    def click_set_filter_button(self):
        self.get_set_filter_button().click()
        print("Click on the set filter button")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click on the buy button")

    def click_basket_button(self):
        self.get_basket_button().click()
        print("Click on the basket button")

    def save_product_name_on_main_page(self):
        global product_name_on_main_page
        product_name_on_main_page = self.get_product_name_on_main_page().text
        return product_name_on_main_page

    def save_product_price_on_main_page(self):
        global product_price_on_main_page
        product_price_on_main_page = self.get_product_price_on_main_page().text
        return product_price_on_main_page


    # Methods

    def select_product(self):
        with allure.step('Selecting a product with filters'):
            Logger.add_start_step(method='select_product')
            self.click_filter_icon()
            self.input_filter_num_players_min(self.min_players)
            self.input_filter_num_players_max(self.max_players)
            self.input_filter_age_min(self.min_age)
            self.input_filter_age_max(self.max_age)
            self.input_filter_time_min(self.min_time)
            self.input_filter_time_max(self.max_time)
            self.scroll_and_click_filter_producer()
            self.click_set_filter_button()
            product_name_on_main_page = self.save_product_name_on_main_page()
            print(f"Product name: {product_name_on_main_page}")
            product_price_on_main_page = self.save_product_price_on_main_page()
            print(f"Product price: {product_price_on_main_page}")
            self.click_buy_button()
            self.click_basket_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_product')











