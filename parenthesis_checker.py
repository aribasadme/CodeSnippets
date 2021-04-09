def ispar(s):
    '''
    Function Arguments :
            @param  : s (given string containing parenthesis)
            @return : boolean True or False
    '''
    stack = []

    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False

            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
    if stack:
        return False
    return True
