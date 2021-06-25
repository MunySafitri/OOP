#memiliki kelas turunan , menampilkan hal yang berbeda
class Manusia(object):
    nama = None
    def __init__(self, nama):
        self.nama = nama
    def makan(self):
        print("{} makan nasi".format(self.nama))
#anak class kita buat
class ManusiaMilenial(Manusia):
    email = None
    __password = None
    def set_email(self, email):
        self.email = email

    def set_pass (self, password):#karena private hanyclass ini yang punya nama variabel
        self.__password = password

    def info(self):#menggantikan methodnya untuk melakukan hal yang berbeda,method overwriting
        print("nama={}, email={}, pass = {}".format(self.nama,self.email,self.__samarkan_password()))

    def __samarkan_password(self):
         #self.__password.replace('i','*')
        return self.__password.replace('a','*')

#konsep polymorphism
class Programmer(ManusiaMilenial):#subclass ManusiaMilenial
    def info(self):
        #print("nama={}: email={}: pass = {}".format(self.nama,self.email,self.__samarkan_password()))#akan menyababkan error karena kita mengakses variabel private class utama
        print("nama={}: email={}".format(self.nama,self.email))

class Influencer(ManusiaMilenial):

    def info(self):
        print("nama={}/ email={}".format(self.nama,self.email))

#funfact
#method overloading
#memiliki nama fungsi yang sama hanya saja parameter berbeda

programmer = Programmer("Eka")#turunan dari manusia milenial
programmer.set_email("eka@gmail.com")
programmer.set_pass("Rahasia")
programmer.info()#karna di dalam fungsi def parameternya self

influencer = Influencer("PUTRA")#turunan dari manusia milenial
influencer.set_email("putra@gmail.com")
influencer.set_pass("Harisah")
influencer.info()
#print(programmer.__password) #sebagai contoh #akan terjadi eeror yang mengatakan tioddak punya variabel tersebut padahala punya
