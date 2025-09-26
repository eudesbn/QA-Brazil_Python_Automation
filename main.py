import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(5)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        urban_routes_page.set_route(address_from, address_to)
        assert urban_routes_page.get_from() == address_from
        assert urban_routes_page.get_to() == address_to

    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.comfort_plan()
        assert urban_routes_page.get_current_plan() == 'Comfort'

    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        number = data.PHONE_NUMBER
        urban_routes_page.set_phone(number)
        assert urban_routes_page.get_phone() == number

    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert urban_routes_page.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        message = data.MESSAGE_FOR_DRIVER
        urban_routes_page.set_message_for_driver(message)
        assert urban_routes_page.get_message() == message

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_blanket_and_handkerchiefs_options()
        assert urban_routes_page.get_blanket_and_handkerchiefs_options_checked()

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.add_ice_creams(2)
        assert urban_routes_page.get_amount_of_ice_creams() == 2

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_order_taxi_button()
        urban_routes_page.wait_order_taxi_popup()

    def test_driver_info_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.wait_driver_info()
        name, rating, image = urban_routes_page.get_driver_info()
        assert name
        assert rating
        assert image

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()