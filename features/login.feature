Feature: Login and Order Product

  Scenario: Successful Login
    Given I am on the Demo Login Page
    When I fill the account information for account StandardUser into the Username field and the Password field
    And I click the Login Button
    Then I am redirected to the Demo Main Page
    And I verify the App Logo exists

  Scenario: Failed Login
    Given I am on the Demo Login Page
    When I fill the account information for account LockedOutUser into the Username field and the Password field
    And I click the Login Button
    Then I verify the Error Message contains the text "Epic sadface: Sorry, this user has been locked out."

  Scenario: Order a product
    Given I am on the inventory page
    When user sorts products from high price to low price
    And user adds highest priced product
    And user clicks on cart
    And user clicks on checkout
    And user enters first name Alice
    And user enters last name Doe
    And user enters zip code 592
    And user clicks on Continue button
    Then I verify in Checkout overview page if the total amount for the added item is $53.99
    When user clicks on Finish button
    Then Thank You header is shown in Checkout Complete page
