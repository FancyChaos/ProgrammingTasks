# Draw a chistmas tree!

# oneline of death (python3)!
h = int(input("Height: "))
print('\n'.join([' '*(h-i)+'x '*i for i in range(0,h)]),' '*(h-1)+'x',sep='\n')

# Muster Lösung
h = int(input("Height: "))
for i in range(0, h):
    print(' ' * (h-i) + 'x ' * i)
print(' ' * (h-1) + 'x')
