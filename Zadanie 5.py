with open("notowania_gieldowe.txt", "r") as plik:
    zawartosc = plik.read()

if zawartosc.endswith("\n"):
    separator = ""
else:
    separator = "\n"

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write(separator + "ALR, 113\n")