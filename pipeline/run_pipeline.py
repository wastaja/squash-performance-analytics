import duckdb

con = duckdb.connect("data/squash.db")

# RAW
con.execute("""
    create or replace view matches as
    select * from read_csv_auto('data/matches.csv')
""")

# STAGING
with open('sql/staging/stg_matches.sql') as f:
    staging_query = f.read()

con.execute(f"""
    create or replace view stg_matches as
    {staging_query}
""")

# FACT
with open('sql/marts/fact_matches.sql') as f:
    fact_query = f.read()

con.execute(f"""
    create or replace view fact_matches as
    {fact_query}
""")

print("Pipeline executed successfully.")