import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from utilities.logger import Logger

faker = Faker("ru_RU")

class ClientInfoPage(Base):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.action = ActionChains(self.driver)
        self.full_name_info = faker.name()
        self.email_info= faker.email()
        self.phone_number_info = faker.phone_number()


    # Locators

    continue_button_2 = "(//button[@class='v-btn--full btn btn-primary'])[1]"
    full_name = "//input[@name='ORDER_PROP_1']"
    email = "//input[@name='ORDER_PROP_2']"
    phone_number = "//input[@name='ORDER_PROP_3']"

    # Getters

    def get_continue_button_2(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_button_2)))

    def get_full_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.full_name)))

    def get_email(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone_number(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))


    # Actions

    def click_continue_button_2(self):
        self.driver.execute_script("arguments[0].click();", self.get_continue_button_2())
        print("Click on the continue button 2")

    def input_full_name(self, full_name):
        self.get_full_name().send_keys(full_name)
        print("Input a full_name")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input an email")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input a phone_number")


    # Methods

    def fill_client_detail_for_unauthorized_user(self):
        with allure.step('Filling client information for an unauthorized user'):
            Logger.add_start_step(method='fill_client_detail_for_unauthorized_user')
            self.click_continue_button_2()
            time.sleep(5)
            self.get_current_url()
            self.input_full_name(self.full_name_info)
            self.input_email(self.email_info)
            self.input_phone_number(self.phone_number_info)
            self.screenshot()
            print("Test has finished. Please check the screenshot")
            Logger.add_end_step(url=self.driver.current_url, method='fill_client_detail_for_unauthorized_user')


    def fill_client_detail_for_authorized_user(self):
        with allure.step('Filling client information for an authorized user'):
            Logger.add_start_step(method='fill_client_detail_for_authorized_user')
            self.click_continue_button_2()
            time.sleep(5)
            self.get_current_url()
            self.input_phone_number(self.phone_number_info)
            self.screenshot()
            print("Test has finished. Please check the screenshot")
            Logger.add_end_step(url=self.driver.current_url, method='fill_client_detail_for_authorized_user')









