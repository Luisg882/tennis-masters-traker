# Tennis Masters

Tennis Masters is a Python terminal program where the user updates the results from the Tennis Masters tournament. This is a fantasy tennis tournament where the greatest tennis players of all time play against each other in a group stage. 

The program will calculate the score of each player, show the leaderboard, and the upcoming matches. 

[Live version of the program](https://tennis-masters-0a642a2fc445.herokuapp.com/)

![picture of laptop, tablet, mobile and computer monitor showing Tennis Masters program in a terminal](/assets/images/multiple-devices.jpg)

## Features

### Existing Features

- **Today's matches**
  - Prints the upcoming matches of the day.
  - It helps as a guide for the user to know the games that are going to be played.

  ![picture of Matches of the day showing the date and followed by the matches in the format player 1 vs player 2](/assets/images/today's-matches.jpg)

- **Update results**
  - Updates the scores of the players
  - It will ask to insert the result by player name, asking if they won or lost and update the result in the database.
  - If they win they score 3 points if they lose they score -1.
  - In case the user inserts a value different than win or loss an error message is going to appear and will repeat the Update results.
  - In case the user adds more winners than losers, and vise-versa, the program will show an error message and repeat the Update results.

  ![picture of the updated results, asking for the results in the following format "Insert the score of player name (win/loss): "](/assets/images/update-scores.jpg)

  ![picture the message confirming the update of the worksheet player-scores and total-score](/assets/images/update-scores-confirmation-message.jpg)

  ![picture of the misspelling error in the following format "Invalid data: invalid input. Please enter 'win' or 'loss'](/assets/images/miss-spelling-error.jpg)

  ![picture of unequal winners than losers error in the following format "Invalid data: There can only be 5 losers and 5 winners"](/assets/images/error-message-more-than-5-win-or-loss.jpg)

- **Leader Board**
  - Sorted the players by the highest total score.

  ![picture of the Leader Board in the following format: "1 position player bane with 20 score"](/assets/images/leader-board.jpg)

- **Next upcoming matches**
  - It's going to provide the upcoming matches date-by-date.

  ![picture of the next upcoming matches in the following format: "Next upcoming matches:  player1 vs player2, player3 vs player4...](/assets/images/next-upcoming-matches.jpg)

- **Update more results**
  - Will ask if the user wants to insert more results.
  - If yes, the program will run again the program giving the Today's Matches and restart the whole program.
  - If not, the program is going to print a message and exit.

  ![picture of the update more results question with a yes answer in the following format: "Do you want to enter new results? (yes/no): yes" runs the program again](/assets/images/update-more-results-yes.jpg)

  ![picture of the update more results question with a yes answer in the following format: "Do you want to enter new results? (yes/no): no" next line "Thank you for using Tennis Masters. Exiting...](/assets/images/update-more-results-no.jpg)

- **Exit the program**
  - When there are no more upcoming matches the program is going to Exit automatically giving an exit message first.

  ![picture of the Exit program message in the following format: "There are no upcoming matches. Exiting..."](/assets/images/exit.jpg)

### Future Features

  - Identify ties and organize them in the leaderboard so they will appear in the same position.
  - Generate a tide break matches.
  - A function that eliminates the bottom 2 players.
  - Create a single elimination tournament after the group stage.
  - Generate new matches with the dates they are going to play.

## Data Model

This project used a series of lists to manipulate the worksheets and update the changes.

The functions were designed to extract information from the worksheet, like the last row or specific row to make calculations for example, the function score_results() adds the results of the matches in the last row of the players-scores worksheet, or the update_scoreboard() function, were it takes the last row of the total-score worksheet, sum the results from score_results() function, and finally add them in the total-score worksheet.

## Testing

This project was manually tested as follows:

  - The program was written and tested using Pylint and no errors were found
  - Tried to insert the wrong values in the insert score question and the error was detected
  - Tried to not insert any value and the error message was thrown
  - Tried to add 7 winners and 3 losers the error message was thrown
  - Tested in Visual Studio Code and Heroku terminal.

  ![picture of the attempt to submit an empty answer](/assets/images/empty-answer-attempt.jpg)

  ![picture of the attempt to submit a different answer than yes or no](/assets/images/different-answer-attempt.jpg)

  ![picture of the attempt to submit more winners than losers](/assets/images/more-winners-than-lossers.jpg)


## Bugs
  **Solved Bugs**
    - After changing the score_results() to ask the result of each player individually the score, win or loss, was translated in 3 and -1 in the same function. This makes it impossible to validate a wrong answer, different than win or loss, in the validate_results() function, because the returned value from score_results() was a list of numbers, not strings. To fix it I make the returning value of score_results() a list of the answers, win or loss, that the user made. Then I create an empty list named int_results in the validate_results function and loop the return value of score_results(). In that way I can check in the validate_results if the answer was a win or loss, from then if it was a win it will append 3 to the ins_result list or -1 in the case of a loss. 

  **Remaining Bugs**
    - No remaining bugs

  **Validator Testing**
    - Pylint
      - No error found

## Deployment
  This project was deployed with a Code Institute mock terminal for Heroku
   - Fork tennis-masters-tracker 
   - Create a new Heroku app
   - Set the buildpacks to Phyton and NodeJS 
   - Link the app to the Git Hub repository 
   - Set the Deployment as automatic
   - Deploy the program

## Credits
  - The update_worksheet() function from [Love Sandwiches](https://love-sssandwich-688e34694d3c.herokuapp.com/)
  - The update_scoreboard was based on the function calculate_stock_data from [Love Sandwiches](https://love-sssandwich-688e34694d3c.herokuapp.com/)
  - Learn about the enumerate function in [w3schools](https://www.w3schools.com/python/ref_func_enumerate.asp)