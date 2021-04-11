
# 12.1 Recursive Printing

def main():
    
    n = int(input('Enter Number: '))
    
    i = 0
    
    recursive_printer(i, n)
  
def recursive_printer(i, n):
    
    if i <= n:
        
        print(i)
        
        recursive_printer(i + 1, n)
    
main()