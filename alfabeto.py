#Definimos el lenguajes
L = {"a", "b", "ab", "ba", "aa"}   

#Pedimos al usurio una palabra
palabra = input("Ingrese una palabra: ")

def pertenece(palabra):
    """Verifica si la palabra pertenece a L"""
    return palabra in L

#Se Verifica si pertenece al lenguaje 
if palabra in L:
    print("Sí: la palabra pertenece a L")
else:
    print("No: la palabra NO pertenece a L")
