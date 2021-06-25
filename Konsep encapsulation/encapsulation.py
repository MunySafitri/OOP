#membungkus semua hal yang ada didalamnya  tpi hanya mengizinkan akses hal2 tertentu saja, seperti pass 
class Manusia(object):
    nama = None
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print("{} makan nasi".format(self.nama))
#anak class kita buat
class ManusiaMilenial(Manusia):#membuat password yang privat
    email = None
    __password = None #dengan menambahkan __ maka tidak dapat print pass
    #kita memprivate kan atribut dengan menggunakan __ hanya bisa dipanggil dalam class itu sendiri

    def set_email(self, email):
        self.email = email

    def set_pass (self, password):
        self.__password = password

    def info(self):
        print("nama={}, email={}, pass = {}".format(self.nama,self.email,self.__samarkan_password()))
    #konsep encapsulation, membuat fungsi private yang ga bisa diakses dari luar
    def __samarkan_password(self):
        return self.__password.replace('a','*')



programmer =ManusiaMilenial("Eka")
programmer.set_email("eka@gmail.com")
programmer.set_pass("Rahasia")
programmer.info()#karna di dalam fungsi def parameternya self

print(programmer.email)
#print(programmer.__password) #sebagai contoh #akan terjadi eeror yang mengatakan tioddak punya variabel tersebut padahala punya
