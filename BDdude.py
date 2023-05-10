import os, sys
os.system("git pull")
os.system('xdg-open https://chat.whatsapp.com/FvEW9ARKwOOLVTJIzd8SKH')
try:
    __import__("NIKI").menu()
except Exception as e:
    exit(str(e))
