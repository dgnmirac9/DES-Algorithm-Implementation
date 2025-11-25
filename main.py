from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import binascii

#Fatih hoca son 2 hanesini şifrelememizi istedi.
ogrenciNumaram = '18' 

#18'i byte formatına çevirdik.
data = ogrenciNumaram.encode('utf-8')

#Anahtar belirleme
key = b'MiracBey' 
#8 byte'lık anahtar 

#DES algoritması veriyi 8 byte'lık gruplar halinde şifreler. 
#Boşluğa yer yoktur. 18 -> 2 byte -> kalan 6 byte'ı da doldurmamız gerek.
#Bunun için padding işlemine başvuracağız.
#block_size -> DES blok boyutu
padded_data = pad(data, block_size=8)

print(f"Orijinal Veri: {data}")
print(f"Padding (Dolgu) yapilmis veri (hex): {binascii.hexlify(padded_data)}")

#Şifreleme 
#ECB -> Şifreleme modu
cipher = DES.new(key, DES.MODE_ECB)
sifreli_veri = cipher.encrypt(padded_data)

#Sonuçlar
print("-" * 30)
print(f"Kullanilan anahtar: {key}")
print(f"Sifrelenmis veri (hex): {binascii.hexlify(sifreli_veri).decode('utf-8').upper()}")
print("-" * 30)