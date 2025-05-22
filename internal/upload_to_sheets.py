import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import sys
import os

# To receive needed information from other directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.google_utils import authorize_gspread
from utils.receive_data import fetch_pokemon_data
from internal.analysis import load_type_chart, rank_pokemons_by_type_strength

# Needed google data
SHEET_ID = "1Uaxs3paVT9QI74wKAlyz0KSXsB8g8m7fq3hFSxt9G7o"
WORKSHEET_NAME = "Pokemon_Ranking"

# Upload the data to google sheet
def upload_dataframe_to_sheet(df, sheet_id, worksheet_name):
    client = authorize_gspread()
    sheet = client.open_by_key(sheet_id)

    try:
        worksheet = sheet.worksheet(worksheet_name)
        worksheet.clear()
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=worksheet_name, rows=1050, cols=30)

    set_with_dataframe(worksheet, df)
    print(f"Data uploaded to '{worksheet_name}' in Google Sheet.")

# === MAIN ===
if __name__ == "__main__":
    df = fetch_pokemon_data()
    type_chart = load_type_chart()
    ranked_df = rank_pokemons_by_type_strength(df, type_chart)

    # Group by NAME and calculate average effectiveness (for the "best Pokémon overall" task)
    grouped = ranked_df.groupby("NAME", as_index=False).agg({
        "TYPE_EFFECTIVENESS_SCORE": "mean",
        "GENERATION": "min",
        "LEGENDARY": "max",
        "TYPE1": "first",
        "TYPE2": "first"
    })

    # Assign ranks after grouping
    grouped["RANK"] = grouped["TYPE_EFFECTIVENESS_SCORE"].rank(ascending=False, method="dense").astype(int)

    upload_dataframe_to_sheet(grouped, SHEET_ID, WORKSHEET_NAME)
