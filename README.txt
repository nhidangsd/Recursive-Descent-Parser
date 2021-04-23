
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Parsing Procedures Documentation


INTRODUCTION
------------

This is a simple recursive descent parser program that can validate and evaluate expressions based on this specified EBNF grammar rule: 

    <relop>  ::=  < | > | <= | >= | = | != | not
    <expr>   ::=  <term> { (and|or) <term> } 
    <term>   ::= (<expr>) | <relop> <factor> | <factor> - <factor> 
    <factor> ::=  int 


REQUIREMENTS
------------

This module requires the following:

 * Python 3.6 or above
    

Parsing Procedures Documentation
--------------------------------

Program flow:
- Create an instance of class recDecsent and pass in the given string as an argument
- Call the method: validate() to check if the given string is valid 


* validate(): will return True if the expression is valid, False otherwise

    - Defines an dictionary called operator_dict for 
    relational operators, dash operator, logical operator, and parenthesis operator.
    - Declares & inits a variable called parenCounter to keep track of matching parenthesis.
    - Initializes the token list from the input string and make an Iterator from it.
    - Declares & inits variables to keep track of the current token and next token
    - Calls expression() to checj if the input is a valid expression

* expression(): will return True if the expression is valid, False otherwise

    - Only returns True if input string matches the pattern:  
        <term> { (and|or) <term> } 

    - Else returns False


* term(): will return True if the term is valid, False otherwise

    - Only returns True it falls into any of 3 cases:
        1. (<expr>)
        2. <relop> <factor>
        3. <factor> - <factor> 
    - Else returns False


* factor(): will return True if the factor is valid, False otherwise

    - Only returns True if the token is an integer
    - Else returns False


* _advance(): will load the new token

    - Sets the current token to the next token AND
    loads new token from the Iterator into next token.


* _accept(key):  will check if the next Token is valid operator

    - Looks ahead to see if the next token is valid operator.
    If so, advances to the next token and return True
        
    @param key:    a valid key in self.operator.dict that we defined in validate()