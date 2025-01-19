#Archivo main para ejecutuar la cálculadora.

from suma import suma
from resta import resta
from division import division
from multiplicacion import multiplicacion
from sumaAvanzada import sumAva

def obtener_numeros():
    cantidad = int(input("¿Con cunatos numeros vamos a operar para la suma avanzada?. "))
    numeros = [] 
    for i in range(cantidad):
        num = float(input(f"Ingresa el número {i+1}: "))
        numeros.append(num)
    return numeros
    
    



def mostrar_menu():
    print ("\nCálculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Suma Avanzada")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = (input("Elige una operación (1-6): ")) 

        if opcion == "6":
            print("¡Gracias por usar la cálculadora!")
            break
        if opcion == "5":
            numeros = obtener_numeros()
            resultado = sumAva(numeros)
            print(f"El resultado de la suma avanzada es: {resultado} ")

        if opcion in ["1","2","3","4"]:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            


            if opcion == "1":
                resultado = suma(num1, num2)
                print(f"El resultado de la suma es: {resultado} ")
            elif opcion == "2":
                resultado = resta(num1, num2)
                print(f"El resultado de la resta es: {resultado} ")
            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
                print(f"El resultado de la multiplicación es: {resultado} ")  
            elif opcion == "4":
                resultado = division(num1, num2)
                print(f"El resultado de la división es: {resultado} ") 

            else:
                print("Opcion no valida.") 




if __name__ == "__main__":
    main()








    
    


