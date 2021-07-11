# Created by trang at 7/10/2021
Feature: Check Sign In page when clicking Orders Icon


  Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page  is opened
