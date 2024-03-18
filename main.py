# esercizio 1
mia_tupla = ()
print(mia_tupla)
# esercizio 2
frutta = ("mela", "banana", "kiwi")
print(frutta)
# esercizio 3
banana = frutta[1]
print(banana)
# esecizio 4
prima_tupla = frutta[:2]
print(prima_tupla)
# esercizio 5
if "ananas" in frutta:
    print("l'elemento 'ananas' è presente nella tupla")
else:
    print("l'elemento 'ananas' non è presente nella tupla")
# esercizio 6
nuova_tupla = frutta + ("pesca", "arancia")
print(nuova_tupla)
# esercizio 7
lunghezza = len(frutta)
# esercizio 8
numeri = (1, 2, 3, 4, 5)
print(numeri)
# esercizio 9
numeri_quadrati = tuple(i ** 2 for i in range(1, 6))
print(numeri_quadrati)
# esercizio 10
occorrenze = frutta.count("mela")
print(occorrenze)