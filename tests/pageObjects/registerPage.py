from selenium import webdriver


class Register:
    textbox_username_id = 'username'
    textbox_email_id = 'email'
    textbox_password_id = 'password'
    textbox_conf_password_id = 'confirm_password'
    button_register_xpath = '//*[@id="submit"]'
    nav_login_page = '/html/body/main/div/div[2]/small/a'
    
    def __init__(self, driver):
        self.driver = driver
        
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        
    def setUserEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)
    
    def setAndConfirmUserPassword(self, password, confPassword):
        self.driver.find_element_by_id(self.textbox_password_id).clear
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        self.driver.find_element_by_id(self.textbox_conf_password_id).clear
        self.driver.find_element_by_id(self.textbox_conf_password_id).send_keys(confPassword)
    
    def clickSignUp(self):
        self.driver.find_element_by_xpath(self.button_register_xpath).click()
    
    def navigateToLoginPage(self):
        self.driver.find_element_by_link_text('Sign In').click()