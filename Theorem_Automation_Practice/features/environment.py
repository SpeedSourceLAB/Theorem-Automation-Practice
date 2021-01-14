#import pandas
from behave.model_core import Status
from behave import fixture, use_fixture
from POM.Test_Utilities import Common_Utilities
from POM.Home_Page import HomePage
from POM.Base_Page import Base_Page
from POM.Summer_Dresses_Page import Summer_Dresses_Page
from POM.Shopping_Cart_Summary_Page import Shopping_Cart_Summary_Page
from POM.Authentication_Page import Authentication_Page
from POM.Address_Page import Address_Page
from POM.Shipping_Page import Shipping_Page
from POM.Payment_Page import Payment_Page

#from Theorem_Automation_Practice.POM.Test_Utilities import Common_Utilities
@fixture
def browser_chrome(context):
    # -- SETUP-FIXTURE PART:
    context.utilities = Common_Utilities()
    context.driver = context.utilities.driver_creation("chrome")
    context.base_page= Base_Page(context.driver)
    context.home_page = HomePage(context.driver)
    context.summer_dresses_page= Summer_Dresses_Page(context.driver)
    context.shopping_cart_summary_page = Shopping_Cart_Summary_Page(context.driver)
    context.authentication_page=Authentication_Page(context.driver)
    context.address_page=Address_Page(context.driver)
    context.shipping_page=Shipping_Page(context.driver)
    context.payment_page = Payment_Page(context.driver)
    #context.user_data = pandas.read_csv('Theorem_Automation_Practice\\resources\\user_details.csv')
    context.user_data_email ="mickey.mouse@gmail.com"
    context.user_data_password ="mickey@123"
    context.user_data_name = "Mickey Mouse"
    return context

def before_feature(context, feature):
    print("before_feature activated")
    use_fixture(browser_chrome,context)

def after_scenario(context, scenario):
     print(scenario.status)
     if scenario.status==Status.failed:
         print(scenario,"failed")