from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        ## resolve is checking that, when called with "/" the root of the site finds a function calle home_page
        self.assertEqual(found.func, home_page)

