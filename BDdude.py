import os, sys
os.system("git pull")
os.system('xdg-open https://chat.whatsapp.com/G6gj4XIXczyGnDrzbfH6Ek')
try:
    __import__("NIKI").menu()
except Exception as e:
    exit(str(e))
