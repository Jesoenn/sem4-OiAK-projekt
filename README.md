# sem4-OiAK-projekt
Projekt mnożenia Montgomery'ego.

## Włączenie symulacji w terminalu

1. Przejdź do katalogu z projektem:

```bash
cd <ścieżka_do_projektu>
```
2. Pomoc
```bash
montgomery.py --help
```
3. Przykładowe odpalenie
```bash
# Odpalenie dla algorytmu SOS dla 10 słów 64 bitowych i zapis wyniku do pliku Testy.txt
montgomery.py 0 10 64 --file Testy.txt 
```
4. Format pliku wyjściowego
```
Algorytm  Słowa  Bity_Na_Słowo  Suma_Bitów  Czas[ms]  Poprawne?(True/False)
```
