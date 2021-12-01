# -*-coding: utf-8-*-

import time
import allure
from Pages.MainPage import MainPage

CURRENCY = dict({"USD": "$", "EUR": "€", "GBP": "£"})
CURRENCY_LIST = list(CURRENCY.keys())


@allure.title("Поиск веб-элементов на главной странице")
@allure.description("Ищем на странице каталога /laptop-notebook/ "
                    "следующие веб-элементы:\n{}\n{}\n{}".format(
                                                                 MainPage.FEATURED,
                                                                 MainPage.LOGO_TEXT,
                                                                 MainPage.SEARCH_LINE))
def test_find_elements_on_main_page(browser, base_url):
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)
    main_page.find_web_element(MainPage.FEATURED)
    main_page.find_web_element(MainPage.LOGO_TEXT)
    main_page.find_web_element(MainPage.SEARCH_LINE)


@allure.title("Проверка количества превью продуктов на странице")
@allure.description("Проверяем, что количество превью продуктов на странице равно 4")
def test_number_of_product_thumbs(browser, base_url):
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)

    if len(main_page.find_all_specified_elements(MainPage.PRODUCT_THUMBS)) != 4:
        browser.save_screenshot(main_page.screenshot_name)
        main_page.logger.error("Number of product thumbs is not 4")
        raise AssertionError


@allure.title("Проверка смены знака валюты у товаров")
def test_check_sign_with_changing_currency(browser, base_url):
    """ Проверяем смену знака валюты у товаров при смене валюты в хедере главной страницы """
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)
    for cur in CURRENCY_LIST:
        main_page.choose_currency(cur)

        if main_page.find_web_element(main_page.CURRENCY_SIGN).text != CURRENCY[cur]:
            main_page.find_web_element(main_page.CURRENCY_SIGN).screenshot("./screenshot/currency_sign.png")
            browser.save_screenshot(main_page.screenshot_name)
            main_page.logger.error("The currency sign in the prices of products does not match the selected one")
            raise AssertionError
        time.sleep(1)


@allure.title("Проверка смены денежного выражения цены товаров при смене валюты")
def test_currency_of_product_price(browser, base_url):
    """ Проверяем смену денежного выражения цены избранных товаров при смене валюты """
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)
    for cur in CURRENCY_LIST:
        main_page.choose_currency(cur)
        prod_list = main_page.find_all_specified_elements(MainPage.PRODUCT_PRICE)
        for price in prod_list:
            assert CURRENCY[cur] in price.text
        time.sleep(1)
