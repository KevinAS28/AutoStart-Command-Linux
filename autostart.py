#!/usr/bin/python3.5

import subprocess
import threading
import os
import time
#import jadwall //udah lama(setiap 3 hari)
import daemon
command = [
"gsettings set org.gnome.desktop.background show-desktop-icons false",
"mount /dev/sda1 /media/root/0CA22FB60ACC5707",
"pulseaudio",
"start-pulseaudio-x11",
"gnome-system-monitor",
"swapon /dev/sda6",
"python3 /root/programming/python_saya/jadwal_baru.py",
#"komorebi",
"zenity --question --text 'pwn-request-urllib-binascii-z3--angr-data_recovery-regex, improve forthell with every knowledge you have, New project? seriously with this fucking question'",
"zenity --question --text 'python range dan join blom bisa? fungsi lannya? itertools, product\n  saat anda merasa pintar, disaat itulah anda paling bodoh'",
"zenity --question  --text 'c++ advance: geeksforgeeks, tutorialpoint, bogotobogo'",
"python /root/programming/python_saya/baterai.py",
"gnome-terminal -- 'iotop -d 2'",
"gnome-terminal -- 'smartctll'",
"gnome-terminal -- 'htop'",
"gnome-terminal -- 'tail -f /var/log/kern.log'"
"gnome-terminal"
]

command1 = [

]

def runcom(command):
 print(subprocess.check_output(command, shell=True))
 
for i in command:
 try:
  #with daemon.DaemonContext():
  to_run1 = threading.Thread(target=runcom, args=[i]).start()
 except:
  print("error while running: %s" %(i))
  continue

