import os

select = input("Convert (Convert .bloctans to .py) or Translate (Convert .py to .bloctans?")

print("Ok!")
if select.lower() == "convert":
    os.system("convert.py")
elif select.lower() == "translate":
    os.system("translate.py")
else:
    input("Invalid selection, press enter to restart selection")
    os.system("main.py")