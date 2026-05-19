while True:
    plec = "string"
    while (plec != "k" and plec != "m"):
        print("Podaj swoją płeć k-kobieta m-mężczyzna")
        plec = str(input())
    print("Podaj swoją masę w kg: ")
    x = int(input())
    suma = 10 * x
    print("Podaj swój wzrost w cm: ")
    x = int(input())
    suma += int(6.25 * x)
    print("Podaj swój wiek: ")
    x = int(input())
    suma -= 5 * x
    if(plec == "k"):
        suma -= 161
    else:
        suma += 5
    print("Twoje PPM to:", suma, "kcal" ); print()
