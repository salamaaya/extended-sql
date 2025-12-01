import sys
from lex import lexer

def main():
    esql = ""

    if len(sys.argv) != 2: # take input
        print("ESQL Code (type done to execute):")
        while True:
            line = input()
            if line.strip().lower() == "done":
                break
            esql += line + "\n"
    elif len(sys.argv) == 2: # input from .esql file
        file = sys.argv[1]
        with open(file, 'r') as f:
            esql = f.read()

    esql_lexer = lexer()

    # Give the lexer esql
    esql_lexer.input(esql)

    # Tokenize
    while True:
        tok = esql_lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
if __name__ == "__main__":
    main()