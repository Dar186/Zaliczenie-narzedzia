## 1. Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) Ile zdań jest w analizowanym tekście?

# word = ('Któregoś dnia w zeszłym tygodniu dokładnie o 9:29 pochyliłam się nerwowo nad klawiaturą komputera gotowa do walki ze sztucznym tworem o nazwie Emma.'
#         'Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. '
#         'Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza.')
# #a
# print("Ilosc wystapien slowa Emma:", (word.count('Emma')))
# #b
# print(word.upper())
# #c
# print(word.split())

## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)

# x = int(input("Wartość x:"))
# y = int(input("Wartość y:"))
#
# wyr = 2*x+5*y
# print("Wynik wyrazenia 2x+5y:" ,wyr)


## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)


# a =(input("Imie: "))
# b =(input("Nazwisko: "))
# c =(input("Liczba: "))
# d =(input("Kierunek studiów: "))
#
# napis = f"Jestem {a} {b} mam {c} lat studiuję {d}"
#
# print(napis)

# 4. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646

# działanie = "1+2+10+20000001+4+347586970885"
# wynik = "321784560456434534646"
#
#
# if działanie == wynik:
#         print("Suma się zgadza")
# else:
#         print("Wynik nie zgadza się")
