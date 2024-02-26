import gspread
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

print("Welcom to Tennis Masters. In this program you can update the results of every day match\n")
print("Wen you add the results they will be assigned in the following order:\nJhon Mcenroe	-- Rafael Nadal -- Roger Federer -- Novak Djokovic -- Andre Agassi -- Pete Sampras -- Rod Laver -- Bjorn Borg -- Jimmi Connors -- Ivan Lendl")

def score_results():
    """
    Get the results of the matches of the day
    """
    while True:
        results = input("Enter the results, each result separeted by a coma, for example -1,3,-1... (-1 for the loser and 3 for the winner):\n")

        results_data = results.split(",")

        if validate_results(results_data):
            print("Correct data!")
            break
    return results_data


def validate_results(values):
    """
    Check if the values inserted in the results function are valid
    """
    try:
        
        int_results = []
        #for loop that adds the values of the results as integers on the int_results list
        for value in values:
            int_results.append(int(value))
        #Checks that the lenght of the result added are a total of 10
        if len(int_results) != 10:
            raise ValueError(
                f"Exactly 10 values required, you provided {len(values)}"
            )
        
        #Checks that the values in the results are only -1 and 3
        for result in int_results:
            if result not in [-1, 3]:  
                raise ValueError(
                    f"The result can only have a value of -1 or 3, you provided {result}"
                )
        
        """
        Checks that there is exactly 5 winners and 5 lossers by 
        taking the sum of the int-Results and see if its a total of 10 
        (5 winers mean 3 times 5 meaning 15, 5 
        lossers mean -5. 15 winners - 5 lossers = 10)
        """
        if sum(int_results) != 10:
            raise ValueError(
                f"There can only be 5 lossers and 5 winners"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


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
        print(f"{index + 1} position {player[0]} with {player[1]} score")
    

def delete_matches():
    """
    Will delete the last row of the upcoming matches after updating the 
    scores of the day
    """
    dates = SHEET.worksheet('upcoming-matches')
    print("Update upcoming matches\n")
    #Use delete_row() method to delete the first row and push up the other dates
    dates.delete_rows(1)
    

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
        results = score_results()
        results_data = [int(num) for num in results]
        print(results_data)
        update_worksheet(results_data, "players-scores")
        scoreboard = update_scoreboard(results_data)
        update_worksheet(scoreboard, "total-score")
        print(f"{scoreboard}\n")
        print("Leader board\n")
        position()
        delete_matches()
        
        # Check for upcoming matches
        upcoming = upcoming_matches()
        if not upcoming:
            print("There are no upcoming matches. Exiting...")
            break
        else:
            print("Next upcoming matches:")
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
    
main()
