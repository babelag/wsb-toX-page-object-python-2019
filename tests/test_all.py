import unittest

from tests.MainPage.tests_main_page import MainPageTestsAdvaOptical as MainPage
from tests.CareersPage.tests_career_page import CareerPageTestsAdvaOptical as Career


class AllTest(unittest.TestCase):

    def test_main_page(self):
        MainPage()
        Career()


if __name__ == '__main__':
    unittest.main()
