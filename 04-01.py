
# 4.1 Bug Collector

total_bugs = 0

for day in range(1, 6):
    
    bugs = int(input('Bugs Collected on Day ' + str(day) + ': '))

    total_bugs += bugs
    
print('Total Bugs Collected:', total_bugs)