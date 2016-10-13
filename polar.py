# coding: utf-8
from math import sqrt, atan2, pi, sin, cos

class Polar:
    "Operaciones con coordenadas polares."
    
    def __init__(self, num="nada", angulo="nada"):
        if num == "nada":
            self.d = self.a = 0  
        elif angulo == "nada":
            'num es cadena de la forma "<d, a>"'
            num = num[1:-1]
            d, a = num.split(",")
            self.d = float(d)
            grados, resto = a.split("º")
            grados = int(grados)
            signo = -1 if grados < 0 else 1  # el signo sólo va en los grados
            minutos, segundos = resto.split("'")[:2]
            minutos = int(minutos)
            segundos = float(segundos)
            self.a = (grados + signo*minutos/60 + signo*segundos/3600)*pi/180
        else:
            "num es la distancia, angulo está en grados"
            self.d = num
            self.a = float(angulo)*pi/180

    def _gms(self, angulo):
        "Cadena con grados, minutos y segundos a partir de angulo decimal en radianes."
        angulo= angulo*180/pi
        grados = int(angulo)
        angulo = abs(60 * (angulo - grados))  # abs(x) es el valor absoluto (valor positivo) de x
        minutos = int(angulo)
        segundos = 60 * (angulo - minutos)
        return "{}º {}' {:.4f}''".format(grados, minutos, segundos)
    
    def dameD(self):
        "getter"
        return self.d
    
    def dameA(self):
        "getter"
        return self.a
    
    def cambiaD(self, d):  # setter
        "setter"
        self.d = d
    
    def cambiaA(self, a):  # setter
        "setter"
        self.a = a
    
    def __str__(self):
        "Lo que debe mostrar al pedir que imprima un Polar"
        return "<{:.2f}, {}>".format(self.d, self._gms(self.a))
    
    def aRectangulares(self):
        "Muestra el Polar en coordenadas rectangulares."
        return self.d * cos(self.a), self.d * sin(self.a)
    
    def deRectangulares(self, x, y):
        "Extrae los valores de las coordenadas rectangulares dadas."
        self.d, self.a = sqrt(x**2 + y**2), atan2(y, x)  # arco tangente con grados estandarizados

    def __add__(self, otro):  # ver https://docs.python.org/3/reference/datamodel.html
        "Métodos especiales. Lo que se debe entender cuando se pide se sumen dos polares."
        x1, y1 = self.aRectangulares()
        x2, y2 = otro.aRectangulares()
        res = Polar()
        res.deRectangulares(x1+x2, y1+y2)
        return res
    
    def aRadianes(self):
        return self.a
        
p = Polar()
p.deRectangulares(-3,4)
print("p=", p, p.aRectangulares())

q = Polar("<6.00, 153º 7' 48.3685''>")
print("q=", q, q.aRectangulares())

print("p+q=", p+q, (p + q).aRectangulares())
