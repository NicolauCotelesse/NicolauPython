#!/usr/bin/python3

import math

def circulo(raio):
    print("A área do círculo é: ", math.pi * raio **2 )

if __name__ == '__main__':

    raio = float(input("informe o raio: "))
    circulo(raio)