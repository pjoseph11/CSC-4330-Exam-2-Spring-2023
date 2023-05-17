from lex import *
from FileReader import *
from parse import *


#readin file
reader = Read('input.txt')
reader.readFile()
code = reader.contents

#tokenize code and label lexically
lex_L = Lexer()
tokens_labeled = lex_L.tokenize(code)
print(tokens_labeled)

#only tokens for the parse
lex = Lexer()
tokens = lex.tokenizer(code)

#parse tokens for syntax
parse = Parser(tokens)
result = parse.parse()  
if result == True:
   print('Pass')
else:
   print('Fail')



