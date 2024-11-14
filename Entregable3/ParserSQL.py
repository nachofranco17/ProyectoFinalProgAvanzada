import ply.yacc as yacc
from Lexer.LexerMain import get_lexer
from Lexer.Tokens import tokens

precedence = (
    ('left', 'AND', 'OR'),
    ('nonassoc', 'BETWEEN', 'IGUAL', 'MAYOR_QUE', 'MENOR_QUE', 'MAYOR_IGUAL', 'MENOR_IGUAL', 'DIFERENTE'),
)

start = 'statement'

def p_statement(p):
    '''statement : select_statement
                 | insert_statement
                 | update_statement
                 | delete_statement
                 | alter_table_statement'''
    p[0] = p[1]

def p_select_statement(p):
    '''select_statement : SELECT opt_distinct select_list FROM table_list opt_join_clause opt_where_clause opt_group_by_clause opt_having_clause opt_order_by_clause PUNTO_Y_COMA'''
    p[0] = ('SELECT', p[2], p[3], p[5], p[6], p[7], p[8], p[9], p[10])
 
def p_opt_order_by_clause(p):
    '''opt_order_by_clause : ORDER_BY column_list
                           | empty'''
    if len(p) == 3:
        p[0] = ('ORDER_BY', p[2])
    else:
        p[0] = None 
    
def p_opt_distinct(p):
    '''opt_distinct : DISTINCT
                    | empty'''
    p[0] = p[1] if len(p) == 2 else None

def p_select_list(p):
    '''select_list : ASTERISCO
                   | select_items'''
    p[0] = p[1]
    
def p_select_items(p):
    '''select_items : select_items COMA select_item
                    | select_item'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]
        
def p_select_item(p):
    '''select_item : DISTINCT identifier
                   | identifier
                   | function_call'''
    if len(p) == 3:
        p[0] = ('DISTINCT', p[2])
    else:
        p[0] = p[1]
        
def p_function_call(p):
    '''function_call : COUNT PARENIZQ operand PARENDER
                     | SUM PARENIZQ operand PARENDER
                     | AVG PARENIZQ operand PARENDER
                     | MIN PARENIZQ operand PARENDER
                     | MAX PARENIZQ operand PARENDER'''
    p[0] = (p[1].upper(), p[3])

def p_column_list(p):
    '''column_list : identifier
                   | identifier COMA column_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_table_list(p):
    '''table_list : identifier
                  | identifier COMA table_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
        
def p_opt_join_clause(p):
    '''opt_join_clause : JOIN identifier ON condition
                       | empty'''
    if len(p) == 5:
        p[0] = ('JOIN', p[2], p[4])
    else:
        p[0] = None

def p_opt_where_clause(p):
    '''opt_where_clause : WHERE condition
                        | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None
        
def p_opt_group_by_clause(p):
    '''opt_group_by_clause : GROUP_BY column_list
                           | empty'''
    p[0] = ('GROUP_BY', p[2]) if len(p) == 3 else None
    
def p_opt_having_clause(p):
    '''opt_having_clause : HAVING condition
                         | empty'''
    p[0] = ('HAVING', p[2]) if len(p) == 3 else None

def p_condition(p):
    '''condition : expression
                 | condition AND condition
                 | condition OR condition'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2].upper() == 'AND':
        p[0] = ('AND', p[1], p[3])
    elif p[2].upper() == 'OR':
        p[0] = ('OR', p[1], p[3])
        
def p_operand(p):
    '''operand : value
               | aggregate_function'''
    p[0] = p[1]
    
def p_value(p):
    '''value : NUM
             | STRING
             | identifier
             | ASTERISCO'''
    p[0] = p[1]

def p_expression(p):
    '''expression : operand comparador operand
                  | operand BETWEEN operand AND operand'''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = ('BETWEEN', p[1], p[3], p[5])

def p_aggregate_function(p):
    '''aggregate_function : COUNT PARENIZQ operand PARENDER
                          | SUM PARENIZQ operand PARENDER
                          | AVG PARENIZQ operand PARENDER
                          | MIN PARENIZQ operand PARENDER
                          | MAX PARENIZQ operand PARENDER'''
    p[0] = (p[1].upper(), p[3])

def p_comparador(p):
    '''comparador : IGUAL
                  | MAYOR_QUE
                  | MENOR_QUE
                  | MAYOR_IGUAL
                  | MENOR_IGUAL
                  | DIFERENTE'''
    p[0] = p[1]
    
def p_insert_statement(p):
    '''insert_statement : INSERT_INTO identifier PARENIZQ column_list PARENDER VALUES PARENIZQ value_list PARENDER PUNTO_Y_COMA'''
    p[0] = ('INSERT', p[2], p[4], p[8])
    
def p_value_list(p):
    '''value_list : value
                  | value COMA value_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
        
def p_update_statement(p):
    '''update_statement : UPDATE identifier SET assignment_list opt_where_clause PUNTO_Y_COMA'''
    p[0] = ('UPDATE', p[2], p[4], p[5])
    
def p_assignment_list(p):
    '''assignment_list : assignment
                       | assignment COMA assignment_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
        
def p_assignment(p):
    '''assignment : identifier IGUAL value'''
    p[0] = (p[1], p[3])
    
def p_delete_statement(p):
    '''delete_statement : DELETE_FROM identifier opt_where_clause PUNTO_Y_COMA'''
    p[0] = ('DELETE', p[2], p[3])
    
def p_alter_table_statement(p):
    '''alter_table_statement : ALTER_TABLE identifier ADD_COLUMN column_definition PUNTO_Y_COMA
                             | ALTER_TABLE identifier DROP_COLUMN identifier PUNTO_Y_COMA'''
    
    if p[3] == 'ADD COLUMN':
        p[0] = ('ALTER_TABLE_ADD', p[2], p[4])
    elif p[3] == 'DROP COLUMN':
        p[0] = ('ALTER_TABLE_DROP', p[2], p[4])
        
def p_create_table_statement(p):
    '''create_table_statement : CREATE_TABLE identifier PARENIZQ column_definition_list PARENDER PUNTO_Y_COMA'''
    p[0] = ('CREATE_TABLE', p[2], p[4])
    
def p_column_definition_list(p):
    '''column_definition_list : column_definition
                              | column_definition COMA column_definition_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_column_definition(p):
    '''column_definition : identifier data_type column_constraints'''
    p[0] = (p[1], p[2], p[3])
    
def p_data_type(p):
    '''data_type : VARCHAR PARENIZQ NUM PARENDER
                 | INT'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('VARCHAR', p[3])
        
def p_column_constraints(p):
    '''column_constraints : constraint
                          | column_constraints constraint'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
        
def p_constraint(p):
    '''constraint : NOT_NULL
                  | UNIQUE
                  | PRIMARY_KEY
                  | FOREIGN_KEY'''
    p[0] = p[1]
    
def p_identifier(p):
    '''identifier : ID
                  | ID PUNTO ID'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}.{p[3]}"

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' línea {p.lineno}")
        raise SyntaxError(f"Error de sintaxis en '{p.value}' línea {p.lineno}")
    else:
        print("Error de sintaxis al final de la entrada")
        raise SyntaxError("Error de sintaxis al final de la entrada")

parser = yacc.yacc()

def parse_sql(sql_query):
    lexer = get_lexer()
    result = parser.parse(sql_query, lexer=lexer)
    return result