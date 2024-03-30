from custom_exceptions import UnbalancedBrackets

def is_balanced(regex):
    """
    Check if the brackets are balanced in the regex.

    Args:
        regex (str): The regular expression to check.

    Raises:
        UnbalancedBrackets: If the brackets in the regex are unbalanced.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    brackets = {'(': ')', '[': ']', '{': '}'}  # Mapping of opening and closing brackets
    opening_brackets = set(brackets.keys())
    closing_brackets = set(brackets.values())

    stack = []  # Stack to store the opening brackets
    
    for i, char in enumerate(regex):
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets[stack.pop()] != char:
                raise UnbalancedBrackets(f"Unbalanced bracket at position {i}: {char}")
                
    if stack:
        raise UnbalancedBrackets(f"Unbalanced bracket at position {len(regex) - 1}: {stack[-1]}")

    return True