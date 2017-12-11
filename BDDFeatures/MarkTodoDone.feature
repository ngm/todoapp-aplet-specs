@MarkTodoDone
Feature: Mark todo as done

As a user
In order to keep track of my todos
I want to be able to mark a todo as done

Scenario: Mark todo as done
Given I have created the following todos:
  | Label                               |
  | Create evil plans strategy document |
  | Execute evil plans                  |
When I mark "Create evil plans strategy document" as done
Then I should see the following todos:
  | Label                                    |
  | DONE Create evil plans strategy document |
  | Execute evil plans                       |
