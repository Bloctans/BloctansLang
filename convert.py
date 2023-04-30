# IDEA:
# its just python
# every line you need to put [String] a certain amount of times
# Bloctans = capital letter
# bloctans_4 = Symbols and numbers
# bloctans = lowercase lettter
# alphie = next letter over
# Alphie = tab
# symbol list: [](){}<>=+-!@#$%^&*_:;"'\/.,
# for line breaks, line break then continue, then you add alphie
#
# this is everything for the project

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import string

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

file = open(filename, "r").read()

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
symbols = '[](){}<>=+-!?@#$%^&*_:;"\'\/.,'

final_parsed = []
currentline = 0

final = ""

_split_alphies = file.split("alphie")

for i in _split_alphies:
    convert_to_letter = i.split(" ")
    convert_to_letter = [x for x in convert_to_letter if x != "\n"]
    convert_to_letter = [x for x in convert_to_letter if x]

    _len = len(convert_to_letter)-1

    if len(final_parsed) == currentline:
        final_parsed.append("")

    if convert_to_letter == []:
        final_parsed[currentline] += ""
    else:
        if convert_to_letter[0] == "bloctans":
            final_parsed[currentline] += lowercase[_len]
        elif convert_to_letter[0] == "Bloctans":
            final_parsed[currentline] += uppercase[_len]
        elif convert_to_letter[0] == "bloctans_4":
            final_parsed[currentline] += symbols[_len]
        elif convert_to_letter[0] == "Alphie":
            final_parsed[currentline] += " "
    
    if "\n" in i:
        currentline += 1

for i in final_parsed:
    final += i + "\n"

print("File translated, writing to a file")
open("./output/convert/"+filename.split("/")[-1].split(".")[0]+".py", "w").write(final)
run = input("Run file?(Y/n) ")
if run.lower() == "y":
    print("RUNNING "+filename.split("/")[-1])

    exec(final)