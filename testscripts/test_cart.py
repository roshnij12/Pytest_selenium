import time

import openpyxl
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from testscripts.BaseTest import BaseTest
from testscripts.test_SauceDemo_Login import Test_Login
from testscripts import test_SauceDemo_Login


class Test_cart_functions(BaseTest):

    def test_cart_checkout(self):
        #test_data_xl = openpyxl.load_workbook("C:\\Users\\roshj\\OneDrive\\Documents\\saucedemo_testdata.xlsx")
        #logindata = test_data_xl["logindata"]
        test_login = Test_Login(self.driver)
        test_login.test_valid_login_TC1("standard_user","secret_sauce")







