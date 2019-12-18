"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid."""

def isValid(self, s: str) -> bool:
    stack = []   #create a stack to push when reading '(', '[', '{' and pop when reading ')', ']', '}'
    for c in s:
    	if (len(stack) == 0) and (c == ')' or c == ']' or c == '}'):
    		return False
    	if c == '(' or c == '[' or c == '{':
    		stack.append(c)
    	elif c == ')' and stack[-1] == '(':
    		stack.pop() #pop the first item in the stack (or last item in the list)
    	elif c == ']' and stack[-1] == '[':
    		stack.pop()
    	elif c == '}' and stack[-1] == '{':
    		stack.pop()
    	#if the character is a closing bracket, and the top of the stack doesn't match the same type, return False
    	elif c == ')' and stack[-1] != '(':
    		return False
    	elif c == ']' and stack[-1] != '[':
    		return False
    	elif c == '}' and stack[-1] != '{':
    		return False
    if len(stack) == 0:
    	return True
    return False

