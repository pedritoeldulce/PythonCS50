def announce(f):
    def wrapper():
        print("Apunto de ejecutar la función")
        f()
        print("Función ejecutada")
    return wrapper # return the function of wrapper

@announce
def hello():
    print("hola mundo")
    

hello()

# DEcorator: tomand una funcion y la modifican, agregando algún comportamiento adicional a la función
# @: indica el decorador

'''
Se agregó el decorador a la function
@announce
def hello():
    print("asda")
'''