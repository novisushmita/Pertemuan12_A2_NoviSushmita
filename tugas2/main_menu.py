from bangundatar.menu import menu
from bangundatar.persegi import persegi
from bangundatar.lingkaran import lingkaran
from bangundatar.segitiga import segitiga

menu()
while True:                                                                                                                                                         
    menu_choice = int(input("Pilih bentuk 2D (1/2/3/4): "))

    if menu_choice == 1:
        persegi()
    elif menu_choice == 2:
        lingkaran()
    elif menu_choice == 3:
        segitiga()
    elif menu_choice == 4:
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
