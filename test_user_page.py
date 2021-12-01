import allure
from Pages.UserLoginPage import UserLoginPage


@allure.title("Проверка наличия веб-элементов на странице авторизации пользователя")
@allure.description("Проверяем наличие элементов, соответствующих кнопке Continue"
                    "и полю ввода пароля на странице авторизации пользователя")
def test_find_continue_btn_on_login_page(browser, base_url):
    user_login_page = UserLoginPage(browser)
    user_login_page.go_to_login_page(base_url)
    user_login_page.find_web_element(user_login_page.CONTINUE_BUTTON)
    user_login_page.find_web_element(user_login_page.INPUT_PASSWORD)


@allure.title("Проверка появления сообщения об ошибке при отправке незаполненной формы")
@allure.description("Проверяем появление сообщения об ошибке после нажатии кнопки Login без заполнения полей "
                    "\"E-Mail Address\" и \"Password\"")
def test_click_Login_without_filling_fields(browser, base_url):
    user_login_page = UserLoginPage(browser)
    user_login_page.go_to_login_page(base_url)
    user_login_page.check_element_appears_after_click(user_login_page.LOGIN_BUTTON, user_login_page.WARNING_ALERT)


@allure.title("Создание нового пользователя")
@allure.description("Позитивный тест создания нового пользователя."
                    "По завершении теста должна появиться надпись \"Your Account Has Been Created!\"")
def test_create_new_user(browser, base_url):
    new_user = UserLoginPage(browser)
    new_user.go_to_account_reg_page(base_url)
    new_user.enter_first_and_last_name()
    new_user.enter_all_fields()
    new_user.wait_and_click(new_user.PRIVACY_POLICY_CHECKBOX)
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    if new_user.view_success_notification() != "Your Account Has Been Created!":
        browser.save_screenshot(new_user.screenshot_name)
        new_user.logger.error("Account creation message was not displayed ")
        raise AssertionError
