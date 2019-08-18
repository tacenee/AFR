# Write your MySQL query statement below
select
        (select DISTINCT
                Salary
            from
                Employee
            order by Salary DESC
            limit 1,1)as SecondHighestSalary