def registrar_equipo(numero_integrantes, nombre_equipo):
    integrantes = []
    for i in range(numero_integrantes):
        integrante = {
            "nombre": input("Digita tu nombre: "),
            "correo": input("Digita tu correo: "),
            "contrasena": input("Digita tu contrasena: ")
        }
        integrantes.append(integrante)
    return integrantes

def calcular_nota_general(integrantes, notas_eficiencia, notas_estabilidad, notas_modelo):

    # Mostrar todos los integrantes del equipo
    print("\n--- INTEGRANTES DEL EQUIPO ---")
    for idx, miembro in enumerate(integrantes, start=1):
        print(f"Integrante {idx}: Nombre: {miembro['nombre']} | Correo: {miembro['correo']}")

    promedio_eficiencia = sum(notas_eficiencia) / len(notas_eficiencia)
    promedio_estabilidad = sum(notas_estabilidad) / len(notas_estabilidad)
    promedio_modelo = sum(notas_modelo) / len(notas_modelo)
    
    nota_final = (0.8 * promedio_estabilidad) + (0.1 * promedio_eficiencia) + (0.1 * promedio_modelo)
    
    return nota_final