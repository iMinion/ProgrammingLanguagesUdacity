import re
regexp = r'\*\/'
print re.findall(regexp, '''/* hello ramu */
	''')