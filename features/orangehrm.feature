Feature: Orange HRM Logo
  Scenario: logo presence on orangehrm
    Given   launch chrome browser
    When    open orangehrm homepage
    Then    verify that logo present or not
    And     close browser

  Scenario: Un and pwd
    Given launch browser
    When open browser
    Then enter un and pwd
    And close page

  Scenario: Employee name details
    Given launch
    When open webpage
    Then Enter Employee records
    And close webpage

