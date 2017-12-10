@AddTodo
Feature: Add todo to list

As a user
In order to keep track of my todos
I want to be able to view a list of my todos

Scenario: Add one-word todo
When I create a todo with the label "Cogitate"
Then the todo "Cogitate" is added to my todo list

Scenario: Add multi-word todo
When I create a todo with the label "Take over the world"
Then the todo "Take over the world" is added to my todo list

Scenario: Add empty todo
When I create a todo with the label ""
Then I should get an error saying the label is empty
