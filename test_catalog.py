import random
import allure
from Catalog import Catalog


@allure.title("Поиск веб-элементов на странице каталога Laptops&Notebooks")
@allure.description("Ищем на странице каталога /laptop-notebook/"
                    "следующие веб-элементы:"
                    "\n{}\n{}\n{}\n{}".format(Catalog.LAPTOPS_NOTEBOOKS,
                                              Catalog.LINK_WINDOWS,
                                              Catalog.CART_TOTAL,
                                              Catalog.PRODUCT_COMPARE_LINK))
def test_find_elements_in_catalog(browser, base_url):
    cat = Catalog(browser)
    cat.go_to_catalog(base_url)
    cat.find_web_element(cat.LAPTOPS_NOTEBOOKS)
    cat.find_web_element(cat.LINK_WINDOWS)
    cat.find_web_element(cat.CART_TOTAL)
    cat.find_web_element(cat.PRODUCT_COMPARE_LINK)


@allure.title("Добавление товара в корзину")
def test_add_to_cart(browser, base_url):
    """ Проверяем добавление товара в корзину """
    cat = Catalog(browser)
    cat.go_to_catalog(base_url)
    all_buttons_to_add = cat.find_all_specified_elements(cat.ADD_TO_CART)
    random.choice(all_buttons_to_add).click()
    cat.wait_web_element(cat.ALERT_SUCCESS, timeout=3)


@allure.title("Добавление товара к сравнению")
def test_add_to_comparation(browser, base_url):
    """ Проверяем добавление товара к сравнению """
    cat = Catalog(browser)
    cat.go_to_catalog(base_url)
    all_buttons_to_compare = cat.find_all_specified_elements(cat.COMPARE_PRODUCT)
    random.choice(all_buttons_to_compare).click()
    cat.wait_web_element(cat.ALERT_SUCCESS)

    if cat.wait_web_element(cat.PRODUCT_COMPARE_LINK).text != "Product Compare (1)":
        cat.logger.error("The value: \"Product Compare ()\" has not increased")
        browser.save_screenshot(cat.screenshot_name)
        raise AssertionError
