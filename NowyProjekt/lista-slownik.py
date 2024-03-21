# Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy

# imie = ['Luther', 'Jacob', 'Harry', 'Maggie', 'Jenna', 'Greg', 'Jacob',
#         'Maggie', 'Linda', 'David']
#
# osoba = input("Podaj imię osoby: ")
# if osoba in imie:
#   id = imie.index(osoba)
#   print(f"Indeks imienia {osoba}: {id}")
#
# ilosc = imie.count(osoba)
# print(f"Ilość osób o imieniu {osoba}: {ilosc}")
#
# new = 'Jason'
# imie.append(new)
# print(imie)
#
# new1 = 'Milton'
# imie.insert(2, new1)
# print(imie)
#
# imie.sort()
# imie.pop()
# print(imie)
#
# i = ['Brian', 'Carlos', 'Alex']
# imie.extend(i)
# print("Nowa lista:" , imie)

# Zadanie 2
# Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
# jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
# następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika

# słownik = {
#        'imie': ['Krzysztof', 'Borys', 'Marcin'],
#        'nazwisko': ['Trytka', 'Paciorek', 'Kocięcki'],
#        'wiek': ['36', '45', '39'] }
#
# numer = int(input("Numer osoby (0,1,2):"))
#
# if numer in range(len(słownik['imie'])):
#
#     print("Dane osoby:".format(numer))
#     print("Imię:", słownik['imie'][numer])
#     print("Nazwisko:", słownik['nazwisko'][numer])
#     print("Wiek:", słownik['wiek'][numer])

#Zadanie 3
# Do poprzednio utworzonego słownika dodaj nowy klucz o nazwie "kierunek_studiów", wartość w/w klucza dowolna
# wskazana przez użytkownika

# słownik = {
#     'imie': ['Krzysztof', 'Borys', 'Marcin'],
#     'nazwisko': ['Trytka', 'Paciorek', 'Kocięcki'],
#     'wiek': ['36', '45', '39']
# }
#
# numer = int(input("Numer osoby (0, 1, 2): "))
#
# if numer in range(len(słownik['imie'])):
#     print("Dane osoby:")
#     print("Imię:", słownik['imie'][numer])
#     print("Nazwisko:", słownik['nazwisko'][numer])
#     print("Wiek:", słownik['wiek'][numer])
#
#
#     kierunek_studiów = input("Podaj kierunek studiów: ")
#     słownik['kierunek_studiów'] = kierunek_studiów
#
#     print("Kierunek studiów:", kierunek_studiów)

#Zadanie 4
# Wyświetl nazwy kluczy poprzednio utworzonego słownika, oraz ilość jego elementów

# słownik = {
#        'imie': ['Krzysztof', 'Borys', 'Marcin'],
#        'nazwisko': ['Trytka', 'Paciorek', 'Kocięcki'],
#        'wiek': ['36', '45', '39'],
# }
#
# numer = int(input("Numer osoby (0,1,2):"))
#
# if numer in range(len(słownik['imie'])):
#
#     print("Dane osoby:".format(numer))
#     print("Imię:", słownik['imie'][numer])
#     print("Nazwisko:", słownik['nazwisko'][numer])
#     print("Wiek:", słownik['wiek'][numer])
#
# keys=słownik.keys()
# print("Nazwy kluczy :", keys)
#
# s=len(keys)
# print("Ilość elementów: ",s)







