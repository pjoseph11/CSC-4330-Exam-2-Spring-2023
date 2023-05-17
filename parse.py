class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self):
        self.stmt_list()
        return self.pos == len(self.tokens)
    
    #define functions for each non-terminal according to grammar
    def stmt_list(self):
        while self.pos < len(self.tokens):
            self.stmt()
            if self.tokens[self.pos] == ';':
                self.pos += 1
            else:
                raise ValueError('Invalid')
    
    def stmt(self):
        if self.tokens[self.pos] == 'if':
            self.if_stmt()
        elif self.tokens[self.pos] == '{':
            self.block()
        elif self.tokens[self.pos] == 'while':
            self.while_loop()
        else:
            self.expr()
    
    def while_loop(self):
        self.expect('while')
        self.expect('(')
        self.bool_expr()
        self.expect(')')
        if self.tokens[self.pos] == '{':
            self.block()
        else:
            self.stmt()
            self.expect(';')
    
    def if_stmt(self):
        self.expect('if')
        self.expect('(')
        self.bool_expr()
        self.expect(')')
        if self.tokens[self.pos] == '{':
            self.block()
        else:
            self.stmt()
            self.expect(';')
        if self.tokens[self.pos] == 'else':
            self.pos += 1
            if self.tokens[self.pos] == '{':
                self.block()
            else:
                self.stmt()
                self.expect(';')
    
    def block(self):
        self.expect('{')
        self.stmt_list()
        self.expect('}')
    
    def expr(self):
        self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-', '*', '/', '%'):
            self.pos += 1
            self.term()
    
    def term(self):
        self.fact()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('*', '/', '%'):
            self.pos += 1
            self.fact()
    
    def fact(self):
        if self.tokens[self.pos].isdigit():
            self.pos += 1
        elif self.tokens[self.pos].isalpha():
            self.pos += 1
        elif self.tokens[self.pos] == '(':
            self.pos += 1
            self.expr()
            self.expect(')')
        else:
            raise ValueError('Invalid')
    
    def bool_expr(self):
        self.bterm()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('>', '<', '>=', '<='):
            self.pos += 1
            self.bterm()
    
    def bterm(self):
        self.band()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('==', '!='):
            self.pos += 1
            self.band()
    
    def band(self):
        self.bor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] == '&&':
            self.pos += 1
            self.bor()
    
    def bor(self):
        self.expr()
        while self.pos < len(self.tokens) and self.tokens[self.pos] == '||':
            self.pos += 1
            self.expr()
    
    def expect(self, token):
        if self.tokens[self.pos] == token:
            self.pos += 1
        else:
            raise ValueError('Invalid')
