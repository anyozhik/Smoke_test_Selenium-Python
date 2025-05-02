import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class OrderPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.street_name_info = 'Ленина'
        self.building_number_info = '25'
        self.entrance_number_info = '3'
        self.floor_number_info = '3'
        self.apartment_number_info = '125'


    # Locators

    delivery_option = "//label[@for='delivery_123']"
    street_name = "(//input[@name='ORDER_PROP_7'])[1]"
    building_number = "(//input[@name='ORDER_PROP_25'])[1]"
    entrance_number = "(//input[@name='ORDER_PROP_31'])[1]"
    floor_number= "(//input[@name='ORDER_PROP_26'])[1]"
    apartment_number = "(//input[@name='ORDER_PROP_27'])[1]"
    continue_button = "(//button[@class='v-btn--full btn btn-primary'])"

    # Getters

    def get_delivery_option(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.delivery_option)))

    def get_street(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.street_name)))

    def get_building(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.building_number)))

    def get_entrance(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.entrance_number)))

    def get_floor(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.floor_number)))

    def get_apartment(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.apartment_number)))

    def get_continue_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def click_delivery_option(self):
        self.driver.execute_script("arguments[0].click();", self.get_delivery_option())
        print("Click on the delivery option")

    def input_street_name(self, street_name):
        self.get_street().send_keys(street_name)
        print("Input a street name")

    def input_building_number(self, building_number):
        self.get_building().send_keys(building_number)
        print("Input a building number")

    def input_entrance_number(self, entrance_number):
        self.get_entrance().send_keys(entrance_number)
        print("Input a entrance number")

    def input_floor_number(self, floor_number):
        self.get_floor().send_keys(floor_number)
        print("Input a floor number")

    def input_apartment_number(self, apartment_number):
        self.get_apartment().send_keys(apartment_number)
        print("Input an apartment number")

    def click_continue_button(self):
        self.driver.execute_script("arguments[0].click();", self.get_continue_button())
        print("Click on the continue button")


    # Methods

    def choose_delivery_option_and_continue(self):
        with allure.step('Choosing delivery option and continuing'):
            Logger.add_start_step(method='choose_delivery_option_and_continue')
            self.get_current_url()
            self.assert_url('https://tomsk.znaemigraem.ru/order/')
            self.click_delivery_option()
            self.input_street_name(self.street_name_info)
            self.input_building_number(self.building_number_info)
            self.input_entrance_number(self.entrance_number_info)
            self.input_floor_number(self.floor_number_info)
            self.input_apartment_number(self.apartment_number_info)
            self.click_continue_button()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='choose_delivery_option_and_continue')











