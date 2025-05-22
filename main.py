import pandas as pd
from utils.receive_data import fetch_pokemon_data
from internal.analysis import load_type_chart, rank_pokemons_by_type_strength

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

    # Show Top 10 Pokémon sorted by ascending rank
    top_10 = grouped.sort_values(by="RANK").head(10)
    print(top_10[['RANK', 'NAME', 'TYPE1', 'TYPE2', 'TYPE_EFFECTIVENESS_SCORE']])
