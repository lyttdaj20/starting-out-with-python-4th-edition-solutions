
# 8.12 Word Separator

def main():

    sentence = input('Enter Sentence: ')
    
    seperated = ''
    
    word = ''

    first = True

    for ch in sentence:
    
        if ch.isupper() == False:
            
            word += ch
    
        else:
            
            seperated += word
            
            if word == '':
            
                seperated += ch
                
            else:
                
                seperated += ' ' + ch.lower()
            
            word = ''

    seperated += word
    
    print(seperated)
    
main()