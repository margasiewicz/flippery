import pytest
from selenium import webdriver
from pageObjects.loginPage import Login

class Test_001_Login:
    baseURL = "http://127.0.0.1:5000/login"
    username = 'admin@gmail.com'
    password = 'admin123'
    falseUsername = 'admin111@gmail.com'
    falseUsername = 'admin111@gmail.com'
    
    def test_loginPageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=='Flippers - Login':
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title=='Flippers':
            assert True
        else:
            assert False
            
    def test_loginFailure(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title=='Flippers':
            assert True
        else:
            assert False
