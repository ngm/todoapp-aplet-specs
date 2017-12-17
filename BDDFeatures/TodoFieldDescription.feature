@DescriptionField
Feature: Todo item description

# how best to do this?
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
