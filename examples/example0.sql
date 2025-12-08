with ny as (
    SELECT cust, count(quant) count_1_quant
    FROM sales
    WHERE state = 'NY'
    GROUP BY cust
),
nj as (
    SELECT cust, sum(quant) sum_2_quant
    FROM sales
    WHERE state = 'NJ'
    GROUP BY cust
),
ct as (
    SELECT cust, max(quant) max_3_quant
    FROM sales
    WHERE state = 'CT'
    GROUP BY cust
)
SELECT ny.cust, count_1_quant, sum_2_quant, max_3_quant
FROM ny, nj, ct
WHERE ny.cust = nj.cust AND nj.cust = ct.cust;