import logging
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Test_Utilities import Common_Utilities
from .Base_Page import Base_Page

class HomePage(Base_Page):


    MY_STORE_LOGO = (By.XPATH,"//img[@alt =\"My Store\"]")
    DRESSES_ELEMENT = (By.XPATH,"//*[@id=\"block_top_menu\"]/ul/li[2]/a")
    SUMMER_DRESSES_ELEMENT =(By.XPATH,"//*[@id=\"block_top_menu\"]/ul/li[2]/ul/li[3]/a")
    ALL_SUMMER_DRESSES_ELEMENT = (By.XPATH, "//*[@id=\"center_column\"]/ul/li")
    image ="//*[@id=\"center_column\"]/ul/li/div/div[1]/div/a[1]/img"
    cart ="//*[@id=\"add_to_cart\"]/button/span"
    def __init__(self,driver):
        logging.info("Initializing HomePage")
        super().__init__(driver)
        #self.common_utility = Common_Utilities()

    'Get Logo Element'
    def get_logo_element(self):
        print("in get_logo_element")
        # return self.common_utility.find_web_element(self.driver,
        #                                             self.MY_STORE_LOGO,
        #                                             "get_logo_element",
        #                                             "one")
        return super().find_web_element(self.MY_STORE_LOGO,
                                        "get_logo_element",
                                        "one")

    'Get DRESSES Element'
    def get_DRESSES_element(self):
        print("In get_DRESSES_element")
        return super().find_web_element(self.DRESSES_ELEMENT,
                                        "get_DRESSES_element",
                                        "one")

    'Hover DRESSES Element to get available options' \
    'and returns True when action is performed successfully'
    def hover_DRESSES_element(self):
        print("In hover_DRESSES_element")
        return super().web_element_action(self.get_DRESSES_element(),
                                            "hover","","hover_DRESSES_element")

    'Get EVENING DRESSES Element and returns web element'
    def get_SUMMER_DRESSES_element(self):
        print("In get_SUMMER_DRESSES_element")
        return super().find_web_element(self.SUMMER_DRESSES_ELEMENT,
                                        "get_SUMMER_DRESSES_element",
                                        "one")

    'Click EVENING DRESSES Element and returns web element'
    def click_SUMMER_DRESSES_element(self):
        print("In click_SUMMER_DRESSES_element")
        result = super().web_element_action(self.get_SUMMER_DRESSES_element(),
                                    "click","","click_SUMMER_DRESSES_element")
        print(result)
        return result

