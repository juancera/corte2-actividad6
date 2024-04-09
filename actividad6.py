perro = {}
perro = {"nombre": "Fido", "color": "Café", "raza": "Labrador", "patas": 4, "edad": 5}
estudiante = {"nombre": "Juan", "apellido": "cera", "sexo": "M", "edad": 20, "estado_civil": "Soltero", "skills": ["Python", "Java"], "pais": "colombia", "ciudad": "cartagena", "direccion": "olaya"}
print(len(estudiante))  
habilidades = estudiante["skills"]
print(type(habilidades)) 
estudiante["skills"].append("JavaScript")
estudiante["skills"].append("HTML")
print(estudiante["skills"])  # Output: ['Python', 'Java', 'JavaScript', 'HTML']
claves = list(estudiante.keys())
print(claves)  # Output: ['nombre', 'apellido', 'sexo', 'edad', 'estado_civil', 'skills', 'pais', 'ciudad', 'direccion']
valores = list(estudiante.values())
print(valores)  # Output: ['Juan', 'cera', 'M', 20, 'Soltero', ['Python', 'Java', 'JavaScript', 'HTML'], 'colombia', 'cartagena', 'olaya']
tuplas = list(estudiante.items())
print(tuplas)  # Output: [('nombre', 'Juan'), ('apellido', 'cera'), ('sexo', 'M'), ('edad', 20), ('estado_civil', 'Soltero'), ('skills', ['Python', 'Java', 'JavaScript', 'HTML']), ('pais', 'colombia'), ('ciudad', 'cartagena'), ('direccion', 'olaya')]
del estudiante["skills"]
print(estudiante)  # Output: {'nombre': 'Juan', 'apellido': 'cera', 'sexo': 'M', 'edad': 20, 'estado_civil': 'Soltero', 'pais': 'colombia', 'ciudad': 'cartagena', 'direccion': 'olaya'}
del perro