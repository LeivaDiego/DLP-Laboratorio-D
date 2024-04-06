from utils.parse_yalex import parse_yalex
from utils.regex_infix_to_postfix import regex_infix_to_postfix
from utils.direct_construction import build_expression_tree
from utils.show_tree import show_expression_tree
from utils.path_cleaner import replace_slash_with_backslash

# Path del archivo .yal a convertir.
raw_path = input("Enter the path of the .yal file: ")
path = replace_slash_with_backslash(raw_path)
yalex_regex, _ = parse_yalex(path)
postfix_yalex_regex = regex_infix_to_postfix(yalex_regex)
yalex_expression_root, _ = build_expression_tree(postfix_yalex_regex)
show_expression_tree(yalex_expression_root, name=path.split("/")[-1].split(".")[0])

print("The tree has been generated successfully.")