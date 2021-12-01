import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


class BaseClass:

    def __init__(self, browser) -> object:
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)
        self.screenshot_name = f'./screenshots/{time.strftime("%Y-%m-%d-%H:%M:%S")}-screenshot.png'

    # Main page locators:
    SEARCH_LINE = (By.CSS_SELECTOR, "[name=search]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-btn button")
    LOGO_TEXT = (By.CSS_SELECTOR, "#logo a")
    CURRENCY = (By.CSS_SELECTOR, "button .fa.fa-caret-down")
    EURO = (By.NAME, "EUR")
    POUND_STERLING = (By.NAME, "GBP")
    US_DOLLAR = (By.NAME, "USD")
    CURRENCY_SIGN = (By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle strong")
    FEATURED = (By.CSS_SELECTOR, "#content h3")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price")
    PRODUCT_THUMBS = (By.CSS_SELECTOR, ".product-thumb")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    SHOPPING_CART_ALERT = (By.CSS_SELECTOR, "p.text-center")
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, ".button-group i.fa")
    SUCCESS_OR_DISMISS_ALERT = (By.CSS_SELECTOR, ".alert")
    MY_ACCOUNT_CARET = (By.CSS_SELECTOR, ".caret")
    REGISTER = (By.LINK_TEXT, "Register")
    LOGIN = (By.LINK_TEXT, "Login")
    # Catalog page locators:
    LOCATION_OF_CATALOG = "laptop-notebook/"
    LAPTOPS_NOTEBOOKS = (By.CSS_SELECTOR, "#content h2")
    LINK_WINDOWS = (By.PARTIAL_LINK_TEXT, "Windows")
    ADD_TO_CART = (By.CSS_SELECTOR, ".button-group .fa.fa-shopping-cart")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    COMPARE_PRODUCT = (By.XPATH, "//*[@class='button-group']/button[@data-original-title='Compare this Product']")
    PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, "#compare-total")
    # Product page locators:
    LOCATION_OF_PRODUCT = "mp3-players/ipod-classic"
    THUMBNAILS = (By.CSS_SELECTOR, ".image-additional .thumbnail")
    TAB_CONTENT = (By.CSS_SELECTOR, ".tab-content")
    PRICE = (By.XPATH, "//*[@class='list-unstyled']/li/h2")
    # User login page locators:
    LOGIN_PAGE = "index.php?route=account/login"
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".well .btn.btn-primary")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value=Login]")
    WARNING_ALERT = (By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    INPUT_PASSWORD = (By.NAME, "password")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.NAME, "agree")
    SUBMIT_CONTINUE_BUTTON = (By.CSS_SELECTOR, ".pull-right .btn.btn-primary")
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, "#content h1")
    # Admin's login page
    ADM_LOGIN_PAGE_LOCATION = '/admin/'
    ADM_LOGIN_BUTTON = (By.CSS_SELECTOR, ".text-right button")
    INPUT_ADMIN_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_ADMIN_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    # Admin page locators:
    AUTORIZED_USER = (By.CSS_SELECTOR, "li.dropdown")
    CATALOG = (By.LINK_TEXT, "Catalog")
    PRODUCTS = (By.LINK_TEXT, "Products")
    # ADD new product button and SAVE button locators
    ADD_NEW = (By.CSS_SELECTOR, '.fa.fa-plus')
    SAVE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-danger")

    # Tab DATA locator
    DATA_TAB = (By.LINK_TEXT, "Data")
    # Locators of required fields of product properties
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
    MODEL_FIELD = (By.CSS_SELECTOR, '#input-model')
    # Локаторы необязательных полей (для наглядности)
    PRICE_FIELD = (By.CSS_SELECTOR, '#input-price')
    # Checkboxes
    CHECKBOX = (By.NAME, "selected[]")

    def find_web_element(self, locator):
        """
        Метод принимает в качестве аргумента локатор веб-элемента.
        Локатором веб-элемента является кортеж вида:
            (<атрибут класса By>, <селектор веб-элемента>)
        Метод производит поиск веб-элемента на странице по указанному локатору.
        Метод возвращает:
            веб-элемент, в случае его обнаружения на веб-странице;
            AssertionError, если веб-элемент не обнаружен на веб-странице.

        """
        self.logger.info('Searching element: \'{} = {}\''.format(*locator))
        try:
            el = self.browser.find_element(*locator)
        except NoSuchElementException as no_elem:
            self.logger.error("Element \'{} = {}\' was not found on the page".format(*locator))
            self.browser.save_screenshot(self.screenshot_name)
            raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")
        else:
            self.logger.info('Element \'{} = {}\' was found'.format(*locator))
            return el

    def wait_web_element(self, locator, timeout=2):
        self.logger.info('Waiting for the element {} within {} seconds'.format(locator, timeout))
        try:
            el = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as time_is_up:
            self.logger.error("Element \'{} = {}\' was not found on the page".format(*locator))
            self.browser.save_screenshot(self.screenshot_name)
            raise AssertionError(time_is_up, "Время ожидания элемента \'{} = {}\' истекло".format(*locator))
        return el

    def find_all_specified_elements(self, locator):
        self.logger.info('Searching for several elements with locator: \'{} = {}\''.format(*locator))
        return self.browser.find_elements(*locator)


class LoginOnAdminPage(BaseClass):

    # ADM_LOGIN_PAGE_LOCATION = '/admin/'
    # LOGIN_BUTTON = (By.CSS_SELECTOR, ".text-right button")
    # INPUT_ADMIN_USERNAME = (By.CSS_SELECTOR, "#input-username")
    # INPUT_ADMIN_PASSWORD = (By.CSS_SELECTOR, '#input-password')

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger('Admin\'s_autorization')

    def go_to(self, url):
        self.logger.info("Going to the {}".format(url))
        self.browser.get(url + self.ADM_LOGIN_PAGE_LOCATION)

    def enter_username(self, username):
        self.logger.info("Enter \'{}\' in the \'Username\' field".format(username))
        username_field = self.browser.find_element(*self.INPUT_ADMIN_USERNAME)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        self.logger.info("Enter \'{}\' in the \'Password\' field".format(password))
        pwd_field = self.browser.find_element(*self.INPUT_ADMIN_PASSWORD)
        pwd_field.clear()
        pwd_field.send_keys(password)

    def submit(self):
        self.logger.info("Clicking on the SUBMIT button")
        self.browser.find_element(*self.ADM_LOGIN_BUTTON).click()

    def submit_with_ENTER(self):
        self.logger.info("Pushing the ENTER button on the keyboard")
        self.browser.find_element(*self.ADM_LOGIN_BUTTON).send_keys(Keys.ENTER)

    def log_in(self, url, username, password):
        self.go_to(url)
        self.enter_username(username)
        self.enter_password(password)
        self.submit_with_ENTER()
