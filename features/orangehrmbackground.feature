Feature: Orange HRM Modules test
  Background: common steps
    Given launch webdrive
    When  lauch App
    And   Enter un "Admin" and "admin123"
    And   click login

  Scenario: login orange hrm
    Then  successfull login Dashboard

  Scenario: Admin Feature
    Then  Admin module
    Then  Admin dashboard

  Scenario: Directory Feature
    Then  Directory module
    Then  Directory dashboard


