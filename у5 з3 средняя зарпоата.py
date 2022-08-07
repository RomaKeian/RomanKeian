import random
a=[]
summ=0
for q in range(12):
    a.append(random.randint(7500,15000))
print('З/п оп месяцам в $:',a)
for elem in a:
    summ = summ + elem
print('Cредняя з/п за год : ', int(summ/len(a)),'$')

