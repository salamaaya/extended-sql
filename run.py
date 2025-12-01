import getopt, sys
from lex import lexer
from parse import parser
from classes.phi import Phi

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
        lexer.input(esql)
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            print(tok)

    if verbose:
        print("=======PARSING=======")
    parsed_esql = parser.parse(esql)
    
    if verbose:
        print("ESQL Object:")
        print(parsed_esql)
    
    phi = Phi()
    phi.convert(parsed_esql)
    if verbose:
        print("Phi Operator:")
        print(phi)
    
if __name__ == "__main__":
    main()