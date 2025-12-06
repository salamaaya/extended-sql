# Extended SQL 

A simple query processor for EMF Queries, allowing aggregation over the same group.

# Usage

- Install requirements:
```
pip install -r requirements.txt
```

- To run an ESQL query:
```
python run.py [-v] [example.esql]
```

* If the ```-v``` option is provided, verbose output will be printed, such as lexing and parsing.

* ```example.esql``` is an optional argument, if it is provided,
input will be read from the file. Otherwise, you are asked to provide valid esql input. To terminate input, simply type "done".

* If no file is provided as argument, you will get the following output when run: 
```Choose an option:
1. ESQL
2. Phi Operator
```
If you choose 1, type the ESQL query and type "done" when you're done. This is equivalent to putting the query in a ```.esql``` file. If you press 2, you will be asked to provide the 6 differen arguments to Phi.

# References

The lexer and parser were inspired by the examples at https://www.dabeaz.com/ply/ply.html#ply_nn9
