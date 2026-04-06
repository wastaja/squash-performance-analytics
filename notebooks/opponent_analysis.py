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

query = f"""
select
    opponent_name
    , count(*) as total_matches
    , sum(is_win) as won_matches
    , round(sum(is_win) * 1.0 / count(*), 2) as win_rate
    , round(avg(duration_min), 1) as avg_duration_min
    , round(avg(my_energy_level), 1) as avg_energy_level
    , round(avg(games_won_by_me), 1) as avg_games_won_by_me
    , round(avg(games_won_by_opponent), 1) as avg_games_won_by_opponent
from fact_matches
where is_scored_match = 1
  and opponent_name = '{selected_opponent}'
group by opponent_name
"""

result = con.execute(query).df()

print("\nOpponent summary:\n")
print(result.to_string())