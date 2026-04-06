import duckdb

con = duckdb.connect("../data/squash.db")

# raw
con.execute("""
    create or replace view matches as
    select * from read_csv_auto('../data/matches.csv')
""")

# staging
with open('../sql/staging/stg_matches.sql', 'r') as f:
    staging_query = f.read()

con.execute(f"""
    create or replace view stg_matches as
    {staging_query}
""")

# marts (fact)
with open('../sql/marts/fact_matches.sql', 'r') as f:
    fact_query = f.read()

con.execute(f"""
    create or replace view fact_matches as
    {fact_query}
""")

# preview
df = con.execute("""
    select *
    from fact_matches
    limit 5
""").df()

print(df)
 
# analysis - win rate
with open('../sql/analysis/overall_win_rate.sql', 'r') as f:
    analysis_query = f.read()

result = con.execute(analysis_query).df()

print("\nOverall win rate:\n")
print(result)

# analysis - win rate by opponent
with open('../sql/analysis/win_rate_by_opponent.sql', 'r') as f:
    opponent_query = f.read()

opponent_result = con.execute(opponent_query).df()

print("\nWin rate by opponent:\n")
print(opponent_result)


# analysis - win rate monthly
with open('../sql/analysis/monthly_win_rate.sql', 'r') as f:
    monthly_query = f.read()

monthly_result = con.execute(monthly_query).df()

print("\nMonthly win rate:\n")
print(monthly_result)