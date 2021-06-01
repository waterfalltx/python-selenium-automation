# Created by trang at 5/30/2021
Feature: User can search for solutions
  #1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
  #2. Use “Search Help Library” field and search for Cancel order
  #3. Emulate hitting keyboard ENTER btn with send_keys command (here’s how)
  #4. Verify that ‘Cancel Items or Orders’ text is present

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open amazon help page
    When Input Cancel order in search field

    Then Verify help search work
