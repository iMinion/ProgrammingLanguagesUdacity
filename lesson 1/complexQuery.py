# Tricky REs with ^ and \

# Assign to regexp a regular expression for double-quoted string literals that
# allows for escaped double quotes.

# Hint: Escape " and \
# Hint: (?: (?: ) )

import re
# Solution
regexp = r'"(?:[^"\\]|(?:\\.))*"'
# My Solution
# regexp = r"(?:\'|\\|(?:\"|[a-z]+|.+)+|.+)+"
print re.findall(regexp,'"\\"')

# regexp matches:

#print re.findall(regexp,'"I say, \\"hello.\\""') == ['"I say, \\"hello.\\""']
#>>> True


# regexp does not match:

#print re.findall(regexp,'"\\"') != ['"\\"']
#>>> True