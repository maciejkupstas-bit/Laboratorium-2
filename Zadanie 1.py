
punkty = int(input("Podaj liczbę zdobytych punktów: "))

if punkty > 80:
    print("Student zalicza egzamin w terminie 0.")
elif punkty >= 50:
    print("Student może poprawić wynik.")
else:
    print("Student musi poprawić egzamin.")
