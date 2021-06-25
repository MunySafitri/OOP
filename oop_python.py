programmer = "Eka"
def programmer_makan():
    print("{} makan nasi".format(programmer))
petani = "Putra"
def petani_makan():
    print("{} makan nasi".format(petani))
dokter = "Putri"
def dokter_makan():
    print("{} makan nasi".format(dokter))

programmer_makan()
petani_makan()
dokter_makan()
#problemnya adalah bagaimana kita tidak membuat banyak nama variabel untuk
#meprint ke layar pada objek yang berbeda-beda.. disini lah kita menggunakan oop
