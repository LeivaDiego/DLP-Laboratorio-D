from utils.custom_exceptions import UnbalancedBrackets

brackets = {'(': ')', '[': ']', '{': '}'}  # Mapping of opening and closing brackets
opening_brackets = set(brackets.keys())
closing_brackets = set(brackets.values())

unary_operators = {'*', '+', '?'}  # Unary operators in regex
binary_operators = {'·', '|'}    # Binary operators in regex
all_operators = unary_operators | binary_operators # All operators in regex

def is_balanced(regex):
    """
    Check if the parenthesis are balanced in the regex.

    Args:
        regex (str): The regular expression to check.

    Raises:
        UnbalancedBrackets: If the brackets in the regex are unbalanced.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
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


def is_empty(regex):
    """
    Check if the regex is empty.

    Args:
        regex (str): The regular expression to check.

    Returns:
        bool: True if the regex is valid, False otherwise.
    """
    if regex == "" or regex.isspace() or not regex:
        raise ValueError("Empty regex")
    else:
        return True
    

def validate_syntax(expr):
    """
    Validates the syntax of a regular expression.

    Args:
        expr (str): The regular expression to validate.

    Raises:
        SyntaxError: If the regular expression has invalid syntax.

    Returns:
        bool: True if the syntax is valid, False otherwise.
    """

    def check_subexpr(subexpr):
        """
        Checks the syntax of a subexpression within a regular expression.
        """
        operand_count = 0
        i = 0
        while i < len(subexpr):
            char = subexpr[i]
            if char.isalnum() or char in opening_brackets:
                if char in opening_brackets:
                    # Find the corresponding closing bracket
                    closing_index = i + 1
                    balance = 1
                    while closing_index < len(subexpr) and balance > 0:
                        if subexpr[closing_index] in opening_brackets:
                            balance += 1
                        elif subexpr[closing_index] in closing_brackets:
                            balance -= 1
                        closing_index += 1
                    if balance != 0:
                        raise SyntaxError("Unbalanced brackets in subexpression")
                    
                    # Check the inner subexpression
                    check_subexpr(subexpr[i+1:closing_index-1])
                    i = closing_index - 1  # Jump to the end of the subexpression
                operand_count += 1
            
            # Unary operators
            elif char in unary_operators:
                if operand_count == 0:
                    raise SyntaxError("Unary operator without operand")
            
            # Binary operators
            elif char in binary_operators:
                if operand_count < 1:
                    raise SyntaxError("Binary operator without valid left operand")
                
                # Expect a valid operand after the binary operator
                if i == len(subexpr) - 1 or (subexpr[i+1] not in '+?*(' and not subexpr[i+1].isalnum()):
                    raise SyntaxError("Binary operator without valid right operand")
                operand_count = 1   # Reset for the next operand
            i += 1

        # At the end of a subexpression, there should be one operand
        if operand_count < 1:
            raise SyntaxError("Subexpression without proper syntax")
        return operand_count

    # Verify the whole regex
    check_subexpr(expr)
    return True