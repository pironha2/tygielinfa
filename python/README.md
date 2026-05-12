# Operatory w Pythonie

## W Pythonie wyróżniamy poniższe operandy
- artmetyczne
- logiczne
- relacyjne
- przypisania
- identycznosciowe
- przynależnosci
- bitowe

## Operatory artmetyczne.
Służą do wykonywania wszelkiego rodzaju działan na liczbach takich jak:
- '+'  dodawanie
- '-'  odejmowanie
- '*'  mnożenie
- '/'  dzielenie
- '//' dzielenie całk
- '%'  reszta z dzielenia dwóch liczb całk
- '**' potęgowanie
```
a = 5
b = 3
c = a / b
print(c)
c = a // b
print(c)
c = a ** b
print(c)
```

## Operatory logiczne. 
Mają zastosowanie w miejscach gdzie występują różnego rodzaju warunki. Głównie w pętlach i instrukcjachwarunkowych do nich zaliczamy:
- 'or'  lub logiczne 	zwraca prawdę gdy conajm jeden z warunków jest prawdziwy 
- 'and' i logiczne	zwraca prawdę gdy wszystkie warunki są prawdziwe
- 'not' zaprzeczenie	zwraca prawdę gdy warunek jest fałszywy
```
n=5
k=7
print(n>3 or k>10)
print(n>3 and k>10)
print(not(n>3 and k>10))
```

## Operatory relacyjne.
Stosujemy w sytułacjach gddy jest potrzeba porównania 2 elementów. Najczęściej w instrukcjach warunkowych i iteracyjnych. Wyróżniamy:
- "<"   mniejszy
- ">"   większy
- "<="  mniejszy bądz równy
- ">="  większy bądz równy
- "=="  równy
- "!="  nie równy
```
a = 5
print("a = ", a)
if (4<=a<=6):
    print("wart zmiennej między 4 a 6")

a = 5
b = 5
print("a = ", a, ", b = ", b)
if (a==b):
    print("wart zmiennych są równe")

a = 5
b = 6
print("a = ", a, ", b = ", b)
if (a != b):
    print("wart zmiennych są różne")
```

## Operatory przypisania.
Przypisanie polega na nadaniu wartości dla zmiennej znajdującej się po lewej stronie wartości po prawej stronie. 
- Podstawowym operatorem przypisania jest "="
```
a = 45
print("a =", a)
b = a
print("b =", b)
a = 2 ** 10
print("a =", a)
```
- Przypisanie mozna dokonać poprzedzając je pewną operacją
```
a =   45
print("a =", a)
a +=  10
print("a =", a)
a -=  50
print("a =", a)
a **= 3
print("a =", a)
a //= 30
print("a =", a)
```

## Operatory identycznosciowe
Operatory te okreslają czy dwie zmienne przechowują ten sam obiekt. Wyróżniamy:
- is
- notis
```
x = "kot"
y = "pies"
if x is not y:
    print("Obiekty są różne")
if x is y:
    print("Obiekry są identyczne")
```
## Operatory przynależności
Operatory tego typu sprawdzają czy dany element znajduje się w podzbiorze wart danego obiektu. Mamy dwa takie operatory:
- in
- not in
```
x = "ala ma kota"
if "ma" in x:
    print("wyraz ma występuje w ", x )
y = [ 2, 3, 4 , 67]
if "4" in y:
    print("jest 4 w ", y)
else:
    print("niema 4 w ", y)
```
## Instrukcje warunkowe:
- if
- if else
- if elif
- if in
