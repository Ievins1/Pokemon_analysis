# Tasks that are done
### 1. Collect information about Pokemons:**
- **Easy mode:** Write a script which will request information from this link: https://gist.github.com/simsketch/1a029a8d7fca1e4c142cbfd043a68f19
### 2. Find the Pokemon which is the most effective companion through all generations (rank the pokemons from best to worst):
- **Normal mode:** Using Pandas or any SQL (python library), write an analytic script which will rank Pokemons by their type's strength (which pokemon is the most effective against all others). Here is a pokemon Type chart for comparison: https://img.pokemondb.net/images/typechart.png
### 3. Create a dashboard according to your vision, adding the rank position, so the user could filter data and see which type of Pokemon is the most suited for him:
- **Normal mode:** Using Google Spreadsheets and Google Looker Studio


# Files/directories purpose
### Additional files
- .env - contains the needed url to receive pokemon data
- .gitignore
- README.md
- main.py - the main script file that runs all the needed functions in order to get calculations

### Utils
This directory contains functions that creates connection to google or the data receiving git link
- receive_data.py - creates connection with the link from .env and returns all data
- google_utils.py - creates connection with google in order to automatically send data to google sheets

### Internal directory
This directory contains inner functions that are needed:
- analysis.py - contains functions taht are needed for calculation to determine the best pokemons
- upload_to_sheets.py - contains needed functions to automatically store the data inside the google sheets. For this to succesfully work 'service_account.json' is needed - all the required secrets for google.
- type_chart.json - stored pokemon type chart data from: https://img.pokemondb.net/images/typechart.png

# Instruction how to run
### Required packages that needs to be installed:
'pip3 install pandas python-dotenv requests'
#### Optional libraries - Used them to automatically store data inside google sheets
'pip3 install gspread gspread_dataframe oauth2client'
### To receive top 10 ranking, from the main directory run this command:
'python3 main.py'
The results will be shown in terminal. The full results are available inside the google docs. The automatical storing inside the google is not working for others, because I used personal google data in 'secret_account.json'

# Created Google links:
- Google sheets: https://docs.google.com/spreadsheets/d/1Uaxs3paVT9QI74wKAlyz0KSXsB8g8m7fq3hFSxt9G7o/edit?usp=sharing
- Google Looker Studio: https://lookerstudio.google.com/reporting/b7e949cb-bd28-4d0b-a58f-a21666cf3a06
