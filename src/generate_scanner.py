import sys
from utils.parse_yalex import parse_yalex
from utils.regex_infix_to_postfix import regex_infix_to_postfix
from utils.direct_construction import direct_construction
from utils.write_scanner import write_scanner
from utils.path_cleaner import replace_slash_with_backslash

raw_path = input("Enter the path of the .yal file: ")
path = replace_slash_with_backslash(raw_path)
scanner_name = (f"{path.split('/')[-1].split('.')[0]}_scanner.py")
yalex_regex, yalex_parser_code = parse_yalex(path)
postfix_yalex_regex = regex_infix_to_postfix(yalex_regex)
dfa = direct_construction(postfix_yalex_regex, yalex_parser_code)
write_scanner(scanner_name, postfix_yalex_regex, yalex_parser_code)