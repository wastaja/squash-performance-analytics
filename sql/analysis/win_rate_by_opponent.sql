select
    opponent_name
    , count(*) as total_matches
    , sum(is_win) as won_matches
    , round(sum(is_win) * 1.0 / count(*), 2) as win_rate
from fact_matches
where is_scored_match = 1
group by opponent_name
order by win_rate desc