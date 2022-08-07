n_kv=int(input('номер квартиры '))
kv_na_etaje=4*9
pod=(n_kv-1)//kv_na_etaje+1
etaj=(n_kv-1)// 4+1

print('Подезд :',pod)
print('етаж :',etaj)
