def infix2postfix(regex):
    """
    Converts an infix regular expression to postfix notation.

    Args:
        regex (str): The infix regular expression to convert.

    Returns:
        str: The postfix regular expression.
    """
    precedence = {'*': 3, '+': 3, '?': 3, '·': 2, '|': 1, '(': 0}
    stack = []
    postfix = []
    for char in regex:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[char]:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)