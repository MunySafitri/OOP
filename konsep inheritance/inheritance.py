class Manusia(object):
    nama = None
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print("{} makan nasi".format(self.nama))
#anak class kita buat
class ManusiaMilenial(Manusia):#konsep inherintance
    email = None

    def set_email(self, email):
        self.email = email

    def info(self):
        print("nama={}, email={}".format(self.nama,self.email))


programmer =ManusiaMilenial("Eka")
programmer.set_email("eka@gmail.com")
programmer.info()

petani = ManusiaMilenial("putra")
petani.set_email("putra@gmail.com")
petani.info()

dokter =ManusiaMilenial("putri")
dokter.set_email("putri@gmail.com")
dokter.info()
