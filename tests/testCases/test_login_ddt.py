import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from utilities.readPropeties import ReadConfig
from utilities import xlReader
from time import sleep

class Test_002_DDT_Login:
    loginURL = ReadConfig.getLoginURL()
    path = '.\\tests\\testData\\loginTestData.xlsx'

    def test_login_ddt(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)

        self.rows = xlReader.rowCount(self.path,'Arkusz1')

        lst_status=[]

        for row in range(2, self.rows+1):
            self.driver.get(self.loginURL)

            self.user = xlReader.readData(self.path, 'Arkusz1', row, 1)
            self.password = xlReader.readData(self.path, 'Arkusz1', row, 2)
            self.exp = xlReader.readData(self.path, 'Arkusz1', row, 3)

            self.lp.setUserName(self.user)
            self.lp.setUserPassword(self.password)
            self.lp.clickLogin()
            sleep(2)
            
            act_title = self.driver.title
            exp_title = 'Flippers'

            if act_title==exp_title:
                if self.exp=='Pass':
                    lst_status.append('Pass')
                else:
                    lst_status.append('Fail')
            else:
                if self.exp=='Pass':
                    lst_status.append('Fail')
                else:
                    lst_status.append('Pass')
            try:
                self.lp.clickLogout()
            except:
                pass

        if 'Fail' not in lst_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False