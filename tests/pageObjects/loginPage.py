from selenium import webdriver


class Login:
    textbox_username_id = 'email'
    textbox_password_id = 'password'
    login_page_button_xpath = '//*[@id="login_button"]'
    logout_button_xpath = '//*[@id="logout_button"]'
    button_login_xpath = '//*[@id="submit"]'
    
    def __init__(self, driver):
        self.driver = driver

    def navigateToLoginPage(self):
        self.driver.find_element_by_xpath(self.login_page_button_xpath).click()
        
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
    
    def setUserPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
    
    
