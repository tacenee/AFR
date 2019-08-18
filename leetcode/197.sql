# Write your MySQL query statement below
select weather.id from weather join weather w on DATEDIFF(weather.RecordDate,w.RecordDate) = 1 and weather.Temperature > w.Temperature 