#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 4:24 下午
# @Author  : Kaimin Zeng
# @File    : shimo_login.py

from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://shimo.im/login?from=home")
        self.driver.maximize_window()
        sleep(1)

    def test_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys("15902038154")
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys("qazwsx")
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
        sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    case = TestCase()
    case.test_xpath()


