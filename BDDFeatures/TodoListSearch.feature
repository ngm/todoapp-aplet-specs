@Search
Feature: Search list of todos

As a user
In order to easily find todos
I want to be able to search my list of todos

Scenario: Search list for text that is present in one todo
Given I have created the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
When I visit my todo list
And I search the list for "strategy"
Then I should see the following todos:
  | Label                               |
  | Create evil plans strategy document |

Scenario: Search list for text that is present in multiple todos
Given I have created the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
When I visit my todo list
And I search the list for "evil"
Then I should see the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
