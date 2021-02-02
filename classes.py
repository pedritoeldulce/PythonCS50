# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# punto = Point(3,6)
# print(punto.x)
# print(punto.y)


''' El método __init__ es un método especial de una clase de Python,
El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos, 
self: hace referencia al mismo objeto


'''

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # self: esta funcion será trabajado como objeto
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["Paolo", "Karina", "Filomena", "Noa"]


for p in people:
    if flight.add_passenger(p):
        print(f"added {p} para vuelo con exito ")
    else:
        print(f"Asiento no disponible para  {p}")