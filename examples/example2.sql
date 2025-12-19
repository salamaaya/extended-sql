with ny as (
    SELECT prod, max(quant) max_1_quant, min(quant) min_1_quant
    FROM sales
    WHERE state = 'NY' and quant > 0
    GROUP BY prod
),
nj as (
    SELECT prod, max(quant) max_2_quant, min(quant) min_2_quant
    FROM sales
    WHERE state = 'NJ' and quant > 0
    GROUP BY prod
)
SELECT ny.prod, max_1_quant, min_1_quant, max_2_quant, min_2_quant
FROM ny, nj
WHERE ny.prod = nj.prod;
