# Created by trang at 5/23/2021
Feature: Test Amazon search
  # Enter feature description here

  Scenario:User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on amazon search icon
    Then Verify search work