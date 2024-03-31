from regex_processing.validator import is_balanced, is_empty, validate_syntax

def main():
    expressions =[")a+|b+(c*",
                  "(a|b|c)*",
                  "(a|b)|(c|d)",
                  "{abc}",
                  "ab|b+]",
                  "a}",
                  "(a|bc(",
                  "a(c|d)?",
                  "a?b?c?",
                  "a+?",
                  "a???",
                  "(a?|b?)c",
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
                  "{ab|}*|c",
                ]
    for regex in expressions:
        try:
            print(f"Checking {regex}")
            is_balanced(regex)
            is_empty(regex)
            validate_syntax(regex)
            print(f"{regex} is Valid.")
        except Exception as e:
            print(f"Error: {e}")
        

if __name__ == "__main__":
    main()