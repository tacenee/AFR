#统计（去重）比我大的分数的个数就是我的排名
# Write your MySQL query statement below
select a.Score Score,(select count(distinct b.Score) from Scores b where b.Score>= a.Score ) Rank from Scores a order by Score desc