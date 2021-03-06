#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Richard Rodriguez"
__email__ = "r.rvangaurdia@gmail.com"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    if numero_1 > numero_2:
       print("el numero mayor es {}" .format(numero_1 , numero_2))
    elif numero_2 > numero_1:
       print("el numero mayor es {}" .format(numero_2 , numero_1))
    if numero_1 <=0 :
        print(" el numero negativo es {}".format(numero_1))
    elif numero_2 <=0:
        print("el numero negativo es {}".format(numero_2))
    if (numero_1 > 0 and numero_1 < 100):
        print("cumple la condicion")
    else:
        (numero_1 < 0 and numero_1 > 100)
        print("no cumple la condicion")
    if  (numero_1 < 10 or numero_2 > -2):
        print("se cumple la condicion")
    else:
        (numero_1 > 10 or numero_2 < -2)
        print("no se cumple la condicion")


    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición


def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    if texto_1 > texto_2:
        print("palabra mayor alfabeticamente {}".format(texto_1))
    elif texto_2 > texto_1:
         print("palabra mayor alfabeticamente {}".format(texto_2))
    if texto_1 > texto_2:
        print("la palabra tiene letras ", len(texto_1))
    if texto_1 > texto_2:
        print("mayor cantidad de caracteres ", min(texto_1))
    else:
        texto_1 < texto_2
        print("mayor cantidad de caracteres " , min(texto_2))

        


    


        

    #texto 1 guapa tex 2 glam 

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    copia_texto_1 = texto_1

    if texto_1 == copia_texto_1:
        print ("los textos son iguales")
    
    else:
        texto_1 != copia_texto_1
        print("los textos no son iguales")

                                # Copia de la variable texto_1

    


    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2
    if numero_1 > 5:
        print("N_1 es mayor")
    if  numero_2 >0:
        print("Resp=1")
    elif numero_2<0:
        print("Resp=2") 
    if numero_1 > 5:
        print("Resp_3") 
    else:
         numero_2 > 5 
         print("Resp_4")


    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = int(input("ingrea tu nota{}"))
    puntaje = 70
    if puntaje >= 90:
        print("A")
    elif puntaje >= 80:
        print("B")  
    elif puntaje >= 70:
        print("c")  
    elif puntaje >= 60:
        print("D")
    else:
        puntaje <= 60
        print("F")




    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
