from BaseClass import BaseClass


class Product(BaseClass):

    def go_to_product_page(self, url):
        self.logger.info("Opening product page, URL: {}".format(url + self.LOCATION_OF_PRODUCT))
        self.browser.get(url + self.LOCATION_OF_PRODUCT)
        return self
