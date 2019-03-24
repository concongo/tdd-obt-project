''' This File has been created to Test Django Installation at first '''
from selenium import webdriver
import unittest
# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver #
# Reference

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='./utils/chromedriver') # Using Chrome browser instead

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User History
        # Paul has heard about a cool ne online to-do app. He goes
        # to chec out its homepage

        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        # This is to check if the basic django server is upexit
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


        # He is invited to enter a to-do item straight away

        # He types "Buy peacock feathers" into a text box

        # When She hits enter, the page updates, and now the page lists

        # "1.: Buy peacok feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She enters 
        # "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Paul wonders whether the site will remember her lsit. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanoatory text to that effect.

        # He visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore') # Launches the unittest test runner, which will automatically find test classes and methods