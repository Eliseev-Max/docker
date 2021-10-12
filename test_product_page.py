import allure
from Product import Product


@allure.title("Поиск элементов на странице карточки товара")
@allure.description("Ищем на странице продукта /mp3-players/ipod-classic/"
                    "следующие веб-элементы:\n{}\n{}".format(Product.TAB_CONTENT,
                                                             Product.PRICE))
def test_find_elements_on_product_page(browser, base_url):
    prod = Product(browser)
    prod.go_to_product_page(base_url)
    prod.find_web_element(Product.TAB_CONTENT)
    prod.find_web_element(Product.PRICE)


@allure.title("Проверка количества миниатюр изображения товара")
@allure.description("Проверяем, что количество миниатюр продуктов на странице равно 3")
def test_number_of_thumbnails(browser, base_url):
    prod = Product(browser)
    prod.go_to_product_page(base_url)
    if len(prod.find_all_specified_elements(Product.THUMBNAILS)) != 3:
        browser.save_screenshot(prod.screenshot_name)
        prod.logger.error("Number of product thumbs is not 3")
        raise AssertionError
