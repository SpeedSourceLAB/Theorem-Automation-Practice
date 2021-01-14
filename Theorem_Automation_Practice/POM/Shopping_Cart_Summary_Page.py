import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Test_Utilities import Common_Utilities
from .Base_Page import Base_Page

class Shopping_Cart_Summary_Page(Base_Page):

    PROCEED_TO_CHECK_OUT = (By.XPATH,"//*[@id=\"center_column\"]/p[2]/a[1]/span")

    def __init__(self,driver):
        print("Initializing Summer_Dresses_Page")
        super().__init__(driver)


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