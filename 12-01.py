
# 12.1 Recursive Printing

def main():
    
    n = int(input('Enter Number: '))
    
    recursive_printer(n)
  
def recursive_printer(n):
    
    if n > 0:
        
        print(n)
        
        recursive_printer(n - 1)
    
main()