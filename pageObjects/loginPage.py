from selenium import webdriver


class Login:
    textbox_username_id = 'email'
    textbox_password_id = 'password'
    button_login_xpath = '//*[@id="submit"]'
    
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
    
    def setUserPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    
    
