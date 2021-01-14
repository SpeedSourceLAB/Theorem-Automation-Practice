import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Test_Utilities import Common_Utilities
from .Base_Page import Base_Page

class Payment_Page(Base_Page):

    PAY_BY_BANK_WIRE = (By.XPATH,"//*[@id=\"HOOK_PAYMENT\"]/div[1]/div/p/a")
    CONFIRM_ORDER =  (By.XPATH,"//*[@id=\"cart_navigation\"]/button/span")
    ACCOUNT_OWNER = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/strong[1]")

    def __init__(self,driver):
        print("Initializing Payment_Page")
        super().__init__(driver)


    'Get PAY_BY_BANK_WIRE Element'
    def get_PAY_BY_BANK_WIRE_element(self):
        print("In get_PAY_BY_BANK_WIRE_element")

        return super().find_web_element(self.PAY_BY_BANK_WIRE,
                                        "get_PAY_BY_BANK_WIRE_element",
                                        "one")

    'Click PAY_BY_BANK_WIRE Element'
    def click_PAY_BY_BANK_WIRE_element(self):
        print("In click_PAY_BY_BANK_WIRE_element")
        time.sleep(2)
        result = super().web_element_action(self.get_PAY_BY_BANK_WIRE_element(),
                                            "click", "", "click_PAY_BY_BANK_WIRE_element")

        print(result)
        return result

    'Get CONFIRM_ORDER Element'
    def get_CONFIRM_ORDER_element(self):
        print("In get_CONFIRM_ORDER_element")

        return super().find_web_element(self.CONFIRM_ORDER,
                                        "get_CONFIRM_ORDER_element",
                                        "one")

    'Click CONFIRM_ORDER Element'
    def click_CONFIRM_ORDER_element(self):
        print("In click_CONFIRM_ORDER_element")
        time.sleep(2)
        result = super().web_element_action(self.get_CONFIRM_ORDER_element(),
                                            "click", "", "click_CONFIRM_ORDER_element")

        print(result)
        return result

    'Get ACCOUNT OWNER element'
    def get_ACCOUNT_OWNER_element(self):
        print("In get_ACCOUNT_ORDER_element")

        return super().find_web_element(self.ACCOUNT_OWNER,
                                        "get_CONFIRM_ORDER_element",
                                        "one")

    'Get text of  ACCOUNT OWNER element'
    def get_text_ACCOUNT_OWNER_element(self):
        print("In get_text_ACCOUNT_OWNER_element")
        time.sleep(2)
        result = super().web_element_action(self.get_ACCOUNT_OWNER_element(),
                                            "get_text", "", "get_text_ACCOUNT_OWNER_element")

        print(result)
        return result