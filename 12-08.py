
# 12.8 Ackermann’s Function

def main():
    
    print(ackermann(3, 3))
    
def ackermann(m, n):

    if m == 0:
        
        return n + 1
    
    elif n == 0:
    
        return ackermann(m - 1, 1)
    
    else:
        
        return ackermann(m - 1, ackermann(m, n-  1))
    
main()