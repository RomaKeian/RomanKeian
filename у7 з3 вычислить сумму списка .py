cod='12,46,79,41'
cod1=cod.split(',')

for i in cod1:
    s=0
    for i1 in i:
        s+=int(i1)
    print(s)