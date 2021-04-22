from rdParser import recDescent

valid_inputs = [
    '7-17',
    '> 90',
    '1-100 and not 50',
    '> 50 or = 20',
    '((1-100) or > 150) and < 300',
    '(5-100) and (not 50) and (>= 30 or (6-12))',
    '((1-100) or ( > 100 and < 150 )) and ( != 110)',
]

in_valid_inputs = [
    '',
    '7 -',
    '>',
    '(7 - 18',
    '7 - 17 or >',
    '( 7 - 17) and',
]

  
def main():
    print('This program will check if the input string is valid based on this EBNF grammar rule:')
    print('\t<relop>  ::= < | > | <= | >= | = | != | not')
    print('\t<expr>   ::= <term> { (and|or) <term> }')
    print('\t<term>   ::= (<expr>) | <relop> <factor> | <factor> - <factor> ')
    print('\t<factor> ::= int', end='\n\n') 

    # This will take input from keyboard and check if it is a valid expression
    while True:
        x = input('=> Please type in a string: ')
        r = recDescent(x)
        print('\n\t| Answer : ',r.validate(), end=' |\n\n') # will print True if input string is a valid expression    

        y = input("Do you want to check another string? [Y/N] : ").upper()
        if y == 'N' or y == '0' or y == 'Q':
            print('Exit program')
            break



# Uncomment this block to test out example predefined inputs
'''
    for i in valid_inputs:
        r = recDescent(i)
        print('Checking "', i, '"')
        print('\n\t| Answer : ',r.validate(), end=' |\n\n') # will print True   

    for i in in_valid_inputs:
        r = recDescent(i)
        print('Checking "', i, '"')
        print('\n\t| Answer : ',r.validate(), end=' |\n\n') # will print False
'''

if __name__ == "__main__":
    main()