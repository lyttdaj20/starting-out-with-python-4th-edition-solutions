
# 8.13 Pig Latin

def main():
    
    sentence = input('Enter Sentence: ')
    
    translation = ''
    
    word = ''

    for ch in sentence:
    
        if ch != ' ':
            
            word += ch
    
        else:
            
            translation += pig_latin(word)
            
            word = ''

    translation += pig_latin(word)
    
    print('Translation:', translation)
    
    
def pig_latin(word):
    
    if len(word) == 1:
        
        return word + 'ay '
    
    else:
        
        return word[1:len(word)] + word[0] + 'ay '



main()