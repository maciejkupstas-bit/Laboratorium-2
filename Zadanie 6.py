litera = input("Podaj jedną literę: ")

if litera.isupper():
    print("Duża litera")
elif litera.islower():
    print("Mała litera")
else:
    print("To nie jest litera")