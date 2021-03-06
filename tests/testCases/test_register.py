import pytest
from selenium import webdriver
from pageObjects.registerPage import Register
from utilities.readPropeties import ReadConfig

class Test_001_Register:
    registerURL = ReadConfig.getRegisterURL()
    username = 'admin'
    email = 'admin@gmail.com'
    password = 'test123'
    faulty_pass = 'test1234'
    
    def test_registerPageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.registerURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title=='Flippers - Register':
            assert True
        else:
            assert False

    def test_register(self, setup):
        self.driver = setup
        self.driver.get(self.registerURL)
        self.rp = Register(self.driver)
        self.rp.setUsername(self.username)
        self.rp.setUserEmail(self.email)
        self.rp.setAndConfirmUserPassword(self.password, self.password)
        self.rp.clickSignUp()
        
        
        message = self.driver.find_elements_by_class_name('invalid-feedback')
        if message:
            for i in message:
                error = i.find_element_by_tag_name("span").text
                print(f'********** {error} **********')
            assert False
        else:
            assert True
        self.driver.close()
        