
# 6.4 Item Counter

def main():
    
    file = open('names.txt', 'r')

    total = 0
    
    for line in file:
        
        total += 1
    
    print('Number of Names:', total)
    
    file.close()
    
main()