# Data Indexing List
x = ['Katib Pasha', 20, 'Desktop Programming', 3.99, True]

x = ('Desktop Programming', 20, 'Katib Pasha', 3.99)
#print(len(x[0]))

y = (1,4,5,2,9,10)
#print(max(y))
#print(min(y))


# Data Indexing Set
z = {2,9,1,4,5,3,5}
#print(type(z))
#print(z)
#z.discard(3)
#z.remove(3)
#z.add(10)
z.update('AMCC')
#print(z)

a = {'name':' katib Pasha','division':'Desktop programming','age': 20, 'IP': 3.99}
a.pop("IP")
a.pop("age")
a.clear()
#9print(a)

#panjang = input('Masukkan nilai panjang: ')
#lebar = input('masukkan nilai lebar: ')
#luas = int(panjang) * int(lebar)
#print("Luas =", luas)

def halo_dunia():
    print('Halo Python! halo dunia!')
    
halo_dunia()

def perkenalan(nama, asal):
    print(f"Perkenalkan saya {nama} dari {asal}")
    
perkenalan('katib Pasha','malaysia')
