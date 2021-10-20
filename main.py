import math
from math import sqrt
"Exercitiul 1"
def citire_lista():
    result_list = []
    dimensiune = int(input("Dimensiune lista:"))

    while dimensiune:
        element = int(input("Introduceti un element:"))
        result_list.append(element)
        dimensiune -= 1

    return result_list #returnam lista citita




"Exercitiul 2"
def lista_numere_negative(lista):
    rezult_list = []
    for i in lista:
        if i < 0: #daca un numar e negativ il adaugam in lista
            rezult_list.append(i)
    return rezult_list #returnam lista modificata

def test_lista_numere_negative():
    assert lista_numere_negative([-1,3,4,5,-4]) == [-1,-4]
    assert lista_numere_negative([1,2,3,4,5]) == []

test_lista_numere_negative()







"Exercitiul 3"
def numar_minim_egal_cu_ultima_cifra(lista, cifra):
        numarmic = None
        for i in lista:
                if i % 10 == cifra: #daca numarul are ultima cifra egala cu cifra citita atunci:
                    if numarmic == None or i < numarmic: #daca nu avem pana acum un numr sau daca avem unul
                        numarmic = i #dar termenul curent este mai mic, actualizam numarul minim
        return numarmic #returnam numarul minim

def test_numar_minim_egal_cu_ultima_cifra():
        assert numar_minim_egal_cu_ultima_cifra([10,12,13,14,15,100],0) == 10
        assert numar_minim_egal_cu_ultima_cifra([1,2,3,4,5,555], 5) == 5

test_numar_minim_egal_cu_ultima_cifra()

def is_prime(numar):
    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(numar)) + 1, 2): #aflam daca un numar este prim
        if numar % x == 0: #daca numarul se imparte la x returnam fals, deoarece nu e prim
            return False
    return True


def main():
    lista = []
    shouldRun = True
    while shouldRun:
        option = input("Alegeti optiunile: 1-Citeste lista, 2-rezolva problema 2, 3-rezolva problema 3, x-inchide meniul:")
        if option == "1":
            print ("Cititi lista:")
            lista = citire_lista()
        elif option == "2":
            print ("Rezolvati problema 2:afisarea numerelor negative nenule din lidta!")
            print (lista_numere_negative(lista))
        elif option == "3":
            print ("Rezolvati problema 3:afisarea numarului minim care are ultima cifra egala cu o cifra citita!")
            cifra_citita = int(input("Dati o cifra:"))
            print(numar_minim_egal_cu_ultima_cifra(lista, cifra_citita))
        elif option == "x":
            print("Ati inchis meniul!")
            shouldRun = False
main()