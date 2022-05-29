import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.get('https://www.mercadolibre.com.ar/')
        driver.maximize_window()
        # driver.implicitly_wait(15)

    def test_search_test_field_by_id(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_test_field_by_name(self):
        search_field = self.driver.find_elements_by_class_name('imput-text')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
