import sys

# Selecting Substrings : Writing a Python Procedure

# Let p and q each be strings containing two words separated by a space.

# Examples:
#    "bell hooks"
#    "grace hopper"
#    "alonzo church"

# Write a procedure called myfirst_yoursecond(p,q) that returns True if the
# first word in p equals the second word in q. Return False otherwise.
def myfirst_yoursecond(p,q):
    a = p.find(" ");
    r = p[0 : a];
    b = q.find(r);
    if(b != -1):
        return True;
    else:
        return False;

# A possible way of writing the code
# def myfirst_yoursecond(p,q):
#    pindex = p.find(" ");
#    qindex = q.find(" ");
#	 return p[:pindex] == q[qindex + 1:];

#print myfirst_yoursecond("bell hooks", "curer bell")
#>>> True
print myfirst_yoursecond("bell hooks", "curer bell")
