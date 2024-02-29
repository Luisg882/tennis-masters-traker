import gspread
from art import text2art
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('tennis-masters')

art = text2art("Tennis Masters")
print(art)
print("Welcome to Tennis Masters. In this program you can update the results of every day match\n")

def score_results():
    """
    Get the results of the matches of the day
    """
    print("Insert todays results player by player:")
    while True:
        data = SHEET.worksheet('players-scores')
        # Get values of the player-scores worksheet
        get_all_rows = data.get_all_values()
        # Get the names of the players
        players = get_all_rows[0]
        # List of the scores
        scores = []

        """
        Loop through the players list and ask for the score for each player
        if they win the score 3 point, if they loss they score -1
        """
        for player in players:
            result = input(f"Insert the score of {player} (win/loss):").lower().strip()
            scores.append(result)

        if validate_results(scores):
            return scores  # Return the scores if validation succeeds
        else:
            print("Please try again.\n")

    
def validate_results(values):
    """
    Check if the values inserted in the results function are valid
    """
    try:
        int_results = []
        # for loop that converts "win" or "loss" to 3 or -1 respectively
        for value in values:
            if value == "win":
                int_results.append(3)
            elif value == "loss":
                int_results.append(-1)
            else:
                raise ValueError("Invalid input. Please enter 'win' or 'loss'.")

        # Check the number of values after all inputs are collected

        if sum(int_results) != 10:
            raise ValueError("There can only be 5 losers and 5 winners")
        
        return int_results

    except ValueError as e:
        print(f"Invalid data: {e}")
        


def update_worksheet(data, worksheet):
    """
    Update the worksheet with the new data inserted
    """
    print(f"Update the {worksheet} worksheet")
    update_worksheet = SHEET.worksheet(worksheet)
    update_worksheet.append_row(data)
    print(f"{worksheet} updated successfully\n")


def update_scoreboard(score):
    """
    Sum the results to the current scoreboard
    """
    scoreboard = SHEET.worksheet('total-score')

    #Get all the values
    all_rows = scoreboard.get_all_values()
    #Get the last row
    last_row = all_rows[-1]
    #Transform them in integers
    int_last_row = [int(num) if num else 0 for num in last_row]
    #Sum the results lis with the last row
    result = [x + y for x, y in zip(score, int_last_row)]
    return result
    

def position():
    """
    Identify and organize the players by their current score
    """
    scoreboard = SHEET.worksheet('total-score')

    # Same technique used in update_scoreboard to get the last row
    all_rows = scoreboard.get_all_values()
    last_row = all_rows[-1]

    # Sort the scores and keep track of player names
    scores = [int(score) if score else 0 for score in last_row]  
    player_names = all_rows[0] 

    # Combine player names and scores
    player_scores = list(zip(player_names, scores))

    # Sort the player_scores based on scores
    sorted_players = sorted(player_scores, key=lambda x: x[1], reverse=True)

    # Create a list of strings representing player positions and scores
    for index, player in enumerate(sorted_players):
          print(f"{index + 1} position {player[0]} with {player[1]} points")
    

def delete_matches():
    """
    Will delete the last row of the upcoming matches after updating the 
    scores of the day
    """
    dates = SHEET.worksheet('upcoming-matches')
    #Use delete_row() method to delete the first row and push up the other dates
    dates.delete_rows(1)
    

def today_match():
    """
    Prints today's matches
    """
    print("Today's matches:\n")
    match_sheet = SHEET.worksheet('upcoming-matches')

    # Get the values from the first row of the upcoming matches
    all_values = match_sheet.get_all_values()
    matches_of_the_day = all_values[0]

    # Print each non-empty match
    for match in matches_of_the_day:
         print(match)
   

def upcoming_matches():
    """
    Prints the upcoming matches
    """
    matches = SHEET.worksheet('upcoming-matches')

    all_values = matches.get_all_values()
    upcoming = []

    # Loop through the list of lists and add non-empty values to the upcoming list
    for date in all_values:
        for data in date:
            if data:
                upcoming.append(data)
    return upcoming
    

def main():
    """
    Run the program
    """
    while True:
        today_match()
        results = score_results()
        validated_results = validate_results(results)
        if validated_results is not None:
            update_worksheet(validated_results, "players-scores")
            scoreboard = update_scoreboard(validated_results)
            update_worksheet(scoreboard, "total-score")
            print("Leader Board:\n")
            position()
            delete_matches()
            
            # Check for upcoming matches
            upcoming = upcoming_matches()
            if not upcoming:
                print("There are no upcoming matches. Exiting...")
                break
            else:
                print("Next upcoming matches:\n")
                for match in upcoming:
                    print(match)
            
            # Ask user if they want to enter new results (with validation)
            while True:
                try:
                    choice = input("Do you want to enter new results? (yes/no): ").lower()
                    if choice not in ['yes', 'no']:
                        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                    break  # Break the loop if input is valid
                except ValueError as e:
                    print(f"Error: {e}")
            
            if choice != 'yes':
                print("Thank you for using the program. Exiting...")
                break
    
if __name__ == "__main__":
    main()