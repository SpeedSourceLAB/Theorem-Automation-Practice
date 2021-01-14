import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Test_Utilities import Common_Utilities
from .Base_Page import Base_Page

class Authentication_Page(Base_Page):

    EMAIL_ADDRESS = (By.XPATH,"//*[@id=\"email\"]")
    PASSWORD = (By.XPATH,"//*[@id=\"passwd\"]")
    SIGN_IN = (By.XPATH, "//*[@id=\"SubmitLogin\"]/span")

    def __init__(self,driver):
        print("Initializing Authentication_Page")
        super().__init__(driver)


    'Get EMAIL_ADDRESS Element'
    def get_EMAIL_ADDRESS_element(self):
        print("In get_EMAIL_ADDRESS_element")

        return super().find_web_element(self.EMAIL_ADDRESS,
                                        "get_EMAIL_ADDRESS_element",
                                        "one")

    'Send Keys to EMAIL_ADDRESS Element'
    def send_keys_EMAIL_ADDRESS_element(self,email):
        print("In send_keys_EMAIL_ADDRESS_element")
        time.sleep(2)

        result = super().web_element_action(self.get_EMAIL_ADDRESS_element(),
                                            "send_keys", email, "send_keys_EMAIL_ADDRESS_element")

        print(result)
        return result

    'Get PASSWORD Element'
    def get_PASSWORD_element(self):
        print("In get_PASSWORD_element")

        return super().find_web_element(self.PASSWORD,
                                        "get_PASSWORD_element",
                                        "one")

    'Send Keys to PASSWORD Element'
    def send_keys_PASSWORD_element(self,password):
        print("In send_keys_PASSWORD_element")
        time.sleep(2)
        result = super().web_element_action(self.get_PASSWORD_element(),
                                            "send_keys", password, "send_keys_EMAIL_ADDRESS_element")

        print(result)
        return result

    'Get SIGN_IN Element'
    def get_SIGN_IN_element(self):
        print("In get_SIGN_IN_element")

        return super().find_web_element(self.SIGN_IN,
                                        "get_SIGN_IN_element",
                                        "one")

    'Click SIGN_IN Element'
    def click_SIGN_IN_element(self):
        print("In click_SIGN_IN_element")
        time.sleep(2)
        result = super().web_element_action(self.get_SIGN_IN_element(),
                                            "click", "", "click_SIGN_IN_element")

        print(result)
        return result