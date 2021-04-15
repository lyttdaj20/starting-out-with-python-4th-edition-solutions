
# 7.7 Driver’s License Exam

def main():

    correct = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    incorrect = [] 

    file = open('answers.txt', 'r')
    
    score = 0
    passed = 'Yes'
    
    index = 0
    
    for line in file:

        if line.rstrip() == correct[index]:
            
            score += 1
        
        else:
            
            incorrect.append(index + 1)
        
        index += 1
    
    incorrect = str(incorrect)
    incorrect = incorrect[1:len(incorrect) - 1]
    
    if score < 15:
        
        passed = 'No'
        
    print('Passed:', passed)
    print('No. Correct:', score)
    print('No. Incorrect:', str(20 - score))
    print('Incorrect:', incorrect)
    
    
main()