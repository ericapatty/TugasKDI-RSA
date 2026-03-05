# Implementasi Algoritma RSA Menggunakan Python

Repository ini berisi implementasi sederhana algoritma kriptografi **RSA (Rivest-Shamir-Adleman)** menggunakan bahasa pemrograman Python. Program ini dibuat untuk mendemonstrasikan bagaimana proses pembangkitan kunci, enkripsi, dan dekripsi pada algoritma RSA bekerja.


## Tentang RSA

RSA adalah algoritma kriptografi **asimetris**, yaitu algoritma yang menggunakan dua kunci berbeda dalam prosesnya:

- **Public Key** digunakan untuk melakukan enkripsi
- **Private Key** digunakan untuk melakukan dekripsi

Keamanan RSA didasarkan pada kesulitan dalam memfaktorkan bilangan besar menjadi faktor prima.

RSA banyak digunakan dalam berbagai sistem keamanan digital, seperti:
- HTTPS (SSL/TLS)
- Digital Signature
- Email Encryption
- Sistem keamanan komunikasi internet


## Tahapan Algoritma RSA

Program ini mengimplementasikan langkah-langkah dasar RSA sebagai berikut:

1. Memilih dua bilangan prima **p** dan **q**
2. Menghitung nilai **n = p × q**
3. Menghitung **phi(n) = (p−1)(q−1)**
4. Menentukan nilai **e** sebagai public exponent
5. Menentukan nilai **d** sebagai private exponent
6. Membentuk **Public Key (e, n)** dan **Private Key (d, n)**
7. Mengubah plaintext menjadi nilai ASCII
8. Melakukan proses **enkripsi**
9. Melakukan proses **dekripsi** untuk mendapatkan kembali plaintext


## Rumus RSA

Proses Enkripsi:
C = M^e mod n

Proses Dekripsi:
M = C^d mod n

Keterangan:
- M = plaintext
- C = ciphertext
- e = public key
- d = private key
- n = hasil perkalian p dan q


## Cara Menjalankan Program

1. Pastikan Python sudah terinstall di komputer.
2. Download atau clone repository ini.
3. Buka file `prosesRSA.py`.
4. Jika ingin menggunakan bilangan prima yang berbeda, ubah nilai `p` dan `q` pada kode program.
5. Jalankan program dengan perintah berikut:

python prosesRSA.py

6. Masukkan pesan yang ingin dienkripsi ketika program meminta input.

Program kemudian akan menampilkan proses pembangkitan kunci, enkripsi, dan dekripsi secara bertahap.


## Contoh Output Program

```
================================
IMPLEMENTASI ALGORITMA RSA
================================

1. Bilangan Prima
p = 17
q = 11

2. Menghitung n = p * q
n = 187

3. Menghitung phi = (p-1)(q-1)
phi = 160

4. Menentukan nilai e
e = 3

5. Menentukan nilai d
d = 107

6. Kunci RSA
Public Key  = (3, 187)
Private Key = (107, 187)

Masukkan pesan yang akan dienkripsi: HALO

Ciphertext = [...]

Hasil Dekripsi = HALO
```


## Author

Nama: Frederica Gabrielle Jovita Patty
NIM: 24051204049
