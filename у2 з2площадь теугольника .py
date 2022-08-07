h=int(input('chislo : '))
j=1
while j<=h:
    i=1
    while i<=h:
        if (j+i<=h):
            print('  ', end=" ")
        else:
            print(' * ', end=" ")
        i = i + 1
    j = j + 1
    print()

