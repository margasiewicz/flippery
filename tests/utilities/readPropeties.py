import configparser

config = configparser.RawConfigParser()
config.read('.\\tests\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
    
    @staticmethod
    def getLoginURL():
        url = config.get('common info', 'loginURL')
        return url
    
    @staticmethod
    def getRegisterURL():
        url = config.get('common info', 'registerURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
        