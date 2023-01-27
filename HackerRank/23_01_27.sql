--Binary Tree Nodes
select n, 
case
when p is null then 'Root'
when n not in (select distinct(p) from bst where p is not null) then 'Leaf'
else 'Inner' end
from bst
order by n;

--Type of Triangle
select
case
when a+b<=c or a+c<=b or b+c<=a then 'Not A Triangle'
when a!=b and b!=c and a!=c then 'Scalene'
when a=b and b=c then 'Equilateral'
else 'Isosceles' end
from triangles;