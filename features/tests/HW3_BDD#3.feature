# Created by trang at 5/31/2021
Feature: Test Amazon Cart

  Scenario: User can check amazon cart items
    Given Open Amazon page
    When Click on amazon cart icon
    Then Verify amazon cart is empty