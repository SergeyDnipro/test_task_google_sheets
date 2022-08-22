from googleapiclient.discovery import build
from google.oauth2 import service_account
from decimal import Decimal
from django.conf import settings


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT = settings.SERVICE_ACCOUNT
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Iw8gvaRMcO5Y-usLODoNCLYGVfFrfX0Frc_3Ql6DCb8'
SAMPLE_RANGE_NAME = 'list1!A2:D'


def list_to_dict(lst):  # Transformation "list" get_google_sheets fields to named "dict" fields
    new_values = []
    for line in lst:
        new_values.append({'excel_id': line[0],
                           'order_id': line[1],
                           'price_usd': line[2],
                           'price_uah': Decimal(line[2]),
                           'delivery_date': line[3],
                           'msg_status': False})
    return new_values


def get_google_sheets():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    return list_to_dict(values)

