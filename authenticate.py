from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from numpy import empty
import os
from dotenv import load_dotenv
load_dotenv()

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# ID para a planilha e range de leitura da planilha.
SAMPLE_SPREADSHEET_ID = os.environ['spreadsheet']
SAMPLE_RANGE_NAME = 'data!A2:D100'


def check_sheet_size(values):
    spreadsheet_width = len(values)
    return(spreadsheet_width)


def authenticate_with_google():  # validate with google

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'chave.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()  # take sheet values
        values = result.get('values', [])
        spreadsheet_width = check_sheet_size(values)

    except HttpError as err:  # apenas mensagem de erro
        print(err)
    return(values, spreadsheet_width)


values = authenticate_with_google()
