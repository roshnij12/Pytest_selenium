#Test case to check add to cart
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By

from testscripts.BaseTest import BaseTest


class Test_Add_Product(BaseTest):

    def __init__(self, driver):
        self.driver = driver

    @pytest.mark.skip
    def test_add_product_to_cart_TC3(self):
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        pro1 = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Onesie']")
        actions = ActionChains(self.driver)
        actions.move_to_element(pro1).perform()
        self.driver.find_element(By.XPATH,"(//button[text()='ADD TO CART'])[5]").click()
        self.driver.find_element(By.ID,"shopping_cart_container").click()
        cart = self.driver.find_element(By.XPATH, "//div[text()='Your Cart']")
        cart.is_displayed()
        assert "Sauce Labs Onesie".__eq__(pro1)
        time.sleep(3)

    def test_add_to_cart_checkout_TC4(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        pro1 = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Onesie']")
        actions = ActionChains(self.driver)
        actions.move_to_element(pro1).perform()
        self.driver.find_element(By.XPATH, "(//button[text()='ADD TO CART'])[5]").click()
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        cart = self.driver.find_element(By.XPATH, "//div[text()='Your Cart']")
        cart.is_displayed()
        # assert pro1.is_displayed()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "CHECKOUT").click()
        checkout_header_1 = self.driver.find_element(By.XPATH,"//div[text()='Checkout: Your Information']")
        checkout_header_1.is_displayed()
        self.driver.find_element(By.ID, "first-name").send_keys("Bella")
        self.driver.find_element(By.ID, "last-name").send_keys("Hank")
        self.driver.find_element(By.ID, "postal-code").send_keys("89787")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        checkout_header_2 = self.driver.find_element(By.XPATH,"//div[text()='Checkout: Overview']")
        checkout_header_2.is_displayed()
        #assert "Sauce Labs Onesie".__eq__(pro1)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "FINISH").click()
        finish_header = self.driver.find_element(By.XPATH, "//div[text()='Finish']")
        finish_header.is_displayed()
        finish_text = self.driver.find_element(By.XPATH, "//h2[text()='THANK YOU FOR YOUR ORDER']")
        # assert "THANK YOU FOR YOUR ORDER".__eq__(finish_text)
        time.sleep(2)

