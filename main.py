import ast
class Biblioteka(list):
  def dodaj_ksiazke(self, kasiazka):
    self.append(ksiazka)

  def wydruk(self):
    wynik = sorted(set([(ksiazka.tytul, ksiazka.autor, self.count(ksiazka)) for ksiazka in self]), key = lambda x: x[0])
    for ksiazka in wynik:
      print(ksiazka)

class Ksiazka():
  def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

  

biblioteka = Biblioteka()
liczba_egzemplarzy = int(input())
for i in range(liczba_egzemplarzy):
  krotka = eval(input())
  tytul = krotka[0]
  autor = krotka[1]
  rok = krotka[2]
  ksiazka = Ksiazka(tytul, autor, rok)
  biblioteka.dodaj_ksiazke(ksiazka)

biblioteka.wydruk()
