import time
from behave import *

@given(u'Chrome browser is opened')
def step_impl(context):
    print("Chrome browser opened successfully")

@when(u'MyStore URL "{url}" is provided')
def step_enter_url(context,url):
    context.driver.get(url)
    time.sleep(5)
    print(context.driver.current_url)
    assert context.driver.current_url == "http://automationpractice.com/index.php"

@then(u'MyStore website is opened successfully with title "{title}"')
def step_validate_website_title(context,title):
    assert context.driver.title == title


@then(u'MyStore logo is displayed on webpage')
def step_validate_website_logo_display(context):
    assert context.home_page.get_logo_element() is not None

@when(u'User hovers Dresses')
def step_impl(context):
    assert context.home_page.hover_DRESSES_element()

@when(u'Chooses Evening Dresses')
def step_impl(context):
    assert context.home_page.click_SUMMER_DRESSES_element()

@then(u'MyStore displays the catalog of evening dresses')
def step_impl(context):
    assert context.summer_dresses_page.choose_one_SUMMER_DRESS_ELEMENT()

@when(u'User chooses one item from the catalog displayed by clicking More')
def step_impl(context):
    pass


@then(u'Item details are shown')
def step_impl(context):
    pass


@then(u'User clicks on Tweet')
def step_impl(context):
    pass


@then(u'Appropriate Twitter Window opens')
def step_impl(context):
    pass


@then(u'User closes the Twitter window')
def step_impl(context):
    pass

@when(u'User clicks Add to cart')
def step_impl(context):
    pass

@then(u'Proceed to checkout popup opens')
def step_impl(context):
    pass

@then(u'User Clicks on Proceed to checkout')
def step_impl(context):
    assert context.summer_dresses_page.click_PROCEED_TO_CHECK_OUT_element()

@given(u'SHOPPING-CART SUMMARY page is dislayed')
def step_impl(context):
    pass


@when(u'Check the availability as In Stock')
def step_impl(context):
    pass

@then(u'Click Proceed to Checkout')
def step_impl(context):
    assert context.shopping_cart_summary_page.click_PROCEED_TO_CHECK_OUT_element()


@given(u'User enters Sign in page')
def step_impl(context):
    pass


@when(u'User provides username and password')
def step_impl(context):
    assert context.authentication_page.send_keys_EMAIL_ADDRESS_element(context.user_data_email)
    assert context.authentication_page.send_keys_PASSWORD_element(context.user_data_password)


@then(u'Click Sign in')
def step_impl(context):
    assert context.authentication_page.click_SIGN_IN_element()


@given(u'User enters Addresses page')
def step_impl(context):
    pass


@when(u'User city and state matches appropriately')
def step_impl(context):
    pass

@then(u'Click Proceed to Checkout in Address Page')
def step_impl(context):
    assert context.address_page.click_PROCEED_TO_CHECK_OUT_element()


@given(u'User enters shipping page')
def step_impl(context):
    pass


@when(u'Shipping details are displayed')
def step_impl(context):
    pass


@when(u'User agrees to Terms of service')
def step_impl(context):
    assert context.shipping_page.click_TERMS_OF_SERVICE_element()

@then(u'Click Proceed to Checkout in Shipping Page')
def step_impl(context):
    assert context.shipping_page.click_PROCEED_TO_CHECK_OUT_element()


@when(u'User enters Payment method page')
def step_impl(context):
    pass


@when(u'Total price is appropriate')
def step_impl(context):
    pass


@then(u'Click Pay by bank wire')
def step_impl(context):
    assert context.payment_page.click_PAY_BY_BANK_WIRE_element()


@given(u'User enters Bank-Wire Payment page')
def step_impl(context):
    pass


@given(u'Total Price is appropriate')
def step_impl(context):
    pass


@then(u'Click I confirm my order')
def step_impl(context):
    assert context.payment_page.click_CONFIRM_ORDER_element()


@then(u'Account owner name is displayed appropriately')
def step_impl(context):
        assert context.payment_page.get_text_ACCOUNT_OWNER_element() == context.user_data_name


