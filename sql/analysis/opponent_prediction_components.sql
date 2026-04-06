select
    opponent_name

    -- overall performance vs opponent
    , round(sum(is_win) * 1.0 / count(*), 2) as historical_win_rate

    -- recent form (last 5 matches vs opponent)
    , round(
        sum(is_win) filter (where match_date >= (
            select max(match_date) - interval '60 days' from fact_matches
        )) * 1.0
        /
        count(*) filter (where match_date >= (
            select max(match_date) - interval '60 days' from fact_matches
        ))
    , 2) as recent_win_rate

    -- avg energy
    , round(avg(my_energy_level) / 5.0, 2) as normalized_energy
    , round(avg(games_won_by_me - games_won_by_opponent), 2) as avg_games_diff

from fact_matches
where is_scored_match = 1
group by opponent_name