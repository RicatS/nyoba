from nyoba import jadwal 
from nyoba import data_list


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

    elif pilihan_menu == 2 :
        print("Terima kasih telah menggunakan aplikasi ini")
        input("Tekan enter untuk keluar aplikasi")
        
          
    else:
        print('input invalid')






# def login_user():
#     print("Silahkan login")
#     username1 = input('Masukkan username: ')
#     password1 = input('Masukkan Password: ')
#     file = open('login.txt', "r")
#     account_found = False
    
#     for row in file:
#         field = row.split(",")
#         username = field[0]
#         password = field[1].strip()  # Remove trailing newline character

#         if username1 == username and password1 == password:
#             print("Login berhasil!")
#             input("Tekan Enter untuk melanjutkan...")
#             account_found = True
#             break
    
#     file.close()

#     if not account_found:
#         print("Akun tidak ada!")
#         user()


# # Writing data to a text file
# with open("data.txt", "w") as file:
#     file.write("This is some data.")

# # Reading data from the text file
# with open("data.txt", "r") as file:
#     data = file.read()
