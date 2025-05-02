from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger
import allure


class LoginPage(Base):

    url = 'https://tomsk.znaemigraem.ru/catalog/boardgames/igra-po-tematike/family/'

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.test_login, self.test_password = self.get_credentials()

    # Locators

    login_icon = "(//span[contains(text(),'Войти')])[1]"
    user_name = "(//input[@class='form__input' and @name='USER_LOGIN'])[1]"
    password = "(//input[@class='form__input' and @name='USER_PASSWORD'])[1]"
    login_button = "(//button[@name='Login'])[1]"
    check_span = "(//span[contains(text(),'Анна')])[1]"


    # Getters

    def get_login_icon(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_icon)))

    def get_user_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_check_span(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.check_span)))


    # Actions

    def click_login_icon(self):
        self.get_login_icon().click()
        print("Click on the login icon")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click on the login button")

    # Methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method = 'authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_login_icon()
            self.input_user_name(self.test_login)
            self.input_password(self.test_password)
            self.click_login_button()
            self.assert_word(self.get_check_span(), "Анна")
            Logger.add_end_step(url= self.driver.current_url, method = 'authorization')

