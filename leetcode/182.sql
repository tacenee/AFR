# Write your MySQL query statement below
select Email from Person Group by Email HAVING count(Email)>1