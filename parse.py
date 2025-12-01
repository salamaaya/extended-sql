import ply.yacc as yacc
from lex import tokens
from classes.esql import ESQL

"""this takes the tokens from lex.py and defines the grammar rules for parsing
and building the ESQL object."""

# operator precendence
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# rule: query = SELECT clause + FROM clause + [WHERE clause] + [GROUP BY clause] + [SUCH THAT clause] + [HAVING clause]
def p_query(p):
    '''query : select_clause from_clause where_clause_opt group_by_clause_opt such_that_clause_opt having_clause_opt'''
    p[0] = ESQL()
    p[0].add_select(p[1])
    p[0].from_tables = p[2]
    p[0].where = p[3]
    p[0].group_by = p[4]
    p[0].such_that = p[5]
    p[0].having = p[6]

def p_select_clause(p):
    '''select_clause : SELECT STAR
                     | SELECT id_list
                     | SELECT id_list COMMA aggregate_function_list'''
    if len(p) > 2:
        if isinstance(p[2], list):
            p[0] = p[2]
        else:
            p[0] = [p[2]]

        if len(p) == 5: # aggregate functions
            p[0] += [p[4]]
    else:
        p[0] = []

def p_from_clause(p):
    '''from_clause : FROM id_list'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

def p_where_clause_opt(p):
    '''where_clause_opt : WHERE condition_list
                        | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

def p_group_by_clause_opt(p):
    '''group_by_clause_opt : GROUP_BY id_list
                           | GROUP_BY id_list SEMICOLON id_list
                           | empty'''
    if len(p) > 2:
        p[0] = p[2]

        if len(p) == 5: # grouping vars
            p[0] += [p[4]] # separate with an identifier
    else:
        p[0] = []

def p_having_clause_opt(p):
    '''having_clause_opt : HAVING condition_list
                         | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

def p_such_that_clause_opt(p):
    '''such_that_clause_opt : SUCH_THAT condition_list
                            | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

def p_id_list(p):
    '''id_list : ID
               | id_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Expression rules (replace existing p_expression)
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression STAR expression
                  | expression DIVIDE expression'''
    p[0] = f'({p[1]} {p[2]} {p[3]})'

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = f'(-{p[2]})'

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_aggregate(p):
    'expression : aggregate_function'
    p[0] = p[1]

def p_condition(p):
    '''condition : expression EQUALS expression
                 | expression NOT_EQUAL expression
                 | expression GREATER expression
                 | expression LESS expression
                 | expression GREATER_EQUAL expression
                 | expression LESS_EQUAL expression
    '''
    p[0] = f'{p[1]} {p[2]} {p[3]}'

def p_condition_list(p):
    '''condition_list : condition
                      | condition_list AND condition
                      | condition_list OR condition
                      | condition_list COMMA condition'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]] + [p[3]]

def p_aggregate_function(p):
    '''aggregate_function : COUNT LPAREN ID RPAREN
                          | SUM LPAREN ID RPAREN
                          | AVG LPAREN ID RPAREN
                          | MAX LPAREN ID RPAREN
                          | MIN LPAREN ID RPAREN'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])

def p_aggregate_function_list(p):
    '''aggregate_function_list : aggregate_function
                               | aggregate_function_list COMMA aggregate_function'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# used for optional rules
def p_empty(p):
    '''empty :'''
    p[0] = None

# syntax error
def p_error(p):
    print("Syntax error at '%s'" % p)

parser = yacc.yacc()
