import os
from datetime import datetime
import json


class Base():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, f"Error. Expected {result} but got {value_word}"
        print("Right value word")

    """Method Screenshot"""
    def screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        self.driver.save_screenshot(f'C://Users//apach//PycharmProjects//ZnaemIgraem//screens//screenshot_{now_date}.png')

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, f"Error. Expected {result} but got {get_url}"
        print("Right url")

    """Method for getting credentials"""
    @staticmethod
    def get_credentials():
        with open(f'{os.getcwd()}\\tests\\config.json', 'r') as config_file:
            config = json.load(config_file)
            test_login = config['login']
            test_password = config['password']
            return test_login, test_password

    """Method for checking price from different pages"""
    def assert_price(self, price_1, price_2):
        assert price_1 == price_2
        print("Price isn't changed")


    """Method for checking product title from different pages"""
    def assert_title(self, title_1, title_2):
        assert title_1 == title_2
        print("Tile isn't changed")




