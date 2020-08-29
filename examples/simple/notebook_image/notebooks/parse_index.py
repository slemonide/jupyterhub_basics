from myst_parser.main import to_html

with open("index.md","r") as infile:
    md_text = infile.read()

print(to_html(md_text))

from pprint import pprint
from myst_parser.main import to_tokens

for token in to_tokens(md_text):
    print(f"{token.type}: \n{token}\n\n")
    print()
