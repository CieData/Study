--Occupations
select
    min(case when occupation='Doctor' then name end),
    min(case when occupation='Professor' then name end),
    min(case when occupation='Singer' then name end),
    min(case when occupation='Actor' then name end)
from (select *,row_number() over (partition by occupation order by name) a from occupations) b
group by a