#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WER   BIN   ICH?")
print("""
\033[31mHata Almamak İcin İlk Önce Numarayı 0 Yapın                                                              
\033[92mNmap Kısayolları                   \033[97m|  \033[92mWorldlist Kısayolları    \033[97m|  \033[92mBrute Force Kısayolları
                                   \033[97m|                           | 
\033[33m[01] Hizli Tarama                  \033[97m|  \033[33m[05] Cupp.py Başlatma    \033[97m|  \033[33m[07] İnstax Başlatma
\033[33m[02] Servis Ve Versiyon Bilgisi    \033[97m|                           |
\033[33m[03] Isletım Sıstemı Bilgisi       \033[97m|  \033[92mFake Site Script         \033[97m|
                                   \033[97m|                           \033[97m|
                                   |  \033[33m[06] Blackeye Başlatma   \033[97m|
                                   |                           |
                                   |                           |
""")

islemno = input("\033[94mIslem Numarası Giriniz: ")

if(islemno=="1"):
               hedefip = input("\033[94mHedef İp Girin: ")
               os.system("nmap " + hedefip)
elif(islemno=="2"):
               hedefip = input("\033[94mHedef İp Girin: ")
               os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
               hedefip = input("\033[94mHedef İp Girin: ")
               os.system("nmap -o " + hedefip)
elif(islemno=="4"):
               os.system("zenmap")
elif(islemno=="5"):
               os.system("python3 Tools/Cupp.py/cupp.py -i")
elif(islemno=="6"):
               os.system("bash Tools/Blackeye/blackeye.sh")
elif(islemno=="7"):
               os.system("bash Tools/İnstax/instax.sh")
elif(islemno=="0"):
               os.system("pkg install nmap")

else:
  print("\033[31mHatalı Secim Yaptın")


