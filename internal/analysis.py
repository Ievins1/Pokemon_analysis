import pandas as pd
import json
import os

def load_type_chart(path=None):
    """
    Loads the Pokémon type effectiveness chart from a JSON file.
    
    Returns:
        dict: Type effectiveness multipliers, like type_chart['Fire']['Grass'] = 2.0
    """
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "type_chart.json")
    with open(path, "r") as f:
        return json.load(f)

def get_type_multiplier(attacker_type, defender_type, type_chart):
    """
    Returns the effectiveness multiplier of one type against another.
    
    If no match is found, returns 1.0 (neutral).
    """
    if attacker_type in type_chart and defender_type in type_chart[attacker_type]:
        return type_chart[attacker_type][defender_type]
    return 1.0  # Default neutral effectiveness if no specific interaction

# Calculates the overall effectiveness between attacker and defender (supports up to 2 types each)
def calculate_effectiveness(attacker_types, defender_types, type_chart):
    """
    Calculates how effective one Pokémon is against another based on their types.

    Returns the average effectiveness across all attacker's types.
    """
    multiplier = 1.0
    for atk_type in attacker_types:
        if atk_type is None or atk_type == "":
            continue
        type_multiplier = 1.0
        for def_type in defender_types:
            if def_type is None or def_type == "":
                continue
            type_multiplier *= get_type_multiplier(atk_type, def_type, type_chart)
        multiplier += type_multiplier
    return multiplier / len(attacker_types)  # Average effectiveness across both attacker's types

def rank_pokemons_by_type_strength(pokemon_df, type_chart):
    """
    Compares each Pokémon against all others based on type effectiveness.

    Adds a 'TYPE_EFFECTIVENESS_SCORE' column and sorts the DataFrame.
    """
    effectiveness_scores = []

    for i, attacker in pokemon_df.iterrows():
        attacker_types = [attacker['TYPE1'], attacker['TYPE2']]
        score = 0

        for j, defender in pokemon_df.iterrows():
            if i == j:
                continue  # Skip self-comparison
            defender_types = [defender['TYPE1'], defender['TYPE2']]
            score += calculate_effectiveness(attacker_types, defender_types, type_chart)

        effectiveness_scores.append(score)

    pokemon_df['TYPE_EFFECTIVENESS_SCORE'] = effectiveness_scores
    ranked = pokemon_df.sort_values(by='TYPE_EFFECTIVENESS_SCORE', ascending=False).reset_index(drop=True)
    return ranked
