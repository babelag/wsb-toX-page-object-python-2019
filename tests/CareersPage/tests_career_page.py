import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


#Locators test_cookie_banner
_logo = "//img[@alt='ADVA Optical Networking']"

#Locators test_filter_job_opportunities_button
_job_opportunities_button = "//section[2]//a[@href='/en/about-us/careers/job-opportunities']"


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


    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()