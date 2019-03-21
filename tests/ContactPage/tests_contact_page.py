import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Locators test cookie banner
_logo = "//div[@id='logo']//img[@alt='ADVA Optical Networking']"

#Locators test_pagecontact_is_scrollable
_imprint_footer = "//footer[@id='site-footer']/section/nav/ul//a[@href='/en/about-us/legal/imprint']"

#Locators test_sending_the_form
_department = "//div[@id='main']/form/fieldset/div[3]//span[@class='text']"
_event = "//div[@id='main']/form/fieldset/div[3]//div[@role='listbox']/div/div[3]"
_first_name = "/html//input[@id='first-name']"
_last_name = "/html//input[@id='last-name']"
_company = "/html//input[@id='company-name']"
_country = "//div[@id='main']/form/fieldset/div[7]//div[@class='stylish-select']/span"
_poland = "//div[@id='main']/form/fieldset/div[7]//div[@role='listbox']/div/div[178]"
_email = "/html//input[@id='email-name']"
_telephone = "/html//input[@id='tel-number']"
_comment = "/html//textarea[@id='comments']"
_sumbit = "//div[@id='main']/form//button[@type='submit']"
_message_sent = "//body/div[3]/div[@class='mod-lightbox']"

#Input values test_sending_the_form
_input_first_name = "Czesław"
_input_last_name = "Kowalski"
_input_company = "Lotos"
_input_email = "czesiu@o2.pl"
_input_telephone = "203203020"
_input_comment = "It is testing message"



#Locators test_search_regional_office
_location = "//div[@id='main']/section[2]/div/section//div[@class='stylish-select']/span"
_italy = "//div[@id='main']/section[2]/div/section/div/div/div/div[@role='listbox']/div/div[10]"
_number = "//div[@id='main']/section[2]//ul[@class='results']//a[@href='tel:+39 06 8676 1027']"


class ContactPageTestsAdvaOptical(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        baseURL = "https://www.advaoptical.com/en/about-us/contact"
        self.driver = webdriver.Chrome(executable_path='C:\\TestFiles\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)

    def test_page_title(self):
        '''
        Test will be checking correct site title.
        :return: Contact
        '''
        title = self.driver.title
        expected = "Contact"

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

    def test_page_contact_is_scrollable(self):
        '''
        Test will be checking that page contact is scrollable.
        :return: True
        '''
        self.setUpClass()
        scroll_down = self.driver.execute_script("window.scrollTo(0, 4000);")
        sleep(3)
        imprint_footer = self.driver.find_element(By.XPATH, _imprint_footer)
        expected = True

        if scroll_down:
            if imprint_footer:
                result = True
            else:
                result = False

            self.assertEqual(result, expected, "Page Contact is not scrollable")

    def test_send_the_form(self):
        '''
        Test will be checking send message to company.
        :return: True
        '''
        department = self.driver.find_element(By.XPATH, _department)
        department.click()
        event = self.driver.find_element(By.XPATH, _event)
        event.click()
        first_name = self.driver.find_element(By.XPATH, _first_name)
        first_name.send_keys(_input_first_name)
        last_name = self.driver.find_element(By.XPATH, _last_name)
        last_name.send_keys(_input_last_name)
        company = self.driver.find_element(By.XPATH, _company)
        company.send_keys(_input_company)
        country = self.driver.find_element(By.XPATH, _country)
        country.click()
        poland = self.driver.find_element(By.XPATH, _poland)
        poland.click()
        email = self.driver.find_element(By.XPATH, _email)
        email.send_keys(_input_email)
        telephone = self.driver.find_element(By.XPATH, _telephone)
        telephone.send_keys(_input_telephone)
        comment = self.driver.find_element(By.XPATH, _comment)
        comment.send_keys(_input_comment)
        sumbit = self.driver.find_element(By.XPATH, _sumbit)
        sumbit.click()
        sleep(10)
        message_sent = self.driver.find_element(By.XPATH, _message_sent)
        expected = True

        if message_sent:
            result = True
        else:
            result = False

        self.assertEqual(result, expected, 'Send message does not work')

    def test_search_regional_office(self):
        '''
        Test will be checking search regional detail office
        :return:
        '''
        scroll_down = self.driver.execute_script("window.scrollTo(0, 4000);")
        sleep(2)
        location = self.driver.find_element(By.XPATH, _location)
        location.click()
        italy = self.driver.find_element(By.XPATH, _italy)
        italy.click()
        sleep(2)
        number = self.driver.find_element(By.XPATH, _number)
        expected = True

        if scroll_down:
            if number:
                result = True
            else:
                result = False

            self.assertEqual(result, expected, 'Search regional office does not work')



    @classmethod
    def tearDownClass(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()