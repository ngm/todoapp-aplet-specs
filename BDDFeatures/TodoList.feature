Feature: View list of todos

As a user
In order to see all of my todos in one place
I want to be able to view a list of my todos

@TodoList
Scenario: List of todos
Given I have created the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
When I visit my todo list
Then I should see the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |

@DescriptionField
@current
Scenario: List of todos with description
Given I have created the following todos:
  | Label                               | Description            |
  | Execute evil plans                  | Some description       |
  | Create evil plans strategy document | Some other description |
When I visit my todo list
Then I should see the following todos:
  | Label                               | Description            |
  | Execute evil plans                  | Some description       |
  | Create evil plans strategy document | Some other description |
