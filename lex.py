import ply.lex as lex

# List of token names
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'GROUP_BY',
    'HAVING',
    'SUCH_THAT',
    'AND',
    'OR',
    'NOT',
    'TRUE',
    'FALSE',
    'NULL',
    'COUNT',
    'SUM',
    'AVG',
    'MAX',
    'MIN',
    'VARIABLE',
    'COMMA',
    'PLUS',
    'MINUS',
    'STAR',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'NOT_EQUAL',
    'NUMBER',
    'QUOTE',
    'DOT',
    'SEMICOLON',
    'DATE',
    'STRING',
    'GROUPING_VARIABLE'
)

reserved = {
    # SQL keywords
    'select'    : 'SELECT',
    'SELECT'    : 'SELECT',
    'from'      : 'FROM',
    'FROM'      : 'FROM',
    'where'     : 'WHERE',
    'WHERE'     : 'WHERE',
    'having'    : 'HAVING',
    'HAVING'    : 'HAVING',
    # note: 'group by' and 'such that' are handled in separate functions due to spaces

    # Logical operators
    'and'       : 'AND',
    'AND'       : 'AND',
    'or'        :  'OR',
    'OR'        :  'OR',
    'not'       : 'NOT',
    'NOT'       : 'NOT',
    'true'      : 'TRUE',
    'TRUE'      : 'TRUE',
    'false'     : 'FALSE',
    'FALSE'     : 'FALSE',
    'null'      : 'NULL',
    'NULL'      : 'NULL',

    # Aggregate functions
    'COUNT'    : 'COUNT',
    'count'    : 'COUNT',
    'SUM'      : 'SUM',
    'sum'      : 'SUM',
    'AVG'      : 'AVG',
    'avg'      : 'AVG',
    'MAX'      : 'MAX',
    'max'      : 'MAX',
    'MIN'      : 'MIN',
    'min'      : 'MIN',
}

# Regular expression rules for simple tokens
'''punctuation'''
t_QUOTE  = r'\''
t_SEMICOLON = r';'
t_STAR   = r'\*'
t_DOT    = r'\.'

'''strings and identifiers'''
t_COMMA  = r','
t_DATE = r'\'\d{4}-\d{2}-\d{2}\''
t_STRING = rf'{t_QUOTE}([^\\{t_QUOTE}]|\\.)*{t_QUOTE}'

'''arithmetic and boolean operators'''
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALS  = r'='
t_GREATER = r'>'
t_LESS    = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_NOT_EQUAL = r'!=|<>'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_GROUP_BY(t):
    r'(GROUP \ BY)|(group \ by)'
    t.type = 'GROUP_BY'
    return t

def t_SUCH_THAT(t):
    r'(SUCH \ THAT)|(such \ that)'
    t.type = 'SUCH_THAT'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VARIABLE')    # Check for reserved words
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
def lexer():
    return lex.lex()
