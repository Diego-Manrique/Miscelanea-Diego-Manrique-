#1. operadores

# Area del triangulO abajo 

#print("Hello guys welcome to area generator ")
#base = float(input ("Porfavor digite la base del triangulo \n"))
#altura = float (input ("porfavor digite la altura \n"))
#area = base * altura / 2
#print("El resultado del are es : " + str(area))



#suma de los numeros abajo 

#print("Hello este es el sumador de numeros")
#numero1  = int (input ("Porfavor digite el primer numero \n"))
#numero2 = int (input ("porfavor digite el segundo numero\n"))
#operacion = numero1 + numero2
#print("El resultado de los nmeros sumados es: " + str(operacion))




#numero elevado al cuadrado aqui abajo 

#print ("Hello aqui podemos sacar el resultado de un numero elevado")
#N1 = int(input("porfavor digite el numero "))
#operacion = N1 **2
#print("El resultado de los numeros sumados es: " + str(operacion))




# euros a dolares aqui abajo 

#print ("Hello aqui podemos sacar ela convercion de euros a dolares")
#euros = float(input("digite una cifra a convertir "))
#operacion = euros  * 1.05
#print("El resultado de euros a dolares es: " + str(operacion))




# algoritmo area de un cuadrado 

#print("Hello guys welcome to area generator ")
#lado = int (input ("Porfavor digite el lado del cuadrado \n"))
#area = lado ** 2
#perimetro = lado* 4
#print("El resultado del area es : " + str(area) )
#print("El resultado del perimetro es : " + str(perimetro) )




#area y volumen de un cilindro

#print("hello aqui determinamos el area y el volumen de un cilindro")
#radio = int(input("porfavor digite el radio \n"))
#area = 3.14 * radio **2
#vol = 2 * 3.14 * area
#print ("el resultado del radio es:" + str (area))
#print ("el resultado del volumen es: " + str (vol))




# algoritmo que lea el radio de una circunferencia

#print("hello aqui determinamos el radio y la cicunferencia \n ")
#rad  = int(input ("Porfavor digite el radio \n "))
#area = 3.14 * rad **2
#long = 2 * 3.14 * rad 
#print ("el area es igual a: \n "  + str (area)) 
#print ("la logitud es igual a: \n " + str (long))




#promedio de tres numeros 

#print ("hello aqui determinamos el promedio de tres numeros")
#n1 = int(input ("porfavor digite el primer numero:  \n"))
#n2 = int(input ("porfavor digite el primer numero:  \n"))
#n3 = int(input ("porfavor digite el primer numero:  \n"))
#numero1  = n1 + n2 +n3 / 3
#print ("el promedio de los tres numeros es igual a: \n" + str (numero1))




# 2. Condicionales


#positivo y negativo aqui abajo 

#print("hello aqui determinamos si un numero es negativo o positivo  \n ")
#Numero1 = int(input ("porfavor digite el primer numero\n "))
#if (Numero1 > 0 ):
  #print (" el numero digitado es positivo ")
#if (Numero1 < 0 ):
  #print (" el numero digitado es negativo ") 
#if (Numero1 == 0 ):
  #print (" el numero digitado es neutro ")




#algorito de dos numeros aqui 

#print("hello aqui determinamos dos numeros para saber cual es el mayor o el menor  \n ")
#Numero1 = int(input ("porfavor digite el primer numero\n "))
#Numero2 = int(input ("porfavor digite el segundo numero\n ")) 

#if (Numero1 > Numero2 ):
  #print (" el numero digitado " + str (Numero1), "es mayor que " + str (Numero2))
#if (Numero1 < Numero2 ):
  #print (" el numero digitado " + str (Numero1), "es menor que " + str (Numero2))
#if (Numero1 == Numero2 ):
  #print (" el numero digitado " + str (Numero1), "es igual que " + str (Numero2))




# programa que lea tres numeros 

#print("hello aqui determinamos tres numeros \n ")
#Numero1 = int(input ("porfavor digite el primer numero\n "))
#Numero2 = int(input ("porfavor digite el segundo numero\n ")) 
#Numero3 = int(input ("porfavor digite el tercer numero\n ")) 

#list = [Numero1, Numero2, Numero3]
#list.sort()

#mayor = (list [2])
#menor = (list [0]) 

#print ("el numero mayor es  ",  str (mayor), ("\nel numero menor es  "),  str (menor))

#datos a y b restandolos 

#print("hello aqui determinamos dos numeros para sumar o restar \n ")
#Numero1 = int(input ("porfavor digite el primer numero\n "))
#Numero2 = int(input ("porfavor digite el segundo numero\n ")) 

#if (Numero1 >= Numero2 ): 
  #print (" la resta es " + str (Numero1 - Numero2))
#else:
  #if (Numero1 <= Numero2 ):
    #print (" la suma es " + str (Numero1 + Numero2))


#hdfghdhxf

#print("hello aqui encontraremos el cociente entre A y B. \n ")
#dividendo = float(input ("porfavor digite el dividendo \n "))
#divisor  = float(input ("porfavor digite el divisor\n ")) 

#if  divisor == 0:
  #print("no fue posible dividir por 0") 
#else:
  #if divisor > 0:
    #print ("El resultado es: " + str (dividendo / divisor))

#Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.

#print("Aqui determinaremos dos numeros positivo o negativo ")
#numero1 = int(input ("porfavor digite el primer numero \n "))
#numero2  = int(input ("porfavor digite el segundo numero\n ")) 
#if ((numero1 < 0) or (numero2 < 0)):
  #print ("el numero restado es: " + str  (numero1 + numero2))
#else:
  #if ((numero1 > 0) and (numero2 > 0)):
    #print ("el numero multiplicado es:" + str  (numero1 * numero2))




#Escribir un algoritmo que determine si un año es bisiesto o no

#print("aqui determinaremos si el año es bisiesto")
#año = int(input("porfavor digite el año\n "))

#if (año % 4 == 0 and (año % 100 != 0)) or (año % 400 == 0):
  #print ("Este año", str (año) + "es bisiento ")

#else:
  #print("Este año", str (año) + "no es bisiesto")

#3. Ciclos

# Imprimir todos los múltiplos de 3 que hay entre 1 y 100.
#print (" Multiplos del 3 hasta 100 ")
#resultado = 3
#while resultado < 98:
  #resultado +=3
  #print (resultado)

#Imprimir los números impares entre 0 y 100.
#print(" numeros impares de 0 a 100")
#numero = 1
#while numero < 100:
  #numero += 2
  #print(numero)  

#Imprimir los números pares del 1 al 100.

#print(" numeros impares de 0 a 100")
#numero = 0
#while numero < 100:
  #numero += 2
  #print(numero)  

#Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30."

#print("cuadrados del 1 al 30")
#for numero in range(1, 31):
  #numero = numero ** 2
  #print(numero) 



#Escribir un programa que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla.
#igual = 0
#print("suma de cuadrados")
#for numero in range (1, 101, 1):
  #numero = numero ** 2
  #igual = igual + numero
  #print(igual) 

#Sumar todos los números que se digitan por teclado mientras no sea cero.
#a = 1
#y = 0
#while a != 0:
  #x = int(input("Porfavor digite los numeros a sumar\n"))
  #if x == 0:
    #a = 0
  #else:
    #y = y + x
  #print (y)



