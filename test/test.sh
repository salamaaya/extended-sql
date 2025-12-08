#!/bin/bash

mkdir output

for i in $(seq 0 5);
do
    python ../run.py ../examples/example${i}.esql 2>/dev/null | sort > output/ex${i}.esql.out
    python sql.py ../examples/example${i}.sql 2>/dev/null | sort  > output/ex${i}.sql.out
    DIFF="$(diff output/ex${i}.esql.out output/ex${i}.sql.out 2>/dev/null)"
    echo ========================================================================
    if [[ -z ${DIFF} ]]; then
        echo "Test ${i}: passed"
    else
        echo "Test ${i}: failed"
        echo "diff output:"
        echo "${DIFF}"
    fi
done

rm -rf output