
# 12.3 Recursive Lines

def main():
    
    n = int(input('Enter Number of Lines: '))
    
    i = 1
    
    recursive_line_printer(i, n)
  
def recursive_line_printer(i, n):
    
    if i <= n:
        
        line = ''
        
        for j in range(0, i):        
        
            line += '*'
        
        print(line)
        
        recursive_line_printer(i + 1, n)
    
main()