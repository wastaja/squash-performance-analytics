select
    match_id
    , match_date
    , opponent_name
    , match_type
    , location
    , games_won_by_me
    , games_won_by_opponent
    , games_total
    , duration_min
    , my_energy_level
    , opponent_level
    , is_win

    , case
        when match_type = 'friendly match' then 1
        else 0
      end as is_scored_match

from stg_matches