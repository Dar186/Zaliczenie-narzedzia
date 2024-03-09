# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy

imie = ['Luther', 'Jacob', 'Harry', 'Maggie', 'Jenna', 'Greg', 'Jacob',
        'Maggie', 'Linda', 'David']
print(imie)
ind = imie.index("Luther")
print(ind)
ind2 = imie.count("Maggie")
print(ind2)

imie.append('Jason')
print(imie)

imie.insert(2, 'Milton')
print(imie)

imie.sort()
print(imie)
# imie.remove(5)
print(imie)

i = ['Brian', 'Carlos', 'Alex']
imie.extend(i)
print(imie)
