from regex_processing.validator import is_balanced

def main():
    expressions =[")a+|b+(c*",
                  "(a|b|c)*",
                  "(a|b)|(c|d)",
                  "{abc}",
                  "ab|b+]",
                  "a]}",
                  "(a|bc(",
                  "a(c|d)?",
                  "a?b?c?",
                  "a+?",
                  "a???",
                  "(a?|b?)c",
                  "(1|2|3)a*b+?",
                  "(a+|b)+b?",
                  "(aa*)|c*|a+",
                  ""
                  ]
    for regex in expressions:
        try:
            is_balanced(regex)
            print(f"{regex} is balanced.")
        except Exception as e:
            print(f"{regex} Error: {e}")

if __name__ == "__main__":
    main()