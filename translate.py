from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import string

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

file = open(filename, "r").read()

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbols = '[](){}<>=+-!?@#$%^&*_:;"\'\/.,'

split = file.split("\n")

final_parsed = []

# bloctans_4 = Symbols and numbers
# bloctans = lowercase lettter
# Bloctans = capital letter
# alphie = next letter over
# Alphie = tab

for i in split:
    final_parsed.append("")
    for i2 in range(len([*i])):
        index = [*i][i2]

        if index in symbols:
            final_parsed[-1] += "bloctans_4 " * (symbols.index(index) + 1)
        elif index in lowercase:
            final_parsed[-1] += "bloctans " * (lowercase.index(index) + 1)
        elif index in uppercase:
            final_parsed[-1] += "Bloctans " * (uppercase.index(index) + 1)
        elif index == "\t" or index == " ":
            final_parsed[-1] += "Alphie "
        else:
            print(final_parsed[-1])
        
        # Very hacky fix
        if i2 + 1 < len([*i]):
            final_parsed[-1] += "alphie "

final = ""

# Same here
for i in final_parsed:
    if final == "":
        final += i + "\n"
    else:
        final += "alphie " + i + "\n"

print("File translated, writing to a file")
open("./output/translate/"+filename.split("/")[-1].split(".")[0]+".bloctans", "w").write(final)