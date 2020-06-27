from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from django.urls import resolve,reverse
import time
import unittest
from django.contrib.auth.models import User

class NewVisitorTest(StaticLiveServerTestCase):  

    port=8888

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(NewVisitorTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(NewVisitorTest, cls).tearDownClass()

    def setUp(self):
        super().setUp()
        User.objects.create_superuser(username="admin", password="admin", email='')

    def build_absolute_url(self, relative_url):
        if not relative_url.startswith('/'):
            relative_url = reverse(relative_url)
        return '%s%s' % (self.live_server_url, relative_url)

    def test_browse_to_page(self):
        # Browse to the login page
        self.selenium.get(self.build_absolute_url('/admin/login/?next=/'))
        time.sleep(1)

        # Fill out input
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('admin')
        time.sleep(1)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('admin')
        time.sleep(1)

        # Log in
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        time.sleep(1)

        # Browse to new post
        self.selenium.get(self.build_absolute_url('cv_new'))
        time.sleep(1)

        # Fill out input
        title_input = self.selenium.find_element_by_name("title")
        title_input.send_keys('My CV')
        time.sleep(1)

        text_input = self.selenium.find_element_by_name("text")
        text_input.send_keys('test')
        time.sleep(1)

        contact_input = self.selenium.find_element_by_name("contact_details")
        contact_input.send_keys('test_Name')
        time.sleep(1)

        educational_input = self.selenium.find_element_by_name("educational_background")
        educational_input.send_keys('test')
        time.sleep(1)

        award_input = self.selenium.find_element_by_name("award")
        award_input.send_keys('test')
        time.sleep(1)

        research_input = self.selenium.find_element_by_name("research_experience")
        research_input.send_keys('test')
        time.sleep(1)

        community_input = self.selenium.find_element_by_name("community_services")
        community_input.send_keys('test')
        time.sleep(1)

        skills_input = self.selenium.find_element_by_name("skills")
        skills_input.send_keys('test')
        time.sleep(1)

        # Submit post
        self.selenium.find_element_by_css_selector('button[type="submit"]').click()
        time.sleep(1)
        title = self.selenium.find_element_by_css_selector('h1').text
        self.assertTrue(title, 'My CV')
        contact = self.selenium.find_element_by_css_selector('p').text
        self.assertTrue(contact, 'test_Name')

#if __name__ == '__main__':  
    #unittest.main(warnings='ignore') 