import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager


class Common_Utilities:
    driver = None

    def __init__(self):
        print("In Common Utilities")

    'Get the driver object - Selenium'
    def get_driver(self, browser):
        print("Trying to open browser in Common defs")
        if (browser == "chrome"):
            try:
                options = webdriver.ChromeOptions()
                options.add_argument('--ignore-certificates-errors')
                options.add_argument("--test-type")
                options.add_argument("start-maximized")
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
                time.sleep(3)
                print("Browser opened successfully")
                logging.info("Browser opened successfully")

            except Exception as e:
                logging.exception("Browser closed unexpectedly")
                logging.exception(e)
                print("Browser closed unexpectedly, hence the script stopped.")

        elif (browser == "gecko"):
            try:
                options = webdriver.FirefoxOptions()
                options.add_argument("-start-maximized")
                caps = DesiredCapabilities().FIREFOX
                caps["marionette"] = True
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options,
                                                capabilities=caps)
                self.driver.maximize_window()
                time.sleep(3)
                print("Browser opened successfully")
                logging.info("Browser opened successfully")
            except Exception as e:
                logging.exception("Browser closed unexpectedly")
                logging.exception(e)
                print("Browser closed unexpectedly, hence the script stopped.")

        return self.driver

    # Crete the driver -Selenium
    def driver_creation(self, browser):
        self.browser = browser
        driver = self.get_driver(browser)

        for i in range(5):
            while (driver == None):
                if (i < 5):
                    print("Opening Browser, Attempts:", i + 1, "/5 times")
                    driver = self.get_driver(browser)
                    time.sleep(10)
                    i += 1
                    if (driver != None):
                        break
        return driver


