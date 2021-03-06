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
        $keys = array();
        foreach ($todos->getRows() as $index => $row) {
            if ($index === 0) { // first row to define fields
                $keys = $row;
                continue;
            }
            $url = '/add.php?label=' . urlencode($row[0]);
            if (isset($row[1]) && $keys[1] == 'Status')
            {
                $url .=  '&status=' . urlencode($row[1]);
            }
            else if (isset($row[1]) && $keys[1] == 'Description')
            {
                $url .=  '&description=' . urlencode($row[1]);
            }
            $this->amOnPage($url);
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
        $keys = array();
        foreach ($todos->getRows() as $index => $row) {
            if ($index === 0) { // first row to define fields
                $keys = $row;
                continue;
            }
            $this->see($row[0]);
            if (isset($keys[1]) && $keys[1] == 'Description')
            {
                $this->see($row[1]);
            }
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

    /**
     * @When I filter the list by :status
     */
    public function iFilterTheListBy($status)
    {
        $this->click($status);
    }

    /**
     * @Then the filter option should not be present
     */
    public function theFilterOptionShouldNotBePresent()
    {
        $this->dontSee('Filter');
    }

    /**
     * @When I search the list for :searchTerm
     */
    public function iSearchTheListFor($searchTerm)
    {
        $this->submitForm('#search', [
            'searchTerm' => $searchTerm
        ]);
    }

    /**
     * @Then I should not see the following todos:
     */
    public function iShouldNotSeeTheFollowingTodos(\Behat\Gherkin\Node\TableNode $todos)
    {
        foreach ($todos->getRows() as $index => $row) {
            if ($index === 0) { // first row to define fields
                $keys = $row;
                continue;
            }
            $this->dontSee($row[0]);
        }
    }

    /**
     * @Then the search option should not be present
     */
    public function theSearchOptionShouldNotBePresent()
    {
        $this->dontSee('Search:');
    }


    /**
     * @When I create a todo with the label :label and description :description
     */
    public function iCreateATodoWithTheLabelAndDescription($label, $description)
    {
        $this->amOnPage('/add.php?label=' . $label . '&description=' . $description);
    }

    /**
     * @Then the todo :label with description :description is added to my todo list
     */
    public function theTodoWithDescriptionIsAddedToMyTodoList($label, $description)
    {
        $this->amOnPage('/index.php');
        $this->see($label);
        $this->see($description);
    }
}
