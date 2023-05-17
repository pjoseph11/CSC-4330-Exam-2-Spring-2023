import re
class Lexer:
    def __init__(self):
        # regex patterns for tokens
        self.patterns = [
          ('IF', r'if'),
          ('ELSE', r'else'),
          ('WHILE', r'while'),
          ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
          ('INT_LIT', r'\d+'),
          ('FLOAT_LIT', r'\d+\.\d+'),
          ('PLUS', r'\+'),
          ('MINUS', r'-'),
          ('MUL', r'\*'),
          ('DIV', r'/'),
          ('MOD', r'%'),
          ('LPAREN', r'\('),
          ('RPAREN', r'\)'),
          ('ASSIGN', r'='),
          ('SEMICOLON', r';'),
          ('LBRACE', r'\{'),
          ('RBRACE', r'\}'),
          ('BOOL_OP', r'(&&|\|\|)'),
          ('REL_OP', r'(<=|>=|!=|==|<|>)'),
        ]
        self.pattern = '|'.join('(?P<%s>%s)' % pair for pair in self.patterns)
    #takes in a string an returns tokens with labels   
    def tokenize(self, code):
        tokens = []
        for match in re.finditer(self.pattern, code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'INTEGER':
                value = int(value)
            elif kind == 'FLOAT':
                value = float(value)
            tokens.append([kind,value])
        return tokens
    #takes in string and returns only tokens   
    def tokenizer(self, code):
        tokens = []
        for match in re.finditer(self.pattern, code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'INTEGER':
                value = int(value)
            elif kind == 'FLOAT':
                value = float(value)
            tokens.append(value)
        return tokens

