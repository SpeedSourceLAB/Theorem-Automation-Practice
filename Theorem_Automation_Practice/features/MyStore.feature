Feature: MyStore User Purchase
  This feature provides the steps performed
  when user purchases an item in MyStore.

  Scenario: MyStore Set up
    Given Chrome browser is opened
    When MyStore URL "http://automationpractice.com/" is provided
    Then MyStore website is opened successfully with title "My Store"
     And MyStore logo is displayed on webpage

  Scenario: User browses "Women's Summer dresses"
    When User hovers Dresses
    And Chooses Summer Dresses
    Then MyStore displays the catalog of Summer dresses and user chooses one

  Scenario: User shares an item in Social Media
    When User chooses one item from the catalog displayed by clicking More
    Then Item details are shown
    And User clicks on Tweet
    And Appropriate Twitter Window opens
    And User closes the Twitter window

  Scenario: User adds Item to cart and proceeds to checkout
    When User clicks Add to cart
    Then Proceed to checkout popup opens
    And User Clicks on Proceed to checkout

  Scenario: SHOPPING-CART SUMMARY - Step 1/5 Checkout process to complete purchase
    Given SHOPPING-CART SUMMARY page is dislayed
    When Check the availability as In Stock
    Then Click Proceed to Checkout

  Scenario: User Sign in - Step 2/5 Checkout process to complete purchase
    Given User enters Sign in page
    When User provides username and password
    Then Click Sign in

  Scenario: Verify Address - Step 3/5 Checkout process to complete purchase
    Given User enters Addresses page
    When User city and state matches appropriately
    Then Click Proceed to Checkout in Address Page

  Scenario: Shipping Details - Step 4/5 Checkout process to complete purchase
    Given User enters shipping page
    When Shipping details are displayed
    And User agrees to Terms of service
    Then Click Proceed to Checkout in Shipping Page

  Scenario: Choose a payment method - Step 5/5 Checkout process to complete purchase
    When User enters Payment method page
    And Total price is appropriate
    Then Click Pay by bank wire

  Scenario: Confirm Order
    Given User enters Bank-Wire Payment page
    And Total Price is appropriate
    Then Click I confirm my order
    Then Account owner name is displayed appropriately



