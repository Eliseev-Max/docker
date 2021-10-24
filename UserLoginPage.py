import random
from BaseClass import BaseClass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from AdminPage import AdminPage as AP


class UserLoginPage(BaseClass):

    def go_to_login_page(self, url):
        self.logger.info("Opening source: {}".format(url + self.LOGIN_PAGE))
        self.browser.get(url + self.LOGIN_PAGE)
        return self

    def go_to_account_reg_page(self, url):
        self.go_to_login_page(url)
        self.logger.info("Clicking on the CONTINUE button")
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CONTINUE_BUTTON)).click()
        return self

    def check_element_appears_after_click(self, clickable_elem, expected_elem):
        self.find_web_element(clickable_elem).click()
        self.wait_web_element(expected_elem)

    @staticmethod
    def generate_name():
        ABC = "abcdefghijklmnopqrstuvwxyz"
        return "".join(random.sample(ABC, random.randint(5, 10))).capitalize()

    @staticmethod
    def generate_email():
        return f"{AP.random_string_generator()}@test.com"

    def find_and_fill_the_field(self, web_element_field, text):
        web_element_field.clear()
        self.logger.info("Filling the field with text: {}".format(text))
        web_element_field.send_keys(text)

    def enter_first_and_last_name(self):
        self.logger.info("Filling fields \"First Name\" and \"Last Name\"")
        first_name = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        last_name = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        self.find_and_fill_the_field(first_name, self.generate_name())
        self.find_and_fill_the_field(last_name, self.generate_name())

    def enter_email(self):
        self.logger.info("Entering email")
        email_field = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        self.find_and_fill_the_field(email_field, self.generate_email())

    def enter_telephone(self):
        self.logger.info("Entering phone number")
        telephone_field = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.TELEPHONE_FIELD))
        phone_number = "+71234567890"
        self.find_and_fill_the_field(telephone_field, phone_number)

    def enter_and_confirm_password(self):
        self.logger.info("Entering and confirming password")
        password = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        confirm_pwd = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PASSWORD_CONFIRM_FIELD))
        generated_pwd = AP.random_string_generator()
        self.find_and_fill_the_field(password, generated_pwd)
        self.find_and_fill_the_field(confirm_pwd, generated_pwd)

    def enter_all_fields(self):
        self.enter_first_and_last_name()
        self.enter_email()
        self.enter_telephone()
        self.enter_and_confirm_password()

    def wait_and_click(self, clickable_element, timeout=2):
        self.logger.info("Clicking on the element \'{} = {}\'".format(*clickable_element))
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(clickable_element)).click()

    def view_success_notification(self):
        notification = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SUCCESS_NOTIFICATION))
        return notification.text
