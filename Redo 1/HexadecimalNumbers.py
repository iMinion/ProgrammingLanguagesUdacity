import ply.lex as lex
import re

tokens = ('NUM', 'ID')

def t_ID(t):
	r'[a-zA-Z]+'
	t.type = 'ID'
	return t

def t_NUM(t):
	r'0x[a-fA-F0-9]+'
	num = t.value[2:]
	i = 0
	no = 0
	while i < len(num):
		no *= 16
		order = ord(num[i])
		if order >= 65 and order <= 70:
			num = num + order - 55
		elif order >= 48 and order <= 57:
			num = num + order - 48
		else:
			num = num + order - 87
		i += 1
	t.type = 'NUM'
	t.value = num
	return t

def t_NUM_decimal(token):
  r'[0-9]+'
  token.value = int(token.value)
  token.type = 'NUM'
  return token

t_ignore = ' \t\v\r'

def t_error(t):
	print "Check the input this lexer only processes "
	t.lexer.skip(1)