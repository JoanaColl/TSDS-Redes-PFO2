
import requests

def registrar():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    r = requests.post("http://localhost:5000/registro", json={"usuario": usuario, "contraseña": contraseña})
    print(r.json())

def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    r = requests.post("http://localhost:5000/login", json={"usuario": usuario, "contraseña": contraseña})
    print(r.json())

def ver_tareas():
    r = requests.get("http://localhost:5000/tareas")
    print("HTML recibido:\n", r.text)

opciones = {
    "1": registrar,
    "2": login,
    "3": ver_tareas
}

while True:
    print("\n1) Registrarse\n2) Iniciar sesión\n3) Ver tareas\n4) Salir")
    opcion = input("Elegí una opción: ")
    if opcion == "4":
        break
    accion = opciones.get(opcion)
    if accion:
        accion()
    else:
        print("Opción inválida")