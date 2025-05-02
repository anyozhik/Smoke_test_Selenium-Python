from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.order_page import OrderPage
from pages.client_info_page import ClientInfoPage
import allure

@allure.description("A smoke test for buying a product without authorization")
def test_buy_product(set_up):
    driver, wait = set_up
    driver.get('https://tomsk.znaemigraem.ru/catalog/boardgames/igra-po-tematike/family/')
    driver.maximize_window()

    mp = MainPage(driver, wait)
    mp.select_product()

    bp = BasketPage(driver, wait)
    bp.check_basket_info_and_continue()

    op = OrderPage(driver, wait)
    op.choose_delivery_option_and_continue()

    cip = ClientInfoPage(driver, wait)
    cip.fill_client_detail_for_unauthorized_user()

