--Weather Observation Station 18
select round(abs(max(lat_n)-min(lat_n))+abs(max(long_w)-min(long_w)),4)
from station;

--Weather Observation Station 19
select 
round(sqrt(pow((max(lat_n)-min(lat_n)),2)+pow((max(long_w)-min(long_w)),2)),4)
from station;

--Weather Observation Station 20
select round(lat_n,4)
from (select lat_n, percent_rank() over (order by lat_n) as percent
      from station) as A
where A.percent=0.5;
