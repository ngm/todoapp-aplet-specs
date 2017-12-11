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
    public function iHaveCreatedTheFollowingTodos(\Behat\Gherkin\Node\TableNode $todos)
    {
        foreach ($todos->getRows() as $index => $row) {
            if ($index === 0) { // first row to define fields
                $keys = $row;
                continue;
            }
            $this->amOnPage('/add.php?label=' . $row[0]);
        }
    }

    /**
     * @When I visit my todo list
     */
    public function iVisitMyTodoList()
    {
        $this->amOnPage('/index.php');
    }

    /**
     * @Then I should see the following todos:
     */
    public function iShouldSeeMyTodos(\Behat\Gherkin\Node\TableNode $todos)
    {
        foreach ($todos->getRows() as $index => $row) {
            if ($index === 0) { // first row to define fields
                $keys = $row;
                continue;
            }
            $this->see($row[0]);
        }
    }

    /**
     * @Then I should get an error saying the label is empty
     */
    public function iShouldGetAnErrorSayingTheLabelIsEmpty()
    {
        $this->see("Please enter a label for your todo");
    }

    /**
     * @When I mark :label as done
     */
    public function iMarkAsDone($label)
    {
        $this->amOnPage('/index.php');
        $this->click('MarkDone');
    }
}
