# Tennis Masters

Tennis Masters is a Python terminal program were the user updates the results form the Tennis Masters tournament. This is a fantasy tennis tournament were the greatest tennis players of all time play agains each other in a group stage. 

The program will calculate the score of each, display the leader board, and the upcoming matches. 

[Live version of the program](https://tennis-masters-0a642a2fc445.herokuapp.com/)

![picture of laptop, tablet, mobile and computer monitor showing Tennis Masters program in a terminal](/assets/images/multiple-devices.jpg)

## Features

### Existing Features

- **Today's matches**
  - Prints the next upcoming matches order by date
  - It will fetch the data from the data base and print the first row of the worksheet

  ![picture of Matches of the day showing the date and followed by the matches in the format player 1 vs player 2](/assets/images/today's-matches.jpg)

- **Update results**
  - Updates the scores of the playes
  - It will ask to insert the result by the player name asking if they win or loss and update the result on the workisheet
  - If the win they scroe 3 point if they loss they score -1
  - Inputs validation error in case that the user insert a value that is not win or loss
  - Validates if the user adds more winners/lossers than 5

  ![picture of the update results, asking the results in the followed format "Insert the score of player name (win/loss): "](/assets/images/update-scores.jpg)

  ![picture the message confirmation the update of the worksheet player-scores and total-score](/assets/images/update-scores-confirmation-message.jpg)

  ![picture of the misspelling error in the following format "Invalid data: invalid input. Please enter 'win' or 'loss'](/assets/images/miss-spelling-error.jpg)

  ![picture of more than 5 winner of losser error in the following format "Invalid data: There can only be 5 losers and 5 winners"](/assets/images/error-message-more-than-5-win-or-loss.jpg)

- **Leader Board**
  - Sorted the players by the higest total score  

  ![picture of the Leader Board in the followed format: "1 position player bane with 20 score"](/assets/images/leader-board.jpg)

- **Next upcoming matches**
  - It's going to provide the upcoming matches date by date

  ![picture of the next upcoming matches in the following format: "Next upcoming matches:  player1 vs player2, player3 vs player4...](/assets/images/next-upcoming-matches.jpg)

- **Update more results**
  - Will ask if the user want's to insert more results
  - If yes the program will run again giving the Todays Matches and restart the hole program
  - If no the program is going to print a message and exit.

  ![picture of the update more results question with a yes answer in the following format: "Do you want to enter new results? (yes/no): yes" tuns the program again](/assets/images/update-more-results-yes.jpg)

  ![picture of the update more results question with a yes answer in the following format: "Do you want to enter new results? (yes/no): no" next line "Thank you for using Tennis Masters. Exiting...](/assets/images/update-more-results-no.jpg)

- **Exit the program**
  - Wen there is no more upcoming matches the program is going to Exit automatically giving a exit message first

  ![picture of the Exit program message in the following format: "There are no upcoming matches. Exiting..."](/assets/images/exit.jpg)

### Future Features

  - Oraganize tides so it will appear in the same position.
  - Generate a tide break matches.
  - A function that eliminates the bottom 2 players.
  - Create a single eliminatory tournament after the group stage.eliminating the bottom 2 players.
  - Generate a new matches with the dates their are going to play

## Data Model

This project used a series of list to manipulate the worksheets and update the changes.

The functions were design extracting the worksheet information like the last row or specific row to make calculations like score_results() were it adds the results of the matches in the las row of the players-scores worksheet, or the update_scoreboard() function, were it takes the last row of the total-score worksheet and sum the results added in the score_results() function.

## Testing

This project was manually tested as follow:

  - Program was written and tested using Pylint and no errors were found
  - Tried to insert wrong values in the insert score question and the error is detected
  - Tried to not insert any value and the error message was trow
  - Tried to add 7 winners and 3 lossers, the error message was trow
  - Tested in Visuial Studio Code and Heroku terminal.

  ![picture of the attempt to submit a empty answer](/assets/images/empty-answer-attempt.jpg)

  ![picture of the attempt to submit a different answer than yes or no](/assets/images/different-answer-attempt.jpg)

  ![picture of the attempt to submit more winners than losers](/assets/images/more-winners-than-lossers.jpg)


## Bugs
  **Solved Bugs**
    - After changing the score_results() to ask the result of each player individualy, the score, win or loss, was translated in 3 and -1 respectively. This make it imposible to validate if the user inser other value different than win or loss in the validate_results, because the returned value from score_results() were a list of numbers not strings. To fix it I make the resturning value of score_results() a list of the answers as strings, then I create a empty list named int_results in the validate_results function and loop the return value of score_results(). In that way I can check in the validate_results if the answer was win or loss, if it was correct I append the result to the list and return the ins_results value.



  **Remaining Bugs**
    - No remaining bugs

  **Validator Testing**
    - Pylint
      - No error found

## Deployment
  This project was deployed with Code Institute mock terminal for Heroku
   - Fork tennis-masters-traker 
   - Create a new Heroku app
   - Set the buildpacks to Phyton and NodeJS 
   - Link the app to the Git Hub repository 
   - Set the Deployment as automatic
   - Deploy the program

## Credits
  - The update_worksheet() function from [Love Sandwiches](https://love-sssandwich-688e34694d3c.herokuapp.com/)
  - The update_scoreboard was based in the function calculate_stock_data from [Love Sandwiches](https://love-sssandwich-688e34694d3c.herokuapp.com/)
  - Learn about the enumerate function in [w3schools](https://www.w3schools.com/python/ref_func_enumerate.asp)