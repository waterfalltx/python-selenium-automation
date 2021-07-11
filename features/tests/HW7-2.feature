# Created by trang at 7/10/2021
Feature: check cart items

  Scenario:'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Amazon Cart is empty.' text present
