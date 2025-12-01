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

# References

The lexer and parser were inspired by the examples at https://www.dabeaz.com/ply/ply.html#ply_nn9