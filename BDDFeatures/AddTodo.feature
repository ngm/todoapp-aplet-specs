Feature: Add todo to list

As a user
In order to keep track of my todos
I want to be able to view a list of my todos

@AddTodo
Scenario: Add one-word todo
When I create a todo with the label "Cogitate"
Then the todo "Cogitate" is added to my todo list

@AddTodo
Scenario: Add multi-word todo
When I create a todo with the label "Take over the world"
Then the todo "Take over the world" is added to my todo list

@AddTodo
Scenario: Add empty todo
When I create a todo with the label ""
Then I should get an error saying the label is empty

@DescriptionField
Scenario: Add todo with description field
When I create a todo with the label "Take over the world" and description "This is step one of my plans for universal domination."
Then the todo "Take over the world" with description "This is step one of my plans for universal domination." is added to my todo list
