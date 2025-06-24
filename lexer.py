# Analizador lexico para Little English
# Definicion de tokens
I = 1
A = 2
THE = 3
ME = 4
CAT = 5
MAT = 6
RAT = 7
LIKE = 8
LIKES = 9
IS = 10
SEE = 11
SEES = 12
DOT = 13

class Token:
    def __init__(self, category, lexeme):
        self.category = category
        self.lexeme = lexeme

keywords = {
    'i': I,
    'a': A, 
    'the': THE,
    'me': ME,
    'cat': CAT,
    'mat': MAT,
    'rat': RAT,
    'like': LIKE,
    'likes': LIKES,
    'is': IS,
    'see': SEE,
    'sees': SEES
}

def tokenize(line):
    tokens = []
    line = line.strip()
    
    if not line:
        raise RuntimeError('Linea vacia')
    
    if not line.endswith('.'):
        raise RuntimeError('La oracion debe terminar en punto')
    
    words = line.split()
    
    for word in words:
        if word.endswith('.'):
            word_part = word[:-1]
            if word_part:
                word_lower = word_part.lower()
                if word_lower in keywords:
                    token = Token(keywords[word_lower], word_lower)
                    tokens.append(token)
                else:
                    raise RuntimeError('Token invalido: ' + word_part)
            
            dot_token = Token(DOT, '.')
            tokens.append(dot_token)
        else:
            word_lower = word.lower()
            if word_lower in keywords:
                token = Token(keywords[word_lower], word_lower)
                tokens.append(token)
            else:
                raise RuntimeError('Token invalido: ' + word)
    
    return tokens