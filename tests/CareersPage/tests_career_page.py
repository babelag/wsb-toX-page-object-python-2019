import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


#Locators test_cookie_banner
_logo = "//img[@alt='ADVA Optical Networking']"

#Locators test_filter_job_opportunities_button
_job_opportunities_button = "//section[2]//a[@href='/en/about-us/careers/job-opportunities']"

#Locators test_page__is_scrollable
_sitemap_button = "//footer[@id='site-footer']/section/nav[2]/ul/li[1]/a[2]"

#Locators test_switch_to_youtube
_youtube_button = "//footer[@id='site-footer']/section/div/ul//img[@alt='youtube']"
_youtube_logo = "/html//div[@id='logo-icon-container']"

#Locators test_switch_to_facebook
_facebook_button = "//footer[@id='site-footer']/section/div/ul//img[@alt='facebook']"
_facebook_logo = "//html[@id='facebook']//div[@id='blueBarDOMInspector']//div[@role='heading']"

#Locators test_search_job_opportunities
_all_departments = "//div[@id='main']/section[2]/div/section[2]/div/div[1]/div[@class='stylish-select']"
_research_and_development = "//div[@id='main']/section[2]/div/section[2]/div/div[1]/div/div[@role='listbox']/div/div[35]"
_all_countries = "//div[@id='main']/section[2]/div/section[2]/div/div[2]/div[@class='stylish-select']"
_USA = "//div[@id='main']/section[2]/div/section[2]/div/div[2]/div/div[@role='listbox']/div/div[13]"
_all_languages = "//div[@id='main']/section[2]/div/section[2]/div/div[3]/div[@class='stylish-select']"
_English = "//div[@id='main']/section[2]/div/section[2]/div/div[3]/div/div[@role='listbox']/div/div[2]"
_hardware_engineer = "//div[@id='main']"


class CareerPageTestsAdvaOptical(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        baseURL = "https://www.advaoptical.com/en/about-us/careers"
        self.driver = webdriver.Chrome(executable_path='C:\\TestFiles\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)

    def test_page_title(self):
        '''
        Test will be checking correct site title.
        :return: Careers
        '''
        title = self.driver.title
        expected = "Careers"
        self.driver.save_screenshot("../screenshots/sd.png")

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

    def test_filter_job_opportunities_button(self):
        '''
        Test will be checking that open search button is enabled on the site.
        :return: True
        '''
        job_opportunities_button = self.driver.find_element(By.XPATH, _job_opportunities_button)
        expected = True

        if job_opportunities_button.is_enabled():
            result = True
        else:
            result = False

        self.assertEqual(result, expected, "Job opportunities button is not displayed on the page")

    def test_page_is_scrollable(self):
        '''
        Test will be checking that page career is scrollable.
        :return: True
        '''
        self.setUpClass()
        scroll_down = self.driver.execute_script("window.scrollTo(0, 4000);")
        sleep(3)
        sitemap_button = self.driver.find_element(By.XPATH, _sitemap_button)
        expected = True

        if scroll_down:
            if sitemap_button:
                result = True
            else:
                result = False

            self.assertEqual(result, expected, "Page Careers is not scrollable")

    def test_switch_to_youtube(self):
        '''
        Test will be checking switch to youtube site.
        :return: True
        '''
        self.setUpClass()
        scroll_down = self.driver.execute_script("window.scrollTo(0, 4000);")
        sleep(3)
        youtube_button = self.driver.find_element(By.XPATH, _youtube_button)
        youtube_button.click()
        sleep(2)
        youtube_logo = self.driver.find_element(By.XPATH, _youtube_logo)
        expected = True

        if scroll_down:
            if youtube_logo:
                result = True
            else:
                result = False

            self.assertEqual(result, expected, "Youtube button does not work")

    def test_switch_to_facebook(self):
        '''
        Test will be checking switch to facebook site.
        :return: True
        '''
        self.setUpClass()
        scroll_down = self.driver.execute_script("window.scrollTo(0, 4000);")
        sleep(3)
        facebook_button = self.driver.find_element(By.XPATH, _facebook_button)
        facebook_button.click()
        sleep(2)
        facebook_logo = self.driver.find_element(By.XPATH, _facebook_logo)
        expected = True
        self.driver.save_screenshot("random.png")

        if scroll_down:
            if facebook_logo:
                result = True
            else:
                result = False

            self.assertEqual(result, expected, "Facebook button does not work")

    def test_search_job_opportunities(self):

        '''
        Test will be checking filter job opportunities
        :return: True
        '''
        job_opportunities_button = self.driver.find_element(By.XPATH, _job_opportunities_button)
        job_opportunities_button.click()
        all_departments = self.driver.find_element(By.XPATH, _all_departments)
        all_departments.click()
        research_and_development = self.driver.find_element(By.XPATH, _research_and_development)
        research_and_development.click()
        sleep(2)
        all_countries = self.driver.find_element(By.XPATH, _all_countries)
        all_countries.click()
        sleep(2)
        USA = self.driver.find_element(By.XPATH, _USA)
        USA.click()
        sleep(2)
        all_languages = self.driver.find_element(By.XPATH, _all_languages)
        all_languages.click()
        sleep(2)
        english = self.driver.find_element(By.XPATH, _English)
        english.click()
        sleep(2)
        hardware_engineer = self.driver.find_element(By.XPATH, _hardware_engineer)
        expected = True

        if hardware_engineer:
            result = True
        else:
            result = False

        self.driver.save_screenshot("Screenshots\\random.png")


        self.assertEqual(result, expected, "Filter job opportunities does not work")


    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()