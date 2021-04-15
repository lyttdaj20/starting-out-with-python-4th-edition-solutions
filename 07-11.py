
# 7.11 Lo Shu Magic Square

def main():

    square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    magic = True

    main_list = []
    
    for i in range(3):
        
        for j in range(3):
            
            main_list.append(square[i][j])

    for i in range(1, 10):
        
        count = 0
        
        for j in main_list:
            
            if i == j:
            
                count += 1
        
        if count != 1:
        
            magic = False
    
    if magic:
        
        total = sum(square[0])
        
        for i in range(1,3):

            if sum(square[i]) != total:
            
                magic = False
         
        for j in range(3):
            
            column = []
            
            for i in range(3):
                
                column.append(square[i][j])
        
            if sum(column) != total:
            
                magic = False            
        
        diagonal1 = []
        
        for i in range(3):
            
            diagonal1.append(square[i][i])
        
        if sum(diagonal1) != total:
            
            magic = False
        
        diagonal2 = []

        for i in range(3):
            
            diagonal2.append(square[i][2 - i])
        
        if sum(diagonal2) != total:
            
            magic = False 

        if magic:
            
            print('This square is a Lo Shu Magic Square')
            
        else:
        
            print('This square is not a Lo Shu Magic Square')


def sum(list):
    
    sum = 0
    
    for i in list:
        
        sum += i
    
    return sum

main()