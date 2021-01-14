import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Test_Utilities import Common_Utilities
from .Base_Page import Base_Page

class Shipping_Page(Base_Page):

    PROCEED_TO_CHECK_OUT = (By.XPATH,"//*[@id=\"form\"]/p/button/span")
    TERMS_OF_SERVICE = (By.XPATH,"//*[@id=\"cgv\"]")

    def __init__(self,driver):
        print("Initializing Shipping_Page")
        super().__init__(driver)

    'Get PROCEED_TO_CHECK_OUT Element'
    def get_TERMS_OF_SERVICE_element(self):
        print("In get_TERMS_OF_SERVICE_element")

        return super().find_web_element(self.TERMS_OF_SERVICE,
                                        "get_TERMS_OF_SERVICE_element",
                                        "one")

    'Click PROCEED_TO_CHECK_OUT Element'
    def click_TERMS_OF_SERVICE_element(self):
        print("In click_TERMS_OF_SERVICE_element")
        time.sleep(2)
        result = super().web_element_action(self.get_TERMS_OF_SERVICE_element(),
                                            "click", "", "click_TERMS_OF_SERVICE_element")

        print(result)
        return result


    'Get PROCEED_TO_CHECK_OUT Element'
    def get_PROCEED_TO_CHECK_OUT_element(self):
        print("In get_PROCEED_TO_CHECK_OUT_element")

        return super().find_web_element(self.PROCEED_TO_CHECK_OUT,
                                        "get_PROCEED_TO_CHECK_OUT_element",
                                        "one")

    'Click PROCEED_TO_CHECK_OUT Element'
    def click_PROCEED_TO_CHECK_OUT_element(self):
        print("In click_PROCEED_TO_CHECK_OUT_element")
        time.sleep(2)
        result = super().web_element_action(self.get_PROCEED_TO_CHECK_OUT_element(),
                                            "click", "", "click_PROCEED_TO_CHECK_OUT_element")

        print(result)
        return result