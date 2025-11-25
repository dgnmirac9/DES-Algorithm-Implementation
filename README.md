# DES Algoritması ile Veri Şifreleme

Bu proje, Fırat Üniversitesi Yazılım Mühendisliği bölümü **Bilgi Sistemleri ve Güvenliği** dersi kapsamında geliştirilmiştir. Python `pycryptodome` kütüphanesi kullanılarak, DES (Data Encryption Standard) algoritmasının temel çalışma prensibini ve padding (dolgu) mantığını göstermeyi amaçlar.

## 🎯 Proje Amacı

Öğrenci numarasının son 2 hanesini (örneğin "18") alarak:
1. ASCII formatından Byte formatına dönüştürmek,
2. DES algoritmasının gerektirdiği 64-bit (8 Byte) blok boyutuna tamamlamak (PKCS7 Padding),
3. Simetrik bir anahtar ile şifrelemek,
4. Sonucu Hexadecimal (Onaltılık) formatta sunmaktır.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Kütüphane:** PyCryptodome
* **Algoritma:** DES (ECB Modu)

## 🚀 Kurulum ve Çalıştırma

Projeyi bilgisayarınıza klonlayın:
```bash
git clone https://github.com/dgnmirac9/DES-Algorithm-Implementation.git
cd DES-Algorithm-Implementation

pip install -r requirements.txt

python main.py