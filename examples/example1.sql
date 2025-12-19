with y19 as (
    SELECT cust, sum(quant) sum_1_quant
    FROM sales
    WHERE year = 2019
    GROUP BY cust
),
large as (
    SELECT cust, count(quant) count_2_quant
    FROM sales
    WHERE quant > 50
    GROUP BY cust
),
p1 as (
    SELECT cust, max(quant) max_3_quant
    FROM sales
    WHERE prod = 'Apple'
    GROUP BY cust
)
SELECT y19.cust, sum_1_quant, count_2_quant, max_3_quant
FROM y19, large, p1
WHERE y19.cust = large.cust AND large.cust = p1.cust;