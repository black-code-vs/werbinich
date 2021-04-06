#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WER   BIN   ICH?")
print("""
Wer bin ich Aracına Hoş Geldin

        \033[92mNmap Kısayolları        \033[97m|
                                \033[97m|
\033[93m[01] Hizli Tarama               \033[97m|
\033[93m[02] Servis Ve Versiyon Bilgisi \033[97m|
\033[93m[03] Isletım Sıstemı Bilgisi    \033[97m|
                                \033[97m|
                                \033[97m|

""")

islemno = input("\033[94mIslem Numarası Giriniz: ")

if(islemno=="1"):
               hedefip = input("\033[94mHedef İp Girin: ")
               os.system("nmap " + hedefip)
elif(islemno=="2"):
               hedefip = input("\033[94mHedef İp Girin: ")
               os.system("nmap -sS -sV " + hedefip)
elif(islemno=="2"):
               hedefip = input("\033[94mHedef İp Girin: ")
               os.system("nmap -0 " + hedefip)
else:
  print("\033[31mHatalı Secim Yaptın")


