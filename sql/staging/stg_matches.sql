select
    match_id::int as match_id
    , match_date::date as match_date
    , opponent_name
    , match_type
    , location

    , games_won_by_me::int as games_won_by_me
    , games_won_by_opponent::int as games_won_by_opponent
    , coalesce(games_won_by_me, 0) + coalesce(games_won_by_opponent, 0) as games_total

    , duration_min::int as duration_min
    , my_energy_level::int as my_energy_level
    , opponent_level::int as opponent_level

    , case
        when match_type = 'training' then null
        when games_won_by_me > games_won_by_opponent then 1
        when games_won_by_me < games_won_by_opponent then 0
        else null
    end as is_win

from matches