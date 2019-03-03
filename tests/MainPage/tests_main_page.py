import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#Locators test_cookie_banner
_accept_button = "//body/section//button[1]"
_cookie_banner ="//body/section/div[@class='wrapper-2000']"

#Locators test_cookie_banner
_logo = "//img[@alt='ADVA Optical Networking']"

#Locators test_page_is_scrollable
_original_footer = "//li[.='© 2019 ADVA Optical Networking']"

#Locators test_button_open_search
_open_search_button = "//div[@class='search-container']/button[1]"


#Locators test_product_list_mega_nav
_mouse_hover_element_products ="//div[@class='first-level-link']/a[@href='/en/products']"
_mega_nav_list = "//nav[@id='primary-nav']/div/ul/li[1]/div[@class='mega-nav']"


class MainPageTestsAdvaOptical(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        baseURL = "https://www.advaoptical.com/en"
        self.driver = webdriver.Chrome(executable_path='C:\\TestFiles\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)

    def test_cookie_banner(self):
        '''
        This test will be checking that after cookie accepted banner won't be available.
        :return: True
        '''
        accept_button = self.driver.find_element(By.XPATH, _accept_button)
        cookie_banner = self.driver.find_element(By.XPATH, _cookie_banner)
        accept_button.click()
        time.sleep(2)

        if not cookie_banner.is_displayed():
            result = True
        else:
            result = False

        self.assertEqual(result, True, "Cookie banner is visible")


    def test_page_title(self):
        '''
        Test will be checking correct site title.
        :return: ADVA Optical Networking
        '''
        title = self.driver.title
        expected_title = "ADVA Optical Networking"

        self.assertEqual(title, expected_title, "Title is not correct")



    def test_logo_available(self):
        '''
        Test will be checking that logo is displayed.
        :return: True
        '''
        logo = self.driver.find_element(By.XPATH, _logo)

        if logo.is_displayed():
            result = True
        else:
            result = False

        self.assertEqual(result, True, "Logo is not displayed on the page")


    # def test_page_is_scrollable(self): DO ZROBIENIAAAAAAAAAAAAAAAAAA
    #     '''
    #     Test will be checking that page is scrollable.
    #     :return: True
    #     '''
    #     # self.setUpClass()
    #     scroll_down = self.driver.execute_script("window.scrollTo(0, 4000);")
    #     original_footer = self.driver.find_element(By.XPATH, _original_footer)
    #     expected = original_footer.is_enabled()
    #
    #     if scroll_down:
    #         time.sleep(5)
    #         result = original_footer.is_enabled()
    #     else:
    #         result = not original_footer.is_enabled()
    #
    #     time.sleep(5)
    #
    #     self.assertEqual(result, expected, "Page is not scrollable")


    def test_button_open_search(self):
        '''
        Test will be checking that open search button is enabled on the site.
        :return: True
        '''
        open_search_button = self.driver.find_element(By.XPATH, _open_search_button)

        if open_search_button.is_enabled():
            result = True
        else:
            result = False

        self.assertEqual(result, True, "Search button is not displayed on the page")

    # def test_search_engine(self):
    #     '''
    #     After clicking on the button open search, we will be inputing "test" word into search engine to checking that
    #     search engine is working correctly.
    #     :return: True
    #     '''
    #     pass

    def test_product_menu(self):
        '''
        After mouse hovering product button menu should be visible.
        :return: True
        '''
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, _mouse_hover_element_products)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        mega_nav_list = self.driver.find_element(By.XPATH, _mega_nav_list)

        if mega_nav_list.is_displayed():
            message = True
        else:
            message = False

        self.assertEqual(message, True, "Mega Nav is working correctly")
    #
    #
    # def test_innovation_menu(self):
    #     '''
    #     After mouse hovering innovation button menu should be visible.
    #     :return:
    #     '''
    #     pass
    #
    # def test_newsroom_menu(self):
    #     '''
    #     After mouse hovering newsroom button menu should be visible.
    #     :return:
    #     '''
    #     pass
    #
    # def test_aboutUs_menu(self):
    #     '''
    #     After mouse hovering about us button menu should be visible.
    #     :return:
    #     '''
    #     pass

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()