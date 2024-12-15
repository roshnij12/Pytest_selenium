#Test case to check login functionalities

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from testscripts.BaseTest import BaseTest


class Test_Login(BaseTest):

    def __init__(self, driver):
        self.driver = driver
    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce" )])
    def test_valid_login_TC1(self, username, password):
        self.driver.find_element(By.ID,"user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert "Swag Labs".__eq__(self.driver.title)

    @pytest.mark.smoke
    def test_invalid_login_TC2(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user_invalid")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce_invalid")
        self.driver.find_element(By.ID, "login-button").click()
        invalid_login_error = self.driver.find_element(By.XPATH,"//h3[contains(text(),'Epic sadface: ')]")
        invalid_login_error.is_displayed()
        #assert "Epic sadface: ".__contains__(invalid_login_error)