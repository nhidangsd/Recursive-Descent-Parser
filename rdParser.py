import re
from functools import *

"""

A LL recursive descent parser for validating simple expressions.

You would need to first write the grammar rules (non-terminal) in EBNF according to the token
patterns and grammar rules specified in Assignment 2 Task A. 
You can then follow the examples of the parsing procedure pseudocode implementation in Figure 5.17
in the textbook to write the recursive descent parsing procedures for the validation parsing.

The following recursive descent parsing algorithm is a LL parser. It implements one parsing 
procedure for each one of the above non-terminals (grammar rules), starting from the top of the 
parse tree, then drilling into lower hierachical levels.

The procedures work together to handle all combinations of the grammar rules, and they 
automatically handle the nested compositions of terms with multi-level priority brackets. 

---------------------------------------------------------------------
Usage

r = recDecsent('7 - 17')
print(r.validate()) # will print True as '7 - 17' is a valid expression

r = recDecsent('7 - ')
print(r.validate()) # will print False as '7 - ' is an invalid expression

"""




"""
PART A: EBNF Grammar Rule:

<relop>  ::=  < | > | <= | >= | = | != | not
<expr>   ::=  <term> { (and|or) <term> } 
<term>   ::= (<expr>) | <relop> <factor> | <factor> - <factor> 
<factor> ::=  int 

"""
class recDescent:
    
    # relational (unary) operators (prefix)
    relop = ['<', '>', '<=', '>=', '=', '!=', 'not']
    
    # binary operators (infix)
    dashop = ['-', '–']
    logicop = ['and', 'or']

    # tokens for manipulating priority
    priopen = '('
    priclose = ')'

    # constructor to initialize and set class level variables
    def __init__(self, expr = ""):

        # string to be parsed
        self.expr = expr

        # tokens from lexer tokenization of the expression
        self.tokens = []

    # lexer - tokenize the expression into a list of tokens
    # the tokens are stored in an list which can be accessed by self.tokens
    # do not edit any piece of code in this function
    def lex(self):
        self.tokens = re.findall("[-\(\)=]|[!<>]=|[<>]|\w+|[^ +]\W+", self.expr)
        # filter out the possible spaces in the elements
        self.tokens = list(filter((lambda x: len(x)), 
                           list(map((lambda x: x.strip().lower()), self.tokens))))    

    
    # validate() function will return True if the expression is valid, False otherwise 
    def validate(self):

        self.operators_dict = {
            'relop': self.relop,
            'dashop': self.dashop,
            'logicop': self.logicop,
            '(': self.priopen,
            ')': self.priclose,
        }

        # Keep track of matching parenthesis '()'
        #  - Increment this variable by 1 when encounter '('
        #  - and Decrement this variable by 1 when encounter ')'
        self.parenCounter = 0

        # Init self.tokens
        self.lex()

        # Convert self.tokens typed list into Iterator so we can use 
        # Python built-in function Next() to obtain the nextToken in the input string
        self.iter_tokens = iter(self.tokens)

        # Declare variables to keep track of the current token and next token
        self.curToken = self.nextToken = None
        # Init values for curToken and nextToken
        self._advance()     

        # Check if the input is a valid expression
        return self.expression()


    '''
        parsing procedures corresponding to the grammar rules 
    '''

    # expression() - determine if the input is a valid expression
    def expression(self):
        """
        - Returns True if the input matches the grammar rule below and otherwise
            <expr> ::= <term> { (and | or) <term> }
    
        """
        res = False

        if self.term():
            res = True

            while self._accept('logicop') and res:
                if not self.term():
                    res = False
                
            if self.nextToken != None:
                if self.nextToken != self.priclose or self.parenCounter <= 0:
                    res = False

        return res


    # term() - will return True if the term is valid, False otherwise
    def term(self):
        """
        - Returns True if the input matches the grammar rule below and otherwise
            <term> ::= (<expr>) | <relop> <factor> | <factor> - <factor> 
        """

        # case: ( <expr> )
        if self._accept('('):
            self.parenCounter += 1

            if self.expression():

                if self._accept(')'):
                    self.parenCounter -= 1
                    return True
  
        # case: <relop> <factor>
        elif self._accept('relop'):
            if self.factor():
                return True

        # case: <factor> - <factor>
        elif self.factor():
            if self._accept('dashop'): 
                if self.factor():
                    return True

        return False


    # factor() - will return True if the factor is valid, False otherwise
    def factor(self):
        """
        - Returns True if the input matches the grammar rule below and otherwise
                <factor>  ::= int

        - This function will look ahead to see if the next token is an integer.
        If so, advances to the new token and return True
        """

        try:
            s = int(self.nextToken)
            self._advance()
            return True
        except:
            return False



    '''
                Helper functions
    '''

    # _advance() - will load the new token
    def _advance(self):

        """
        - Sets the current token to the next token AND
        loads new token from the Iterator into next token.
        """
        self.curToken, self.nextToken = self.nextToken, next(self.iter_tokens, None)


    # _accept() - will check if the next Token is valid operator
    def _accept(self, key):
        """
        - Looks ahead to see if the next token is valid operator.
            If so, advances to the next token and return True
        
        @param key:    a valid key in self.operator.dict

        Note: We convert self.nexToken to a string in case of NoneType
            For example: None in ['a,'b'] will throw an error.
        """
        if str(self.nextToken) in self.operators_dict[key]:
            self._advance()
            return True

        return False
