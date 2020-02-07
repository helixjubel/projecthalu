import os
import sys
import time
from termcolor import colored
ossystem('clear')
def run(teks):
    putih = "\033[0m"
    merah = "\033[91m"
    teks = teks+" "
    try:
        num = 0
        while num < 1:
            for i,char in enumerate(teks):
                if i == 0:
                    sys.stdout.write('\r%s%s%s%s' % (putih,char.lower(),merah,teks[1:])),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        zbl = teks[0].lower()
                        sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[2:])),
                        sys.stdout.flush()
                    else:
                        if i == i:
                            zbl = teks[0:i].lower()
                            sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[i+1:])),
                            sys.stdout.flush()
                    time.sleep(0.1)
            num += 1
    except: exit()

run("||=============||RaisaSedangDibangunkan||===========||")
os.system('termux-tts-speak saya sudah bangun tuan kuching, saya akan menghidupkan program')
os.system('clear')
time.sleep(2)
print(colored('>>>>>>> Menghidupkan Program <<<<<<<','red', attrs=['bold']))
time.sleep(1)
print(colored('>>>>>>> Menghidupkan Program <<<<<<<','white', attrs=['bold']))
time.sleep(2)
print(colored('>>>>>>> Menghidupkan Program <<<<<<<','white', attrs=['bold']))
timesleep(2)
def run(teks):
    putih = "\033[0m"
    merah = "\033[91m"
    teks = teks+" "
    try:
        num = 0
        while num < 1:
            for i,char in enumerate(teks):
                if i == 0:
                    sys.stdout.write('\r%s%s%s%s' % (putih,char.lower(),merah,teks[1:])),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        zbl = teks[0].lower()
                        sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[2:])),
                        sys.stdout.flush()
                    else:
                        if i == i:
                            zbl = teks[0:i].lower()
                            sys.stdout.write('\r%s%s%s%s%s%s' % (merah,zbl,putih,char.lower(),putih,teks[i+1:])),
                            sys.stdout.flush()
                    time.sleep(0.3)
            num += 1
    except: exit()

run("L O A D I N G ...............")
os.system('clear')
baner= """                 ____ ____ _ ____ ____ 
                |__/ |__| | [__  |__| 
                |  \ |  | | ___] |  | 
                                      
           ___  ____ ____  _ ____ ____ ___ 
           |__] |__/ |  |  | |___ |     |  
           |    |  \ |__| _| |___ |___  |  
                                           
     ___  _ _  _ _ ___  _  _ ___  _  _ ____ _  _ 
     |  \ | |__| | |  \ |  | |__] |_/  |__| |\ | 
     |__/ | |  | | |__/ |__| |    | \_ |  | | \| 
                                                 
"""
print(colored(baner,'green'))
os.system('termux-tts-speak Raisa Project Dihidupkan')
os.system('clear')
tai= """
=============================
Author  : Kuching
Contact : 081250654041
Mail    : iqbal298077@gmail.com
=============================
Raisa v1.5 Tools Penghancur Bumi
"""
os.system('clear')
print(colored(tai,'cyan'))
print(colored(tai,'white'))
print(colored('[1]. Hack The Planet >','cyan', attrs=['bold']))
print(colored('[2]. Hack Nasa >','cyan', attrs=['bold']))
print(colored('[3]. Control The Satelite >','cyan', attrs=['bold']))
print(colored('[4]. Send Signal To Alien >','cyan', attrs=['bold'])) 
print(colored('[5]. Instal System Nuklir USA >','cyan', attrs=['bold']))
print(colored('[6]. Instal System Nuklir Rusia >','cyan', attrs=['bold']))
print(colored('[7]. Password End The World >','cyan', attrs=['bold']))
print(colored('[8]. Tiket Pesan Masuk Surga >','cyan', attrs=['bold']))
print(colored('[9]. Exit','red', attrs=['bold']))
os.system('termux-tts-speak selamat datang di Raisa Project, Saya Adalah Suatu Program Yang Dibuat Oleh Tuan Chucky, saya adalah tools penghancur bumi segera pindah')
x = str (input ('Silahkan Masukan Nomber >  ' ))
