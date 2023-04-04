@echo off
echo ####################################################
echo #  A lot of Tools for DoS/DDoS, and                #
echo #  to hack sql servers, and to cheat               #
echo #  kahhot, and liveworksheets. And much            #
echo #  more. Use of the program is your responsibility.#
echo ####################################################
timeout 5
goto choice

:choice
set /P c= [Type the number you want!] [1]: DoS/DDoS [2]: kahoot cheat [3]: liveworksheets cheat [4]: sql hack [5]: soon ~
if /I "%c%" EQU "1" goto 1
if /I "%c%" EQU "2" goto 2
if /I "%c%" EQU "3" goto 3
if /I "%c%" EQU "4" goto 4
if /I "%c%" EQU "5" goto 5
goto choice


:1
echo please wait...
git clone https://github.com/palahsu/DDoS-Ripper.git
timeout 2
exit

:2
git clone https://github.com/nitro-n7/kahoot-cheats.git
timeout 2
exit

:3
echo press f12 in liveworksheets and copy commands.js code to console (inside devtools)
git clone https://github.com/RealNattawattHongthong/liveworksheet-cheat.git
timeout 5
exit

:4
echo soon
timeout 5
exit

:5
echo soon
timeout 5
exit