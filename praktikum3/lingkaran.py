# Meminta pengguna untuk memasukkan jari-jari lingkaran
jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))

# Menghitung luas lingkaran
luas = 3.14159265359 * jari_jari ** 2

# Menghitung keliling lingkaran
keliling = 2 * 3.14159265359 * jari_jari

# Menampilkan hasil
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah {keliling:.2f}")
