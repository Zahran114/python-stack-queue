stack = []

def tambah_barang(stack, barang_baru):
    stack.append(barang_baru)
    print(f"{barang_baru} berhasil ditambahkan ke dalam stack.")
    
def hapus_barang_terakhir(stack):
    if len (stack) == 0 :
        print("stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        barang_terakhir = stack.pop()
        print(f"{barang_terakhir} berhasil dihapus dari stack")

def tampilan_barang_teratas(stack):
    if len(stack) == 0 :
        print("stack kosong, tidak ada barang yang dapat ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print("barang keatas di dalam stack adalah {barang_teratas}.")
        
while True:
    print("\n Gudang saat ini:",stack)
    print("Menu:")
    print("1.Tambah Barang")
    print("2.Hapus Barang Terakhir")
    print("3.Tampilan Barang Teratas")
    print("4.Keluar")
    
    pilihan = input("Masukan Pilihan Anda (1/2/3/4):")