import os
#from user_ import user_menu


class Bookinglist:
    def __init__(self , bookinglist_name, bookinglist_nim, bookinglist_hp, bookinglist_umur):
        self.bookinglist_name = bookinglist_name
        self.bookinglist_nim = bookinglist_nim
        self.bookinglist_hp = bookinglist_hp
        self.bookinglist_umur = bookinglist_umur

class JadwalKonsuler:
    def __init__(self,jadwalKonsuler_hari,jadwalKonsuler_nama,jadwalKonsuler_status,jadwalKonsuler_waktu):
        self.jadwalKonsuler_hari = jadwalKonsuler_hari
        self.jadwalKonsuler_nama = jadwalKonsuler_nama
        self.jadwalKonsuler_status = jadwalKonsuler_status
        self.jadwalKonsuler_waktu = jadwalKonsuler_waktu

jadwal = [
    JadwalKonsuler('senin','Sena',True,'08:00 - 12:00'),
    JadwalKonsuler('senin','Adiarja',True,'12:00 - 16:00'),
    JadwalKonsuler('selasa','Selia',True,'08:00 - 12:00'),
    JadwalKonsuler('selasa','Elizabeth',True,'12:00 - 16:00'),
    JadwalKonsuler('rabu','Rabita',True,'08:00 - 12:00'),
    JadwalKonsuler('rabu','Leon',True,'12:00 - 16:00'),
    JadwalKonsuler('kamis','Kamila',True,'08:00 - 12:00'),
    JadwalKonsuler('kamis','Tiffa',True,'12:00 - 16:00'),
    JadwalKonsuler('jumat','Jumarni',True,'08:00 - 12:00'),
    JadwalKonsuler('jumat','Kafka',True,'12:00 - 16:00')
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

login_data = {
    'admin': 'admin123'
}

'''
def register():
    print ("Silahkan melakukan registrasi")
    username = input("Masukan username : ")
    password = input("Masukan password : ")
    confirm_password = input("Konfirmasi Password : ")

    file = open("login.txt","a")
    file.write (username)
    file.write (",")
    file.write (password)
    file.write ("\n")
    file.close

    if password != confirm_password:
        print("Passwords tidak sesuai.")
        return

    if username in login_data:
        print("Username sudah ada.")
        return

    user[username] = password
    print("Registrasi selesai!")
'''
def user_menu():
    ascii_art = """
    __        __   _                            _ 
    \ \      / /__| | ___ ___  _ __ ___   ___  | |
     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
      \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|     
       \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_) 

                                
    """

    print(ascii_art)
    menu = True
    while menu==True:
        print("Selamat datang di aplikasi konseling")
        print("1. Cek Jadwal")
        print("2. Exit")
        pilihan_menu = int(input("Silahkan memilih menu anda: "))
    
        if pilihan_menu == 1 :
            pilihan_nim = input("Masukkan NIM : ")
            print('\n')
            print ('=====================================')
            for i in range(len(data_list)):
                if data_list[i] is not None and data_list[i].bookinglist_nim == pilihan_nim:
                    print('Nama : ',data_list[i].bookinglist_name)
                    print('NIM : ',data_list[i].bookinglist_nim)
                    print('HP : ',data_list[i].bookinglist_hp)
                    print('Umur : ',data_list[i].bookinglist_umur)
                elif data_list[i] is None != pilihan_nim:
                    pass
                else:
                    pass

            jadwalbook = []
            n= 0
            for list in jadwal:
                if list.jadwalKonsuler_status== True:
                    if data_list[n]is not None:
                        jadwalbook.append([list.jadwalKonsuler_hari,list.jadwalKonsuler_nama,list.jadwalKonsuler_waktu,    data_list[n]])
                    else:
                        pass
                    n += 1
            
                else:
                    if data_list[n]is not None:
                        jadwalbook.append([list.jadwalKonsuler_hari,list.jadwalKonsuler_nama, list.jadwalKonsuler_waktu,  data_list[n]])
                    else:
                        pass
                    n += 1
            
            if jadwalbook[0][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[0][0])
                print('Waktu booking : ',jadwalbook[0][2])
            elif jadwalbook[0][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[1][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[1][0])
                print('Waktu booking : ',jadwalbook[1][2])
            elif jadwalbook[1][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[2][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[2][0])
                print('Waktu booking : ',jadwalbook[2][2])
            elif jadwalbook[2][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[3][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[3][0])
                print('Waktu booking : ',jadwalbook[3][2])
            elif jadwalbook[3][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[4][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[4][0])
                print('Waktu booking : ',jadwalbook[4][2])
            elif jadwalbook[4][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[5][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[5][0])
                print('Waktu booking : ',jadwalbook[5][2])
            elif jadwalbook[5][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[6][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[6][0])
                print('Waktu booking : ',jadwalbook[6][2])
            elif jadwalbook[6][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[7][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[7][0])
                print('Waktu booking : ',jadwalbook[7][2])
            elif jadwalbook[7][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[8][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[8][0])
                print('Waktu booking : ',jadwalbook[8][2])
            elif jadwalbook[8][3].bookinglist_nim != pilihan_nim:
                pass
            elif jadwalbook[9][3].bookinglist_nim == pilihan_nim:
                print('Hari booking : ',jadwalbook[9][0])
                print('Waktu booking : ',jadwalbook[9][2])
            elif jadwalbook[9][3].bookinglist_nim != pilihan_nim:
                pass
            else:
                pass
            print ('=====================================')
            print('\n')

        elif pilihan_menu == 2 :
            print("Terima kasih telah menggunakan aplikasi ini")
            input("Tekan enter untuk keluar aplikasi")
               
        else:
            print('input invalid')


def login():
    while True:
        
        print("Silahkan login")
        username1 = input("Username: ")
        password1 = input("Password: ")

        file = open("login.txt", "r")

        for line in file: 
            field = line.split(",")
            username = field[0]
            password = field[1]
            lastchar = len(password)-1
            password = password[0:lastchar]
        if username1 == username and password1 == password:
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            break
        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk mencoba lagi...") 
#file.close()
user_data= {}
def admin(): 
    while True:
        print("Silahkan login")
        username = input("Username: ")
        password = input("Password: ")

        if username == username and password == password:
            print("Login berhasil!")
            input("Tekan Enter untuk melanjutkan...")
            break
        else:
            print("Username atau password salah!")
            input("Tekan Enter untuk mencoba lagi...")
            

def user():
    print ("Silahkan melakukan registrasi")
    username = input("Masukan username : ")
    password = input("Masukan password : ")
    confirm_password = input("Konfirmasi Password : ")
    file = open("login.txt","a")
    file.write (username)
    file.write (",")
    file.write (password)
    file.write ("\n")
    file.close
    if password != confirm_password:
        print("Passwords tidak sesuai.")
        return
    if username in user_data:
        print("Username sudah ada.")
        return

    user_data[username] = password
    print("Registrasi selesai!")
    input("Tekan enter untuk login...")
    print(user_data)
    login_user()

def login_user() : 
    print("silhkan login")
    username1 = input('Masukkan username : ')
    password1 = input('Masukkan Password : ')
    file = open('login.txt',"r")
    for row in file: 
            field = row.split(",")   
            username = field[0]
            password = field[1]
            lastchar = len(password)-1
            password = password[0:lastchar]
    if username1 == username and password1 == password:
        print("Login berhasil!")
        input("Tekan Enter untuk melanjutkan...")
        account_found = True
        user_menu()
        if not account_found:
            print("Akun tidak ada!")
    else:
        print("Username atau password salah!")
        input("Tekan Enter untuk mencoba lagi...")
        login_user()


login_utama = input("Apakah anda user / admin ? : ").lower()

if login_utama == 'admin': 
    admin()
elif login_utama == 'user' :
    registrasi_akun = input("Apakah anda sudah memiliki akun? (y/t)").lower()
    if registrasi_akun == 't':
        user()
    else:
        login_user()
'''
registrasi_akun = input("Apakah anda sudah memiliki akun? (y/t)").lower()
if registrasi_akun == 't':
    register()
else:
    login()
login() '''     

ascii_art = """
  __        __   _                            _ 
  \ \      / /__| | ___ ___  _ __ ___   ___  | |
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
    \ V  V /  __/ | (_| (_) | | | | | |  __/ |_|     
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_) 

                             
"""

print(ascii_art)
data_list = [None] * 10
menu = True
while menu==True:
    print("Selamat datang di aplikasi konseling")
    print("1. Registrasi")
    print("2. Tampilkan Jadwal")
    print("3. Cari jadwal booking berdasarkan NIM")
    print("4. Cetak Jadwal ke TXT")
    print("5. Keluar aplikasi")
    pilihan_menu = int(input("Silahkan memilih menu anda: "))

    if pilihan_menu == 1:   
        hariKonseling = input('Masukkan hari Konseling : ') 
        jamkonseling = input("Masukan jam yang ingin pilih (08:00 - 12:00(A) dan 12:00 - 16:00(B)): ")
        if hariKonseling.lower()=='senin' and jamkonseling.lower()=='a':
            if jadwal[0].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 1
                jadwal[0].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
            else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='senin' and jamkonseling.lower()=='b':
            if jadwal[1].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 2
                jadwal[1].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
            else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='selasa' and jamkonseling.lower()=='a':
             if jadwal[2].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 3
                jadwal[2].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='selasa' and jamkonseling.lower()=='b':
             if jadwal[3].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 4
                jadwal[3].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='rabu' and jamkonseling.lower()=='a':
             if jadwal[4].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 5
                jadwal[4].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='rabu' and jamkonseling.lower()=='b':
             if jadwal[5].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 6
                jadwal[5].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='kamis' and jamkonseling.lower()=='a':
             if jadwal[6].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 7
                jadwal[6].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='kamis' and jamkonseling.lower()=='b':
             if jadwal[7].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 8
                jadwal[7].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='jumat' and jamkonseling.lower()=='a':
             if jadwal[8].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 9
                jadwal[8].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')
        elif hariKonseling.lower()=='jumat' and jamkonseling.lower()=='b':
             if jadwal[9].jadwalKonsuler_status == True :
                print("Masukan biodata anda:")
                nama = input("Nama : ")
                nim = input("NIM : ")
                hp = input("No HP : ")
                umur = input("Umur : ")
                id= 10
                jadwal[9].jadwalKonsuler_status = False
                print('Jadwal telah di tambahkan \n')
             else :
                print('Jadwal sudah penuh \n')     
        else:
            print('Input tidak valid')
            
        
        if 'nama' in locals() and 'nim' in locals() and 'hp' in locals() and 'umur' in locals() and 'id' in locals():
            data_konseling = Bookinglist(nama, nim, hp, umur)
            del data_list[id - 1]
            data_list.insert(id - 1, data_konseling)
        else:
            print('Biodata tidak lengkap. Registrasi dibatalkan.\n')


    elif pilihan_menu == 2:
        n= 0
        file = open('jadwal.txt' , 'r')
        for list in jadwal:
            if list.jadwalKonsuler_status== True:
                tersedia = 'Available'
                print ('=====================================')
                print('Hari : ',list.jadwalKonsuler_hari)
                print("Konsuler : ",list.jadwalKonsuler_nama)
                print("Waktu : ",list.jadwalKonsuler_waktu)
                print("Status : ",tersedia)
                print ('=====================================')
                n += 1
            
            else:
                tidakTersedia = 'Not Available'
                print ('=====================================')
                print('Hari : ',list.jadwalKonsuler_hari)
                print("Konsuler : ",list.jadwalKonsuler_nama)
                print("Waktu : ",list.jadwalKonsuler_waktu)
                print("Status : ",tidakTersedia)
                print('di Booking oleh : ',data_list[n].bookinglist_name)
                print('NIM : ',data_list[n].bookinglist_nim)
                print('Umur : ',data_list[n].bookinglist_umur)
                print('No hp : ',data_list[n].bookinglist_hp)
                print ('=====================================')
                n += 1
        
        jawaban = input("Apakah ada yang ingin di hapus ? (y/t)")
        if jawaban.lower() == 'y' :
            tujuanHapus = input('Hari apa yang ingin di hapus ? ')
            tujuanWaktu = input('Masukan jam yang ingin dihapus (08:00 - 12:00(A) dan 12:00 - 16:00(B)):')
            if tujuanHapus.lower() == 'senin' and tujuanWaktu.lower()=='a':
                if jadwal[0].jadwalKonsuler_status == False :
                    jadwal[0].jadwalKonsuler_status = True     
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'senin' and tujuanWaktu.lower()=='b':
                if jadwal[1].jadwalKonsuler_status == False :
                    jadwal[1].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'selasa' and tujuanWaktu.lower()=='a':
                if jadwal[2].jadwalKonsuler_status == False :
                    jadwal[2].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'selasa' and tujuanWaktu.lower()=='b':
                if jadwal[3].jadwalKonsuler_status == False :
                    jadwal[3].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'rabu' and tujuanWaktu.lower()=='a':
                if jadwal[4].jadwalKonsuler_status == False :
                    jadwal[4].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'rabu' and tujuanWaktu.lower()=='b':
                if jadwal[5].jadwalKonsuler_status == False :
                    jadwal[5].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'kamis' and tujuanWaktu.lower()=='a':
                if jadwal[6].jadwalKonsuler_status == False :
                    jadwal[6].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'kamis' and tujuanWaktu.lower()=='b':
                if jadwal[7].jadwalKonsuler_status == False :
                    jadwal[7].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'jumat' and tujuanWaktu.lower()=='a':
                if jadwal[8].jadwalKonsuler_status == False :
                    jadwal[8].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            elif tujuanHapus.lower() == 'jumat' and tujuanWaktu.lower()=='b':
                if jadwal[9].jadwalKonsuler_status == False :
                    jadwal[9].jadwalKonsuler_status = True
                    print('Jadwal telah di hapus \n')
            
            else : 
                print('Input tidak valid')
        else :
            print('\n')
            
    elif pilihan_menu == 3:
        pilihan_nim = input("Masukkan NIM : ")
        print('\n')
        print ('=====================================')
        for i in range(len(data_list)):
            if data_list[i] is not None and data_list[i].bookinglist_nim == pilihan_nim:
                print('Nama : ',data_list[i].bookinglist_name)
                print('NIM : ',data_list[i].bookinglist_nim)
                print('HP : ',data_list[i].bookinglist_hp)
                print('Umur : ',data_list[i].bookinglist_umur)
            elif data_list[i] is None != pilihan_nim:
                pass
            else:
                pass

        jadwalbook = []
        n= 0
        for list in jadwal:
            if list.jadwalKonsuler_status== True:
                if data_list[n]is not None:
                    jadwalbook.append([list.jadwalKonsuler_hari,list.jadwalKonsuler_nama,list.jadwalKonsuler_waktu,data_list[n]])
                else:
                    pass
                n += 1
            
            else:
                if data_list[n]is not None:
                    jadwalbook.append([list.jadwalKonsuler_hari,list.jadwalKonsuler_nama,list.jadwalKonsuler_waktu,data_list[n]])
                else:
                    pass
                n += 1
            
        if jadwalbook[0][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[0][0])
            print('Waktu booking : ',jadwalbook[0][2])
        elif jadwalbook[0][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[1][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[1][0])
            print('Waktu booking : ',jadwalbook[1][2])
        elif jadwalbook[1][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[2][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[2][0])
            print('Waktu booking : ',jadwalbook[2][2])
        elif jadwalbook[2][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[3][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[3][0])
            print('Waktu booking : ',jadwalbook[3][2])
        elif jadwalbook[3][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[4][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[4][0])
            print('Waktu booking : ',jadwalbook[4][2])
        elif jadwalbook[4][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[5][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[5][0])
            print('Waktu booking : ',jadwalbook[5][2])
        elif jadwalbook[5][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[6][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[6][0])
            print('Waktu booking : ',jadwalbook[6][2])
        elif jadwalbook[6][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[7][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[7][0])
            print('Waktu booking : ',jadwalbook[7][2])
        elif jadwalbook[7][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[8][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[8][0])
            print('Waktu booking : ',jadwalbook[8][2])
        elif jadwalbook[8][3].bookinglist_nim != pilihan_nim:
            pass
        elif jadwalbook[9][3].bookinglist_nim == pilihan_nim:
            print('Hari booking : ',jadwalbook[9][0])
            print('Waktu booking : ',jadwalbook[9][2])
        elif jadwalbook[9][3].bookinglist_nim != pilihan_nim:
            pass
        else:
            pass
        print ('=====================================')
        print('\n')
    elif pilihan_menu == 4:
        n= 0
        file = open("Jadwal.txt", "w")
        for list in jadwal:
            
            if list.jadwalKonsuler_status== True:
                tersedia = 'Available'
                
                file.write ('=====================================' + '\n')
                file.write('Hari : '+list.jadwalKonsuler_hari  + '\n')
                file.write("Konsuler : "+list.jadwalKonsuler_nama + '\n')
                file.write("Waktu : "+list.jadwalKonsuler_waktu + '\n')
                file.write("Status : "+tersedia + '\n')
                file.write ('=====================================' + '\n')
                n += 1
            
            else:
                tidakTersedia = 'Not Available'
                file.write ('=====================================' + '\n')
                file.write('Hari : ' + list.jadwalKonsuler_hari + '\n')
                file.write("Konsuler : "+list.jadwalKonsuler_nama + '\n')
                file.write("Waktu : "+list.jadwalKonsuler_waktu + '\n')
                file.write("Status : "+tidakTersedia + '\n')
                file.write('di Booking oleh : '+data_list[n].bookinglist_name + '\n')
                file.write('NIM : '+data_list[n].bookinglist_nim + '\n')
                file.write('Umur : '+data_list[n].bookinglist_umur + '\n')
                file.write('No hp : '+data_list[n].bookinglist_hp + '\n')
                file.write('=====================================' + '\n')
                
                n += 1 
        file.close()
    elif pilihan_menu == 5:
        print("Terima kasih telah menggunakan aplikasi ini")
        input("Tekan enter untuk keluar aplikasi")
        break
        
    else:
            print("Input tidak valid")



