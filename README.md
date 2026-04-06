# 🏓 Squash Performance Analytics

> Personal analytics project focused on building a lightweight data pipeline and prediction model for squash performance tracking.

## 📌 Overview

This project is an end-to-end analytics pipeline built to track and analyze personal squash performance.

It transforms raw match data into analysis-ready datasets and applies a simple, interpretable prediction model to estimate win probability against specific opponents.

The goal of the project is to demonstrate practical skills in:
- SQL-based data modeling
- analytics engineering
- lightweight data pipeline orchestration
- combining SQL and Python for analysis and scoring

---

## 🧱 Architecture

The project follows a layered analytics structure:

```
data (CSV)
   ↓
RAW (DuckDB view)
   ↓
STAGING (cleaned & typed data)
   ↓
MART (fact table with metrics)
   ↓
ANALYSIS (aggregations & insights)
   ↓
PYTHON (prediction logic)
```

---

## ⚙️ Tech Stack

- **SQL** – data transformations and modeling  
- **DuckDB** – local analytical data warehouse  
- **Python** – pipeline execution and prediction logic  
- **Pandas** – working with query results  
- **Makefile** – simple pipeline orchestration  

---

## 🚀 How to Run

### 1. Run the data pipeline

```bash
make run
```

Builds:
- raw view from CSV
- staging model
- fact table

---

### 2. Run analysis

```bash
make analysis
```

Example outputs:
- overall win rate
- win rate by opponent
- monthly performance

---

### 3. Run prediction

```bash
make predict
```

You will be asked to input an opponent name:

```
Enter opponent name: Raisa
```

Example output:

```
Prediction:
Opponent: Raisa
Win probability score: 0.45
Interpretation: Low chance of winning
```

---

## 📊 Data Model

### `stg_matches`
- cleaned and typed dataset
- basic transformations
- win flag (`is_win`)

### `fact_matches`
- enriched dataset with:
  - total games
  - match indicators
  - normalized metrics
  - flags for analysis

---

## 🧠 Prediction Logic

The prediction model is a simple weighted scoring system based on:

- historical win rate  
- recent performance (last ~60 days)  
- average energy level  
- average games difference  

```
score =
  0.4 * historical_win_rate +
  0.25 * recent_win_rate +
  0.15 * normalized_energy +
  0.20 * normalized_games_diff
```

The model is intentionally simple and interpretable.

---

## 📈 Example Insights

From the dataset:

- Performance varies significantly by opponent  
- Recent form can differ from historical averages  
- Energy level has a visible impact on outcomes  
- Some opponents show consistently low win probability  

---

## 🎯 What This Project Demonstrates

- building a **modular analytics pipeline**
- structuring data into **staging and marts layers**
- transforming raw data into **analysis-ready datasets**
- combining SQL and Python in a realistic workflow
- implementing a simple **interpretable scoring model**
- orchestrating execution with a **Makefile**

---

## 🔮 Possible Improvements

- data quality checks (e.g. null validation, constraints)  
- storing tables instead of views (materialization)  
- adding a dashboard (e.g. Streamlit or Power BI)  
- replacing scoring model with ML (e.g. logistic regression)  
- scheduling pipeline runs  

---

## 📁 Project Structure

```
.
├── data/
│   ├── matches.csv
│   └── squash.db
├── pipeline/
│   └── run_pipeline.py
├── sql/
│   ├── staging/
│   ├── marts/
│   └── analysis/
├── notebooks/
│   ├── run_analysis.py
│   ├── opponent_analysis.py
│   └── opponent_prediction.py
├── Makefile
└── README.md
```