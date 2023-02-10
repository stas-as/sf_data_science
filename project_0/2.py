line = "(()())"
from collections import *
def brackets(line):
    stec = deque()
    for i in line:
        if i == "(":
            stec.append(i)
        elif i == ")":
            stec.pop()
    if len(stec) == 0:
        return True
    else:
        return False
    
    
print(brackets(line))