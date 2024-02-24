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
    results = input("Enter the matches results (-1 for the losser and 3 for the winner):\n")

    results_data = results.split(",")

    if validete_results()


def validete_results(values):
    """
    Check if the values inserted in the results function are valid
    """
    try:
        int_results = []
        for value in values:
            int_results.append(int(value))
        if len(int_results) != 10:
            raise ValueError(
                f"Exactly 10 values required, you provide {len(values)}"
            )
        for result in int_results:
            if result != -1 or result != 3:
                raise ValueError(
                    f"The result can only have a value of -1 or 3, you provide {result}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
