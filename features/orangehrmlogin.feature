Feature: login Orange HRM
  Scenario: verify login
    Given launch webdriver
    When open orange hrm login
    And orange hrm "Admin" and "admin123"
    And click login button
    Then login successfully

  Scenario Outline: Login to Orange hrm with multiple parameters
    Given launch webdriver
    When open orange hrm login
    And orange hrm "<username>" and "<password>"
    And click login button
    Then login successfully

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminzyx |
