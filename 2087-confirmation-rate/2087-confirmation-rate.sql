# Write your MySQL query statement below

select s.user_id, 
    ROUND(
        AVG(
            CASE 
                WHEN c.action = 'confirmed' THEN 1.00
                ELSE 0
            END
        ), 2) AS confirmation_rate

from signups s left join confirmations c on s.user_id = c.user_id group by s.user_id;

