class Manusia(object):
    nama = None
    #fungsi konstruktor
    #init diperlukan ketika kita membuat sebuah objek
    def __init__(self, nama):#membuat sebuah fungsi yang meneriman nama
        self.nama = nama
    def makan(self):
        print("{} makan nasi".format(self.nama))

programmer = Manusia("Eka")#kita bentuk objeknya, kita lahirkan istilahnya
programmer.makan()
petani = Manusia("putra")
petani.makan()
dokter =Manusia("putri")
dokter.makan()
