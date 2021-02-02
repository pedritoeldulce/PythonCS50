personas =[
    {"name":"Paolo", "lastname":"Perez"},
    {"name":"Karina", "lastname":"Justiniano"},
    {"name":"Filomena", "lastname":"Ttito"}
]

#Funciones Lambda
personas.sort(key=lambda personas:personas["lastname"])
print(personas)