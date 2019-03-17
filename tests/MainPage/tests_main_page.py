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


#Loacators test_search_engine:
_search_engine_placeholder = "//input[@name='search']"
_submit_search_button = "//button[@class='submit-search']"
_search_value = "Test"

#Locators test_product_menu
_mouse_hover_element_products ="//div[@class='first-level-link']/a[@href='/en/products']"
_mega_nav_list = "//nav[@id='primary-nav']/div/ul/li[1]/div[@class='mega-nav']"

#Locators test_innovation_menu
_mouse_hover_innovation_menu ="//div[@class='first-level-link']/a[@href='/en/innovation']"
_innovation_menu_list = "//li[2]/div[@class='mega-nav']"

#Locators test_newsroom_menu
_mouse_hover_newsroom_menu ="//div[@class='first-level-link']/a[@href='/en/newsroom']"
_newsroom_menu_list = "//li[3]/div[@class='mega-nav']"

#Locators test_aboutus_menu
_mouse_hover_aboutus_menu ="//div[@class='first-level-link']/a[@href='/en/about-us']"
_aboutus_menu_list = "//li[5]/div[@class='mega-nav']"




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
        expected = "ADVA Optical Networking"

        self.assertEqual(title, expected, "Title is not correct")



    def test_logo_available(self):
        '''
        Test will be checking that logo is displayed.
        :return: True
        '''
        logo = self.driver.find_element(By.XPATH, _logo)
        expected = True

        if logo.is_displayed():
            result = True
        else:
            result = False

        self.assertEqual(result, expected, "Logo is not displayed on the page")


    def test_page_is_scrollable(self):
        '''
        Test will be checking that page is scrollable.
        :return: True
        '''
        self.setUpClass()
        scroll_down = self.driver.execute_script("window.scrollTo(0, 4000);")
        original_footer = self.driver.find_element(By.XPATH, _original_footer)
        expected = True

        if scroll_down:
            if original_footer:
                result = True
            else:
                result = False

            self.assertEqual(result, expected, "Page is not scrollable")



    def test_button_open_search(self):
        '''
        Test will be checking that open search button is enabled on the site.
        :return: True
        '''
        open_search_button = self.driver.find_element(By.XPATH, _open_search_button)
        expected = True

        if open_search_button.is_enabled():
            result = True
        else:
            result = False

        self.assertEqual(result, expected, "Search button is not displayed on the page")

    def test_search_engine(self):
        '''
        After clicking on the button open search, we will be inputing "test" word into search engine to checking that
        search engine is working correctly. Finally we should be on the search results card.
        :return: True
        '''
        open_search_button = self.driver.find_element(By.XPATH, _open_search_button)
        open_search_button.click()
        time.sleep(2)
        search_engine_placeholder = self.driver.find_element(By.XPATH, _search_engine_placeholder)
        search_engine_placeholder.send_keys(_search_value)
        time.sleep(2)
        submit_search_button = self.driver.find_element(By.XPATH, _submit_search_button)
        submit_search_button.click()
        time.sleep(2)
        title = self.driver.title
        expected = "Search Results"

        self.assertEqual(title, expected, "Search engine does not work")


    def test_product_menu(self):
        '''
        After mouse hovering product button menu should be visible.
        :return: True
        '''
        element = self.driver.find_element(By.XPATH, _mouse_hover_element_products)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        mega_nav_list = self.driver.find_element(By.XPATH, _mega_nav_list)
        time.sleep(1)
        expected = True

        if mega_nav_list.is_displayed():
            result = True
        else:
            result = False

        self.assertEqual(result, expected, "Product menu is not visible")


    def test_innovation_menu(self):
        '''
        After mouse hovering innovation button menu should be visible.
        :return:
        '''
        element = self.driver.find_element(By.XPATH, _mouse_hover_innovation_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        innovation_menu_list = self.driver.find_element(By.XPATH, _innovation_menu_list)
        time.sleep(1)
        expected = True

        if innovation_menu_list.is_displayed():
            result = True
        else:
            result = False

        self.assertEqual(result, expected, "Innovation menu is not visible")

    def test_newsroom_menu(self):
        '''
        After mouse hovering newsroom button menu should be visible.
        :return:
        '''
        element = self.driver.find_element(By.XPATH, _mouse_hover_newsroom_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        newsroom_menu_list = self.driver.find_element(By.XPATH, _newsroom_menu_list)
        time.sleep(1)
        expected = True

        if newsroom_menu_list.is_displayed():
            result = True
        else:
            result = False

        self.assertEqual(result, expected, "Newsroom menu is not visible")

    def test_aboutus_menu(self):
        '''
        After mouse hovering about us button menu should be visible.
        :return:
        '''
        element = self.driver.find_element(By.XPATH, _mouse_hover_aboutus_menu)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        newsroom_menu_list = self.driver.find_element(By.XPATH, _aboutus_menu_list)
        time.sleep(1)
        expected = True

        if newsroom_menu_list.is_displayed():
            result = True
        else:
            result = False

        self.assertEqual(result, expected, "AboutUs menu is not visible")

    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()