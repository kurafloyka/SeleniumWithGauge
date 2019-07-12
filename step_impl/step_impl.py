from getgauge.python import step, before_scenario, Messages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')


@step("isim yaz")
def isimyaz():
    print("farukakyoladanali")
    # Uygulama Mesajları


@step("Uygulamanin Acilmasi")
def ilkStep():
    driver = webdriver.Firefox(executable_path="C:/Users/FARUK/Desktop/SeleniumWithGauge/resources/geckodriver.exe")
    driver.get("http://www.python.org")

    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    logger.warning('1This is a warning')
    logger.error('2This is an error')
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

    assert "No results found." not in driver.page_source
    driver.close()


# ---------------
# Execution Hooks
# ---------------

@before_scenario()
def before_scenario_hook():
    print("before senaryo")
    logger.debug('3This is a debug message')
