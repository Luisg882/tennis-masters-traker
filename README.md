# Tennis Masters

Tennis Masters is a Python terminal program were the user updates the results form the Tennis Masters tournament. This is a fantasy tennis tournament were the greatest tennis players of all time.

Also the program will calculate the score of each, display the leader board, and the upcoming matches.

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

  ![picture of the next]

- **Update more results**
  - Will ask if the user want to insert more results
  - If yes the program will run again giving the following date

