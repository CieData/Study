--New Companies
select c.company_code,c.founder,
    count(distinct(lm.lead_manager_code)),
    count(distinct(sm.senior_manager_code)),
    count(distinct(m.manager_code)),
    count(distinct(e.employee_code))
from company c
    inner join lead_manager lm
    on c.company_code=lm.company_code
    inner join senior_manager sm
    on lm.lead_manager_code=sm.lead_manager_code
    inner join manager m
    on sm.senior_manager_code=m.senior_manager_code
    inner join employee e
    on m.manager_code=e.manager_code
group by c.company_code,c.founder
order by c.company_code;