
# 7.6 Larger Than n

def main():
    
    list = [9, 5, 15, 1, 7, 36, 12, 15, 10]
    
    n = 10
    
    larger(list, n)

def larger(list, n):
    
    for i in list:
        
        if i > n:
            
            print(i)

main()  

