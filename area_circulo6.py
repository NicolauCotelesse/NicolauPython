#!/usr/bin/python3

import math


def circulo(raio):
    return math.pi * raio**2

if (__name__ == "__main__"):
    raio = float(input("Diga o raio: "))
    area = circulo(raio)



print("A área do círculo é: ",area)