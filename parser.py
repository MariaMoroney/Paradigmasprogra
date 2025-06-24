from lexer import *

tokenlist = []
tokenindex = -1
token = None

def advance():
    global tokenindex, token
    tokenindex += 1
    if tokenindex < len(tokenlist):
        token = tokenlist[tokenindex]

def consume(expected_category):
    if token and token.category == expected_category:
        advance()
    else:
        raise RuntimeError('Se esperaba token diferente')

def sentence():
    subject()
    predicate()
    consume(DOT)

def subject():
    if token.category == I:
        consume(I)
    elif token.category == A:
        consume(A)
        noun()
    elif token.category == THE:
        consume(THE)
        noun()
    else:
        raise RuntimeError('Se esperaba sujeto valido')

def predicate():
    if token.category == LIKE:
        consume(LIKE)
        object_phrase()
    elif token.category == LIKES:
        consume(LIKES)
        object_phrase()
    elif token.category == IS:
        consume(IS)
        object_phrase()
    elif token.category == SEE:
        consume(SEE)
        object_phrase()
    elif token.category == SEES:
        consume(SEES)
        object_phrase()
    else:
        raise RuntimeError('Se esperaba verbo valido')

def object_phrase():
    if token.category == ME:
        consume(ME)
    elif token.category == A:
        consume(A)
        noun()
    elif token.category == THE:
        consume(THE)
        noun()
    else:
        raise RuntimeError('Se esperaba objeto valido')

def noun():
    if token.category == CAT:
        consume(CAT)
    elif token.category == MAT:
        consume(MAT)
    elif token.category == RAT:
        consume(RAT)
    else:
        raise RuntimeError('Se esperaba sustantivo valido')

def parse(tokens):
    global tokenlist, tokenindex, token
    tokenlist = tokens
    tokenindex = -1
    
    if not tokens:
        raise RuntimeError('No hay tokens')
    
    advance()
    sentence()
    
    if tokenindex < len(tokenlist):
        raise RuntimeError('Tokens extra al final')