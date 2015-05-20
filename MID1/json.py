import ply.lex as lex

tokens = (
	'OBJECT',
	'ARRAY',
	'STRING',
	'NUMBER',
	)

def t_error(t):
	t.lexer.skip(1)

t_ignore = ' \v' # whitespace 

def t_NUMBER(t):
	r'-?[0-9]+(?:\.[0-9]+(?:[eE][\-\+][0-9]+)?)?'
	t.type = 'NUMBER'
	return t

def t_STRING(t):
    r'"(?:[^\\]|(?:\\.))*"'
    t.type = 'STRING'
    t.value = t.value[1:-1]
    return t

