
# 12.5 Recursive List Sum

def main():
    
    sample_list = [1, 2, 18, 31]
    index = 0
    sum = 0
    sum = list_sum(sample_list, index, sum)
    print('Sum:', sum)
    
def list_sum(list, index, sum):
    
    if index < len(list):
    
        sum += list[index] 
            
        sum = list_sum(list, index + 1, sum)
    
    return sum

main()