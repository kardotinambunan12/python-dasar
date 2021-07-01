# perulangan menggunakan list

# nilai = [1,2,3,4,5,6,7,8,9,10]


# for newnilai in nilai :

#     print (newnilai)

# listkota = [
#     'medan', 'berastagi','dairi','Humbang Hasundutan','kec.Parlilitan'
#     ]

# for kota in listkota :
#     print(kota)

# x =10
# for i in range(x):

#     if (i == 5 ):
#         continue
#     print( i)


# listkota = [
#     'medan', 'berastagi', 'dairi', 'Humbang Hasundutan', 'kec.Parlilitan'
# ]
# # nama = 'masukkannamakota'

# namakota = input('masukkan nama kota : ')
# for i, kota in enumerate(listkota):
#     if kota == namakota:
#         print('kota yang kamu car berada :', i)
#         break
# else:
#     print('kota yang kamu cari tidak tersedia')

listnama =['aqil', 'hafsah', 'benry', 'timbul']
listmarga = ['parna', 'purba', 'manalu', 'sihotang']

for nama in listnama:
    print(nama)
    for marga in listmarga:
        print(marga)
