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

def score_results():
    """
    Get the results of the matches of the day
    """
    while True:
        results = input("Enter the matches results (-1 for the loser and 3 for the winner):\n")

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
        if len(int_results) != 4:
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
        if sum(int_results) != 4:
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
    print(f"Update the {worksheet} worksheet\n")
    update_worksheet = SHEET.worksheet(worksheet)
    update_worksheet.append_row(data)
    print(f"{worksheet} updated successfully")


def update_scoreboard(score):
    """
    Sum the results to the current scoreboard
    """
    scoreboard = SHEET.worksheet('total-socore')

    #Get all the values
    all_rows = scoreboard.get_all_values()
    #Get the last row
    last_row = all_rows[-1]
    #Transform them in integers
    int_last_row = [int(num) for num in last_row]
    #Sum the results lis with the last row
    result = [x + y for x, y in zip(score, int_last_row)]
    print(result)
    


    



def main():
    """
    Run the program
    """
    results = score_results()
    results_data = [int(num) for num in results]
    print(results_data)
    update_worksheet(results_data, "players-scores")


#main()
update_scoreboard([-1,3,-1,3,-1,3,-1,3,-1,3])