
# 5.13 Falling Distance

# The formula for freefall distance from rest is 0.5 * g * t^2

def main():
    
    distance = 0
    
    for i in range(1, 11):
        distance = falling_distance(i)
        print('The object will fall', distance, 'meters in', i, 'seconds')

def falling_distance(time):
    gravity = 9.8
    distance = round(0.5 * gravity * pow(time, 2), 1)
    return distance

main()