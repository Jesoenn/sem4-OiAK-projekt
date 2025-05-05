# sem4-OiAK-projekt
Projekt mnożenia Montgomery'ego.

## Włączenie symulacji w terminalu

#### Przejdź do katalogu z projektem:

```bash
cd <ścieżka_do_projektu>
```
#### Pomoc
```bash
montgomery.py --help
```
#### Przykładowe odpalenie
```bash
# Odpalenie dla algorytmu SOS dla 10 słów 64 bitowych i zapis wyniku do pliku Testy.txt
montgomery.py 0 10 64 --file Testy.txt 
```
#### Format pliku wyjściowego
```
Algorytm  Słowa  Bity_Na_Słowo  Suma_Bitów  Czas[ms]  Poprawne?(True/False)
```
#### Przykładowy plik wyjściowy
```
CIOS	10	100	1000	0,506	True
CIOS	10	100	1000	0,499	True
CIOS	10	100	1000	0,953	True
CIOS	10	100	1000	0,727	True
CIOS	10	100	1000	0,5	True
SOS	10	100	1000	0,512	True
SOS	10	100	1000	0,486	True
SOS	10	100	1000	0,488	True
SOS	10	100	1000	0,496	True
SOS	10	100	1000	0,545	True
```

