import unittest

from tests.MainPage.tests_main_page import MainPageTestsAdvaOptical as MainPage
from tests.CareersPage.tests_career_page import CareerPageTestsAdvaOptical as Career
from tests.ContactPage.tests_contact_page import ContactPageTestsAdvaOptical as Contact


class AllTest(unittest.TestCase):

    def test_main_page(self):
        MainPage()
        Career()
        Contact()

if __name__ == '__main__':
    unittest.main()
