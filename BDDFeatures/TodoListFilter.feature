@Filter
Feature: Filter list of todos

As a user
In order to easily find todos
I want to be able to filter my list of todos

Background:
Given I have created the following todos:
  | Label                               | Status |
  | Execute evil plans                  | TODO   |
  | Create evil plans strategy document | DONE   |

Scenario: Filter list for done todos
When I visit my todo list
And I filter the list by "DONE"
Then I should see the following todos:
  | Label                               |
  | Create evil plans strategy document |

Scenario: Filter list for TODO todos
When I visit my todo list
And I filter the list by "TODO"
Then I should see the following todos:
  | Label                               |
  | Execute evil plans                  |

Scenario: Clear filter
When I visit my todo list
And I filter the list by "NO FILTER"
Then I should see the following todos:
  | Label                               |
  | Execute evil plans                  |
  | Create evil plans strategy document |
