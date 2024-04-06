from regex_processing.validator import is_balanced, is_empty, validate_syntax
from regex_processing.transformer import extend_unary_operands, explicit_concat
from regex_processing.postfix_converter import infix2postfix

def main():
    expressions =[")a+|b+(c*",
                  "(a|b|c)*d",
                  "(a|b)|(c|d)",
                  "(abc)",
                  "ab|b+]",
                  "a}",
                  "(a|bc(",
                  "a(c|d)?",
                  "a?b?c?",
                  "a+?",
                  "a???",
                  "(a?|b?)*c",
                  "(1|2|3)a*b+?",
                  "(a+|b)+b?",
                  "(aa*)|c*|a+",
                  "(a|b)*c|",
                  "((a|)*|c)c+|(a?|b?)",
                  " ",
                  "",
                  "a+",
                  None,
                  "a|b",
                  "(ab|)*|c",
                  "((a|b)c)+"
                ]
    for regex in expressions:
        try:
            print(f"Checking {regex}")
            is_balanced(regex)
            is_empty(regex)
            validate_syntax(regex)
            print(f"{regex} is Valid.")
            new_regex = extend_unary_operands(regex)
            print(f"Extended: {new_regex}")
            new_regex = explicit_concat(new_regex)
            print(f"Explicit Concatenation: {new_regex}")
            postfix = infix2postfix(new_regex)
            print(f"Postfix: {postfix}\n")
        except Exception as e:
            print(f"Error: {e}\n")
        

if __name__ == "__main__":
    main()