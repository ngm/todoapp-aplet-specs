@NotSearch
Feature: Search list of todos is not present
  
Scenario: Search list of todos is not present
Given I have created the following todos:
  | Label                               | Status |
  | Execute evil plans                  | TODO   |
  | Create evil plans strategy document | DONE   |
When I visit my todo list
Then the search option should not be present
