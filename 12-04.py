
# 12.4 Largest List Item

def main():
    
    sample_list = [1, 17, 3, 88, 15, 60]
    index = 0
    max = 0
    max = largest_list_item(sample_list, index, max)
    print('Largest Value:', max)
    
def largest_list_item(list, index, max):
    
    if index < len(list):
    
        if list[index] > max:
            
            max = list[index]
            
        max = largest_list_item(list, index + 1, max)
    
    return max

main()