<?php


/**
 * Inherited Methods
 * @method void wantToTest($text)
 * @method void wantTo($text)
 * @method void execute($callable)
 * @method void expectTo($prediction)
 * @method void expect($prediction)
 * @method void amGoingTo($argumentation)
 * @method void am($role)
 * @method void lookForwardTo($achieveValue)
 * @method void comment($description)
 * @method \Codeception\Lib\Friend haveFriend($name, $actorClass = NULL)
 *
 * @SuppressWarnings(PHPMD)
*/
class AcceptanceTester extends \Codeception\Actor
{
    use _generated\AcceptanceTesterActions;

   /**
    * Define custom actions here
    */

    /**
     * @When I create a todo with the label :label
     */
    public function iCreateATodoWithTheLabel($label)
    {
        $this->amOnPage('/add.php?label=' . $label);
    }

    /**
     * @Then the todo :label is added to my todo list
     */
    public function theTodoIsAddedToMyTodoList($label)
    {
        $this->amOnPage('/index.php');
        $this->see($label);
    }

    /**
     * @Given I have created the following todos:
     */
    public function iHaveCreatedTheFollowingTodos()
    {
        throw new \Codeception\Exception\Incomplete("Step `I have created the following todos:` is not defined");
    }

    /**
     * @When I visit my todo list
     */
    public function iVisitMyTodoList()
    {
        throw new \Codeception\Exception\Incomplete("Step `I visit my todo list` is not defined");
    }

    /**
     * @Then I should see my todos
     */
    public function iShouldSeeMyTodos()
    {
        throw new \Codeception\Exception\Incomplete("Step `I should see my todos` is not defined");
    }
}
