@Search
Feature: Search list of todos

As a user
In order to easily find todos
I want to be able to search my list of todos

Scenario: Filter list with text that is present in one todo
Given I have created the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
When I visit my todo list
And I filter the list by "strategy"
Then I should see the following todos:
  | Label                               |
  | Create evil plans strategy document |

Scenario: Filter list with text that is present in multiple todos
Given I have created the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
When I visit my todo list
And I filter the list by "evil"
Then I should see the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
