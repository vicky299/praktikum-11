

print ('Tolong masukkan data pada saat meminjam buku :')

print ('================================================')

print ('')

bulan={1:'Januari',2:'Februari',3:'Maret',4:'April',5:'Mei',6:'Juni',7:'Juli',8:'Agustus',9:'September',10:'Oktober',11:'November',12:'Desember'}

TP=int(input('Tanggal Pinjam: '))

BP=int(input('Bulan Pinjam: '))

THP=int(input('Tahun Pinjam: '))

print ('')

print ('Tolong masukkan data pada saat mengembalikan buku :')

print ('================================================')

TM=int(input('Tanggal mengembalikan: '))

BM=int(input('Bulan mengembalikan: '))

THM=int(input('Tahun mengembalikan: '))

tgl=TM-TP

bln=BM-BP

thn=THM-THP

p=bln*30

q=thn*365

r=q+p+tgl

s=r*2000

print ('Lama peminjaman ',r,' Hari dengan biaya Rp ',s,'kembali pada tanggal',TM,',bulan',bulan[BM],'tahun',THM)

print ('')


