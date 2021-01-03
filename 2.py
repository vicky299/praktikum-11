while True:
    x = input('Masukkan Kode Member	: ')
    y = input('Masukkan Nama Member	: ')
    z = input('Masukkan Judul Buku	: ')
    from datetime import datetime, timedelta

    dt = datetime.now()
    h = dt + timedelta(days=7)
    print('dipinjam pada tanggal:', dt)
    print('batas waktu::', h)
    print('Ulangi lagi(y/n)?   : ')
    jawab = input()
    if jawab == 'n':
        break
    
print(x,y,z,dt,h)
