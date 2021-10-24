import BaseClass


class Catalog(BaseClass.BaseClass):

    def go_to_catalog(self, url):
        self.logger.info("Opening source: {}".format(url + self.LOCATION_OF_CATALOG))
        self.browser.get(url + self.LOCATION_OF_CATALOG)
        return self
