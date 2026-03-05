def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_e(phi):
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            return e
        e += 1

def find_d(e, phi):
    d = 1
    while True:
        if (d * e) % phi == 1:
            return d
        d += 1

print("\n================================")
print("   IMPLEMENTASI ALGORITMA RSA   ")
print("================================\n")

# pilih bilangan prima
p = 17
q = 11

print("1. Bilangan Prima")
print("p =", p)
print("q =", q)

n = p * q
print("\n2. Menghitung n = p * q")
print("n =", n)

phi = (p - 1) * (q - 1)
print("\n3. Menghitung phi = (p-1)(q-1)")
print("phi =", phi)

e = find_e(phi)
print("\n4. Menentukan nilai e")
print("e =", e)

d = find_d(e, phi)
print("\n5. Menentukan nilai d")
print("d =", d)

print("\n6. Kunci RSA")
print("Public Key  =", (e, n))
print("Private Key =", (d, n))

plaintext = input("\nMasukkan pesan yang akan dienkripsi: ")

print("\n7. Konversi karakter ke ASCII")
ascii_values = []
for char in plaintext:
    val = ord(char)
    ascii_values.append(val)
    print(char, "->", val)

print("\n8. Proses Enkripsi")
cipher = []
for num in ascii_values:
    c = (num ** e) % n
    cipher.append(c)
    print(num, "^", e, "mod", n, "=", c)
print("\nCiphertext =", cipher)

print("\n9. Proses Dekripsi")
decrypted = ""
for c in cipher:
    p_val = (c ** d) % n
    char = chr(p_val)
    decrypted += char
    print(c, "^", d, "mod", n, "=", p_val, "->", char)

print("\nHasil Dekripsi =", decrypted)
print("\n==== Proses RSA selesai ====\n")