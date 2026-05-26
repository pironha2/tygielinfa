cenaul = 40
cenador = 80
print("Witaj w sklepie powerlandii 3 największego parku rozrywki w Polsce \nPodaj swoje imię: ")
name = input()
print("Witaj", name, "podaj swój wiek:")
age = int(input())

if age < 18 or age >= 70:
    ulgowy = True
else:
    ulgowy = False
print("Podaj swój wzrost: ")
height = int(input())

if height >= 170:
    minwz = True
else:
    minwz = False

if ulgowy:
    print("koszt:", cenaul, "zł")
    if minwz:
        print("Możesz korzystac ze wszystkich atrakcji parku")
    else:
        print("Możesz korzystać z atrakcji dla klientów poniżej 170 cm")
else:
    print("koszt:", cenador, "zł")
    if minwz:
        print("Możesz korzystac ze wszystkich atrakcji w parku")
    else:
        print("Możesz korzystać z atrakcji dla klientów poniżej 170 cm")
