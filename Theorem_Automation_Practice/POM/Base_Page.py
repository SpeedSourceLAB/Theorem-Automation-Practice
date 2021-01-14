import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime


class Base_Page:

    def __init__(self,driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    'Find the Web element using Selenium'
    def find_web_element(self,locator, element_desc, element_count):

        web_element = ''
        if element_count == "one":
            try:
                print(locator)
                web_element = self.wait.until(EC.presence_of_element_located(locator))
                print(element_desc, "found")
                logging.info(element_desc + " found")
                return web_element
            except Exception as e:
                print(element_desc + " not found", e)
                logging.exception("Exception Occurred when fetching element " + element_desc)
                logging.exception(e)
                filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
                self.driver.get_screenshot_as_file(filename)
        elif element_count == "multiple":
            try:
                print(locator)
                web_elements = self.wait.until(EC.presence_of_all_elements_located(locator))
                print(element_desc, "found and returned list of web elements")
                logging.info("Found and returned list of web elements " + element_desc)
                return web_elements
            except Exception as e:
                print(element_desc, "not found", e)
                logging.exception("Unexpected Exception raised when fetching list of web elements " + element_desc)
                logging.exception(e)
                filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
                self.driver.get_screenshot_as_file(filename)

    'Perform action on web element using Selenium'

    def web_element_action(self, web_element, action, send_keys_values, element_desc):
        try:
            if action == "send_keys":
                try:
                    web_element.send_keys(send_keys_values)
                    print(action, "to", element_desc)
                    logging.info(action + " to " + element_desc)
                    return True
                except Exception as e:
                    print("Unexpected Exception raised when", action, "to", element_desc, e)
                    logging.exception("Unexpected Exception raised when", action, "to" + element_desc)
                    logging.exception(e)
                    filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(filename)
                    return False
            elif action == "click":
                try:
                    web_element.click()
                    print(element_desc, "clicked")
                    logging.info(element_desc + " clicked")
                    return True
                except Exception as e:
                    print("Unexpected error while clicking", element_desc, e)
                    logging.exception("Unexpected error while clicking " + element_desc)
                    logging.exception(e)
                    filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(filename)
                    return False
            elif action == "get_text":
                try:
                    print(element_desc, "get_text")
                    logging.info(element_desc + "get_text ")
                    print(web_element.get_attribute('innerHTML'))
                    return web_element.get_attribute('innerHTML')
                except Exception as e:
                    print("Unexpected error while getting text ", element_desc, e)
                    logging.exception("Unexpected error while getting text" + element_desc)
                    logging.exception(e)
                    filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(filename)
                    return False
            elif action == "clear_text":
                try:
                    print(element_desc, "clear_text")
                    logging.info(element_desc + " clear_text")
                    web_element.clear()
                    return True
                except Exception as e:
                    print("Unexpected error while clearing text at ", element_desc, e)
                    logging.exception("Unexpected error while clearing text" + element_desc)
                    logging.exception(e)
                    filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(filename)
                    return False
            elif action == "hover":
                try:
                    print(element_desc, "hover")
                    logging.info(element_desc + "hover")
                    hover = ActionChains(self.driver).move_to_element(web_element)
                    hover.perform()
                    return True
                except Exception as e:
                    filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(filename)
                    print("Unexpected error while hovering on ", element_desc, e)
                    logging.exception("Unexpected error while hovering on" + element_desc)
                    logging.exception(e)
                    return False
        except Exception as e:
            print("Unexpected exception occurred in def web_element_action", e)
            logging.error("Unexpected exception occurred in web_element_action")
            filename = "Screenshot\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
            self.driver.get_screenshot_as_file(filename)
            logging.exception(e)