def operaciones():
    seleccion=0
    while (seleccion!=5):
               print ("1.Suma")
               print ("2.Resta")
               print ("3.Multiplicacion")
               print ("4.Division")
               print ("5.Salir")
               seleccion=int(input("Dame opcion: "))
               if((seleccion==1)):
                   print(suma())
               elif((seleccion==2)):
                   print(resta())
               elif((seleccion==3)):
                   print(multiplicacion())
               elif((seleccion==4)):
                   print(division())
                   
def suma():
    a=int(input("numero 1: "))
    b=int(input("numero 2: "))
    print("El resultado de la suma es:",(a+b))  
def resta():
    a=int(input("numero 1: "))
    b=int(input("numero 2: "))
    print("El resultado de la resta es:",(a-b))
def multiplicacion():
    a=int(input("numero 1: "))
    b=int(input("numero 2: "))
    print("El resultado de la multiplicacion es:",(a*b))
def division():
    a=int(input("numero 1: "))
    b=int(input("numero 2: "))
    print("El resultado de la division es:",(a/b))
    
