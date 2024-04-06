import sys
import os
from utils.parse_yalex import parse_yalex
from utils.regex_infix_to_postfix import regex_infix_to_postfix
from utils.direct_construction import build_expression_tree
from utils.show_tree import show_expression_tree

# Path del archivo .yal a convertir.
path = sys.argv[1] if (len(sys.argv) > 1) else "./yalex/slr-1.yal"
scanner_name = sys.argv[2] if (len(sys.argv) > 2) else "scanner.py"
yalex_regex, _ = parse_yalex(path)
postfix_yalex_regex = regex_infix_to_postfix(yalex_regex)
yalex_expression_root, _ = build_expression_tree(postfix_yalex_regex)
show_expression_tree(yalex_expression_root)