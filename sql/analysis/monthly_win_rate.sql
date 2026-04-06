select
    date_trunc('month', match_date) as month_nr
    , count(*) as total_matches
    , sum(is_win) as won_matches
    , round(sum(is_win) * 1.0 / count(*), 2) as win_rate
from fact_matches
where is_scored_match = 1
group by 1
order by 1