def is_balanced(s):
    # This function finds if a string is balanced or not
    stack = []
    closing_bracs = {'(': ')', '{': '}', '[': ']'}
    
    for b in s:
        if b in closing_bracs:
            stack.append(b)
        else:
            if not stack:
                return False
            popped_brac = stack.pop()
            if closing_bracs[popped_brac] != b:
                return False
    return not stack

