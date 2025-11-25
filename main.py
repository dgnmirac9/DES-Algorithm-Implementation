from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import binascii

#OgrenciNoSon2Hane.
ogrenciNumaram = '18' 

#18'i byte formatina cevirdik.
data = ogrenciNumaram.encode('utf-8')

#Anahtar belirleme
key = b'Rastgele' 
#8 byte'lık anahtar 

#DES algoritmasi veriyi 8 byte'lik gruplar halinde sifreler. 
#Bosluga yer yoktur. 18 -> 2 byte -> kalan 6 byte'i da doldurmamiz gerek.
#Bunun icin padding islemine basvuracagiz.
#block_size -> DES blok boyutu
padded_data = pad(data, block_size=8)

print(f"Orijinal Veri: {data}")
print(f"Padding (Dolgu) yapilmis veri (hex): {binascii.hexlify(padded_data)}")

#Sifreleme 
#ECB -> Sifreleme modu
cipher = DES.new(key, DES.MODE_ECB)
sifreli_veri = cipher.encrypt(padded_data)

#Sonuclar
print("-" * 30)
print(f"Kullanilan anahtar: {key}")
print(f"Sifrelenmis veri (hex): {binascii.hexlify(sifreli_veri).decode('utf-8').upper()}")
print("-" * 30)