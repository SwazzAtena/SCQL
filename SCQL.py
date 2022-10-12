#!/usr/bin/env python3 

import os

os.system("pkg install toilet")
os.system("clear")
os.system("toilet -f bigmono12 SCQL -F gay")
print("""

1)İnformation About The Target Site(Site Hakkında Bilgi Toplama)
2)Fast Port Scanner(Hızlı Port Tarama)
3)Version İnformation(Versiyon Bilgisi)
4)SQL Dork Scanner(SQL Açık Tarama)

""")

islemno= input("Select The Number :")

if islemno=="1":
  hedefip= input("Enter Target Site: ")
  os.system("whois "+hedefip)
elif islemno=="2":  
  hedefip= input("Enter Targer The Site: ")
  os.system("nmap "+hedefip)
elif islemno=="3":
  hedefip= input("Enter Target Site: ")
  os.system("nmap -sV "+hedefip)
elif islemno=="4":
  hedefip= input("Enter Dork: ")
  os.system("sqlmap -g "+hedefip)
  
