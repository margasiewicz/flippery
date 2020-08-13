from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

# PyTest HTML Reports 

def pytest_configure(config):
    config._metadata['Project Name'] = 'Flippers remote control'
    config._metadata['Module Name'] = 'Flippers'
    config._metadata['Tester'] = 'margasiewicz'