
# 2.13 Planting Grapevines

row_length = float(input('Enter amount of space between the vines in feet: '))
endpost_space = float(input('Enter amount of space used by an end-post assembly in feet: '))
vine_space = float(input('Enter amount of space between vines in feet: '))

grapevines = round(row_length - (2 * endpost_space * vine_space), 0)

print('Number of grapevines', grapevines)

