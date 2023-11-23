def main():
    print("Selamat Datang di Pizza Hut Delivery")
    print("Silahkan pilih menu")
    print("Toping pizza:")
    print("1. Frankfurter")
    print("2. Meat Monsta")
    print("3. Super Supreme")
    print("4. Super Supreme Chicken")

    pilihan_pizza = int(input("Pilih toping pizza anda (nomer 1-4): "))
    if pilihan_pizza == 1:
        pizza = "Frankfurter"
        harga_pizza = 43636
    elif pilihan_pizza == 2:
        pizza = "Meat Monsta"
        harga_pizza = 43636
    elif pilihan_pizza == 3:
        pizza = "Super Supreme"
        harga_pizza = 43636
    elif pilihan_pizza == 4:
        pizza = "Super Supreme Chicken"
        harga_pizza = 43636
    else:
        print("Pilihan tidak tersedia. Silakan pilih pizza yang tersedia.")
        return
    
    print("Silahkan pilih ukuran")
    print("1. personal")
    print("2. regular")
    print("3. large")
    pilihan_ukuran = int(input("Pilih ukuran pizza anda (nomer 1-3): "))
    if pilihan_ukuran == 1:
        ukuran = "personal"
        harga_ukuran = 0
    elif pilihan_ukuran == 2:
        ukuran = "regular"
        harga_ukuran = 57.273
    elif pilihan_ukuran == 3:
        ukuran = "large"
        harga_ukuran = 89.091
    else:
        print("Ukuran tidak tersedia. Silakan pilih ukuran yang tersedia.")
        return
    
    print("Silahkan pilih crust")
    print("1. pan")
    print("2. stufferedcrust cheese")
    print("3. stufferedcrust sausage")
    print("4. cheesy bites")
    print("5. crown crust")
    pilihan_crust = int(input("Pilih crust pizza anda (nomer 1-5): "))
    if pilihan_crust == 1:
        crust = "pan"
        harga_crust = 0
    elif pilihan_crust == 2:
        crust = "stuffedcrust cheese"
        harga_crust = 11.819
    elif pilihan_crust == 3:
        crust = "stuffedcrust sausage"
        harga_crust = 9.091
    elif pilihan_crust == 4:
        crust = "cheesy bites"
        harga_crust = 13.637
    elif pilihan_crust == 5:
        crust = "crown crust"
        harga_crust = 11.818
    else:
        print("crust tidak tersedia. Silakan pilih crust yang tersedia.")
        return
    cheese = input("Apakah anda ingin menambah extra cheese? (ya/tidak): ")
    harga_cheese = 13000 if cheese.lower() == "ya" else 0
    total_harga = harga_pizza + harga_ukuran + harga_crust + harga_cheese
    print("Terima kasih telah memilih Pizza Hut Delivery!") 
    print("Tagihan akhir anda adalah: Rp",total_harga)
    
if __name__=="__main__":
    main()