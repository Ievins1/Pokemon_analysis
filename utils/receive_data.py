import os
import requests
import pandas as pd
from dotenv import load_dotenv
from io import StringIO

# Ielādē .env failā saglabāto mainīgo
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

# Funkcija, kas atgriež datus, no dotās saites
def fetch_pokemon_data():
    url = os.getenv("data_url")
    if not url:
        raise ValueError("data_url nav atrasts .env failā.")

    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Neizdevās ielādēt datus. Statusa kods: {response.status_code}")

    # Pārvērš CSV tekstu par pandas DataFrame
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data, on_bad_lines='skip')  # Ignorē nepareizās rindas - piemēram, 1043 rindā ir par daudz vērtības dotas

    return df

# Pārbaudei, ka dati tiek atgriezti
if __name__ == "__main__":
    df = fetch_pokemon_data()
    print(df.head())
    print(f"Atgriezto rindas skaits: {len(df)}")
    print(f"Kolonnu skaits: {len(df.columns)}")
