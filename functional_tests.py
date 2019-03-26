''' This File has been created to Test Django Installation at first '''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver #
# Reference

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='./utils/chromedriver') # Using Chrome browser instead

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User History
        # Paul has heard about a cool ne online to-do app. He goes
        # to chec out its homepage

        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        # This is to check if the basic django server is upexit
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # He types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        # When She hits enter, the page updates, and now the page lists

        # "1.: Buy peacok feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
                
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        # There is still a text box inviting her to add another item. She enters 
        # "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Paul wonders whether the site will remember her lsit. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanoatory text to that effect.

        # He visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore') # Launches the unittest test runner, which will automatically find test classes and methods