lines = 0
words = 0
letters = 0
list_ = [',', '.', '(', ')']

with open(fname, 'r'):
    
    lines = f.read()
    lines = text.count('\n')
    for item in text:
        if item in list_:
            
