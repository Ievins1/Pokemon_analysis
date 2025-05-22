import gspread
from oauth2client.service_account import ServiceAccountCredentials

# === CONFIG ===
SERVICE_ACCOUNT_FILE = "../service_account.json"

# === AUTH ===
def authorize_gspread():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
    return gspread.authorize(creds)
