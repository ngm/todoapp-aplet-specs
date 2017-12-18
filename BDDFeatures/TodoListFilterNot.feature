Feature: Filter list of todos is not present
  
@NotFilter
Scenario: Filter list of todos is not present
Given I have created the following todos:
  | Label                               | Status |
  | Execute evil plans                  | TODO   |
  | Create evil plans strategy document | DONE   |
When I visit my todo list
Then the filter option should not be present
