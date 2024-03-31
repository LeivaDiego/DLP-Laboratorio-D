from regex_processing.validator import unary_operators, all_operators

def extend_operand(operand, operator):
    """
    Tranforms a unary operator and an operand into an extended expression.

    Args:
        operand (str): The operand to extend.
        operator (str): The unary operator to apply.

    Returns:
        str: The extended operand.
    """
    if operator == '*':
        return f"{operand}*"
    elif operator == '+':
        return f"({operand}{operand}*)"
    elif operator == '?':
        return f"({operand}|ϵ)"
    

def extend_unary_operands(subexpr):
    """
    Transforms all unary operands within a subexpression to
    its extended form.

    Args:
        subexpr (str): The subexpression to transform.

    Returns:
        str: The transformed subexpression.
    """
    new_expr = ""
    i = 0
    while i < len(subexpr):
        char = subexpr[i]
        if char in unary_operators and i > 0 and subexpr[i - 1] not in all_operators and subexpr[i - 1] != '(':
            if new_expr[-1] == ')':
                balance = 1
                j = len(new_expr) - 2
                while j >= 0 and balance != 0:
                    if new_expr[j] == ')':
                        balance += 1
                    elif new_expr[j] == '(':
                        balance -= 1
                    j -= 1
                operand = new_expr[j + 1:]
                new_expr = new_expr[:j + 1]
            else:
                operand = new_expr[-1]
                new_expr = new_expr[:-1]

            while i < len(subexpr) and subexpr[i] in unary_operators:
                operand = extend_operand(operand, subexpr[i])
                i += 1
            new_expr += operand
            i -= 1
        else:
            new_expr += char
        i += 1
    return new_expr