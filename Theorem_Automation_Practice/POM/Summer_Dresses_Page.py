import time
from random import randint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Test_Utilities import Common_Utilities
from .Base_Page import Base_Page

class Summer_Dresses_Page(Base_Page):


    SUMMER_DRESSES_ELEMENT =(By.XPATH,"//*[@id=\"block_top_menu\"]/ul/li[2]/ul/li[3]/a")
    ALL_SUMMER_DRESSES_ELEMENT = (By.XPATH, "//*[@id=\"center_column\"]/ul/li")
    ADD_TO_CART=(By.XPATH,"//*[@id=\"center_column\"]/ul/li[1]/div/div[2]/div[2]/a[1]/span")
    PROCEED_TO_CHECK_OUT = (By.XPATH,"//*[@id=\"layer_cart\"]/div[1]/div[2]/div[4]/a/span")

    def __init__(self,driver):
        print("Initializing Summer_Dresses_Page")
        super().__init__(driver)
        #self.common_utility = Common_Utilities()

    'Get all SUMMER DRESSES web elements and return'
    def get_ALL_SUMMER_DRESSES_element(self):
        print("In get_ALL_SUMMER_DRESSES_element")
        return super().find_web_element(self.ALL_SUMMER_DRESSES_ELEMENT,
                                        "get_ALL_SUMMER_DRESSES_element",
                                        "multiple")

    'Choose one of the SUMMER_DRESSES and return True if operation successful'
    def choose_one_SUMMER_DRESS_ELEMENT(self):
        print("In choose_one_SUMMER_DRESS_ELEMENT")
        'Getting total no. of summer dresses'
        total_summer_dresses =len(self.get_ALL_SUMMER_DRESSES_element())
        print(total_summer_dresses)

        'Choosing a random summer dress from the catalog'
        option_no = randint(1, total_summer_dresses -1)
        print(option_no)

        'Construct XPATH of the random summer dress from catalog'
        xpath_chosen_summer_dress = "//*[@id=\"center_column\"]/ul/li["+str(option_no)+"]/div/div[1]/div/a[1]/img"
        print(xpath_chosen_summer_dress)

        'Get the chosen summer dress element'
        ONE_SUMMER_DRESSES_ELEMENT = (By.XPATH, xpath_chosen_summer_dress)
        chosen_summer_dress  = super().find_web_element(ONE_SUMMER_DRESSES_ELEMENT,
                                 "choose_one_SUMMER_DRESS_ELEMENT",
                                 "one")
        print(chosen_summer_dress)

        'Scroll to the chosen Summer Dress'
        self.driver.execute_script("arguments[0].scrollIntoView();", chosen_summer_dress)


        'Hover on the randomly chosen summer dress from the catalog'
        result= super().web_element_action(chosen_summer_dress,
                                   "hover", "", "choose_one_SUMMER_DRESS_ELEMENT")

        'Construct XPATH of the random summer dress ADD_TO_CART element'
        xpath_chosen_summer_dress_add_to_cart ="//*[@id=\"center_column\"]/ul/li["+str(option_no)+"]/div/div[2]/div[2]/a[1]/span"
        print(xpath_chosen_summer_dress_add_to_cart)

        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_chosen_summer_dress_add_to_cart))).click()
            print("in try block")
            result = True
        except Exception as e:
            print("Exception occured while clicking Add to cart in Summer Dresses")

        # 'Get the chosen summer dress ADD_TO_CART element'
        # ONE_SUMMER_DRESSES_ADD_TO_CART_ELEMENT = (By.XPATH, xpath_chosen_summer_dress_add_to_cart)
        # chosen_summer_dress_add_to_cart = super().find_web_element(ONE_SUMMER_DRESSES_ADD_TO_CART_ELEMENT,
        #                                                "choose_one_SUMMER_DRESS_ELEMENT",
        #                                                "one")
        # print(chosen_summer_dress_add_to_cart)
        #
        # 'Click on the randomly chosen summer dress from the catalog'
        # result = super().web_element_action(chosen_summer_dress_add_to_cart,
        #                                     "hover", "", "choose_one_SUMMER_DRESS_ELEMENT")
        print(result)

        return result

    'Get ADD_TO_CART Element'
    def get_ADD_TO_CART_element(self):
        print("In get_ADD_TO_CART_element")

        return super().find_web_element(self.ADD_TO_CART,
                                        "get_ADD_TO_CART_element",
                                        "one")

    'Click ADD_TO_CART Element'
    def click_ADD_TO_CART_element(self):
        print("In click_ADD_TO_CART_element")
        time.sleep(2)
        result = super().web_element_action(self.get_ADD_TO_CART_element(),
                                    "click","","click_ADD_TO_CART_element")

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





