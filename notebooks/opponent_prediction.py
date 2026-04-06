import duckdb
import pandas as pd

pd.set_option('display.max_columns', None)

selected_opponent = input("Enter opponent name: ")

con = duckdb.connect("data/squash.db")

# raw
con.execute("""
    create or replace view matches as
    select * from read_csv_auto('data/matches.csv')
""")

# staging
with open('sql/staging/stg_matches.sql', 'r') as f:
    staging_query = f.read()

con.execute(f"""
    create or replace view stg_matches as
    {staging_query}
""")

# marts
with open('sql/marts/fact_matches.sql', 'r') as f:
    fact_query = f.read()

con.execute(f"""
    create or replace view fact_matches as
    {fact_query}
""")

# prediction components
with open('sql/analysis/opponent_prediction_components.sql', 'r') as f:
    components_query = f.read()

components_df = con.execute(components_query).df()

row = components_df[components_df['opponent_name'] == selected_opponent]

if row.empty:
    print("\nNo data for this opponent.")
else:
    row = row.iloc[0]

    historical_win_rate = row['historical_win_rate']
    recent_win_rate = row['recent_win_rate']
    normalized_energy = row['normalized_energy']
    avg_games_diff = row['avg_games_diff']
    normalized_games_diff = max(min((avg_games_diff + 5) / 10, 1), 0)

    # fallback if recent_win_rate is null
    if pd.isna(recent_win_rate):
        recent_win_rate = historical_win_rate

    prediction_score = (
        0.4 * historical_win_rate
        + 0.25 * recent_win_rate
        + 0.15 * normalized_energy
        + 0.20 * normalized_games_diff
    )

    print("\nPrediction components:\n")
    print(row.to_string())
    print(f"\nNormalized games diff: {round(normalized_games_diff, 2)}")
    
    print("\nPrediction:\n")
    print(f"Opponent: {selected_opponent}")
    print(f"Win probability score: {round(prediction_score, 2)}")

    if prediction_score >= 0.65:
        interpretation = "High chance of winning"
    elif prediction_score >= 0.45:
        interpretation = "Moderate / competitive match"
    else:
        interpretation = "Low chance of winning"

    print(f"Interpretation: {interpretation}")