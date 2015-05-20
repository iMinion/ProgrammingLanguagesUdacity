# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

# Example:

l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f = len

def findmax(f, l):
    best_element_sofar = None
    best_f_value_sofar = None
    for i in l:
        f_value = f(i)
        if best_f_value_sofar == None || f_value > best_f_value_sofar:
            best_f_value_sofar = f_value
            best_element_sofar = i
    return best_element_sofar

print findmax(lambda(word): word.find("l"), l)