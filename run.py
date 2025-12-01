import getopt, sys
from lex import lexer
from parse import parser


def main():
    esql = ""
    verbose = False 

    try:
        opts, args = getopt.getopt(sys.argv[1:], ":v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
    
    if args:
        file = args[0]
        with open(file, 'r') as f:
            esql = f.read()
    else: # take input
        print("ESQL Code (type done to execute):")
        while True:
            line = input()
            if line.strip().lower() == "done":
                break
            esql += line + "\n"

    if verbose:
        print("=======LEXING=======")
    esql_lexer = lexer()
    esql_lexer.input(esql)

    # Tokenize
    while True:
        tok = esql_lexer.token()
        if not tok: 
            break      # No more input
        if verbose:
            print(tok)

    if verbose:
        print("=======PARSING=======")
    esql_parser = parser()
    parsed = esql_parser.parse(esql)
    
    if verbose:
        print(parsed)
    
if __name__ == "__main__":
    main()