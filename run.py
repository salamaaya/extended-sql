import getopt, sys
from lex import lexer
from parse import parser
from classes.phi import Phi
from generate import generator

def main():
    esql = ""
    verbose = False
    opt = 'Phi'
    phi = Phi()
    output = None
    verbose = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], ":vo:", ["help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for o, a in opts:
        if o == "-v":
            verbose = True
        if o == "-o":
            output = a
            print(output)
        if o == "-help":
            print("usage: python run.py [-v] [-help] [example.esql]")
            sys.exit()

    if args:
        file = args[0]
        with open(file, 'r') as f:
            esql = f.read()
            opt = 'ESQL'
    else: # take input
        while True:
            print("Choose an option:")
            option = input("1. ESQL\n2. Phi Operator\n")

            if option == '1':
                opt = 'ESQL'
                print("Type 'done' to exit.")
                while True:
                    line = input()
                    if line.strip().lower() == "done":
                        break
                    esql += line + "\n"
                break
            
            elif option == '2':
                """
                1. s - projected columns / expressions
                2. n - number of grouping variables
                3. V - grouping attributes: {self.v}
                4. F-VECT - vector of aggregate functions: {self.f_vect}
                5. PRED-LIST - list of predicates for grouping var's: {self.pred_list}
                6. HAVING: {self.having}"""

                s = input('1. s - projected columns / expressions (separated list by commas): ')
                if s != 'None':
                    s = s.strip().split(',')
                    phi.s = s

                n = input('2. n - number of grouping variables (int): ')
                n = int(n)
                if n > 0:
                    phi.n = n

                v = input('3. v - grouping attributes (separated list by commas): ')
                if v != 'None':
                    v = v.strip().split(',')
                    phi.v = v

                f_vect = input('4. F-VECT - vector of aggregate functions (separated list by commas): ')
                if f_vect != 'None':
                    f_vect = f_vect.strip().split(',')
                    phi.f_vect = f_vect

                pred_list = input("5. PRED-LIST - list of predicates for grouping var's (separated list by commas): " )
                if pred_list != 'None':
                    pred_list = pred_list.strip().split(',')
                    phi.pred_list = pred_list

                having = input('6. HAVING: ')
                if having != 'None':
                    having = having.strip().split(',')
                    phi.having = having
                
                break
            else:
                print("Invalid option, try again.")

    if opt == 'ESQL':
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
            phi.convert(parsed_esql)
    
    if verbose:
        print("=======Phi Operator=======")
        print(phi)

    generator.generate(phi, output_file=output)
    
if __name__ == "__main__":
    main()
