''' This File has been created to Test Django Installation at first '''
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest
# https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver #
# Reference
MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='./utils/chromedriver') # Using Chrome browser instead

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site.
        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc

        self.browser.quit()

        self.browser = webdriver.Chrome(executable_path='./utils/chromedriver')

        # Francis visits the home page. There is no sign of Edith's
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own uniqueURL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)


    def test_can_start_a_list_for_one_user(self):
        # User History
        # Paul has heard about a cool ne online to-do app. He goes
        # to chec out its homepage

        # LiveServer gives an attribute to get rid the http://localhost
        self.browser.get(self.live_server_url)

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
        inputbox.send_keys(Keys.ENTER)

        # "1.: Buy peacok feathers" as an item in a to-do list

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # Satisified, she goes back to sleep
        
        # There is still a text box inviting her to add another item. She enters 
        # "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Paul wonders whether the site will remember her lsit. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanoatory text to that effect.

        # He visits that URL - her to-do list is still there

        # Satisfied, she goes back to sleep

        self.fail('Finish the test!')

        