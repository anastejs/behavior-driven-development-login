Feature: Login
    Identify the visitor and store their data

  Scenario: Successful Login
    Given username and password 
    When Log In button is clicked
    Then show welcome message