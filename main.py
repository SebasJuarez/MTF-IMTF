from mtf import move_to_front, improved_mtf

# Definimos las secuencias de acceso que se utilizarán en los problemas
def get_sequences():
    return [
        [0, 1, 2, 3, 4] * 4, # Secuencia problema 1
        [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4],  # Secuencia problema 2
        [2] * 20,  # Secuencia problema 5 parte 1
        [3] * 20   # Secuencia problema 5 parte 2
    ]

# Función para elegir el algoritmo a utilizar - Se elige entre MTF e IMTF
def elegir_algoritmo():
    while True:
        print("\n¿Qué algoritmo deseas usar?")
        print("1. MTF")
        print("2. IMTF")
        opcion = input("Opción: ")
        if opcion == "1":
            return move_to_front, "MTF"
        elif opcion == "2":
            return improved_mtf, "IMTF"
        else:
            print("Opción inválida. Intenta de nuevo.")

# Función para imprimir los resultados de los accesos y el costo total acumulado
def print_result(logs, total_cost):
    print("\n--- Resultados del Acceso ---\n")
    print(f"{'Paso':<5} {'Configuración actual':<30} {'Solicitud':<10} {'Costo':<6}")
    print("-" * 60)

    for i, (config, solicitud, cost) in enumerate(logs, 1):
        config_str = ", ".join(map(str, config))
        print(f"{i:<5} [{config_str:<27}] {solicitud:<10} {cost:<6}")

    print("\nResumen:")
    print(f"Total de accesos: {len(logs)}")
    print(f"Costo total acumulado: {total_cost}")
    print("-" * 60)

# Función principal - Menu para elegir el problema a resolver
def main():
    while True:
        print("\nProyecto - MTF & IMTF")
        print("1. Secuencia 1: [0,1,2,3,4] * 4")
        print("2. Secuencia 2: [4,3,2,1,0,...]")
        print("3. Mejor caso (mínimo costo)")
        print("4. Peor caso (máximo costo)")
        print("5. Secuencia repetida [2]*20 y [3]*20")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "6":
            print("Saliendo del programa.")
            break

        algoritmo, nombre_algoritmo = elegir_algoritmo()
        sequences = get_sequences()

        # Problema 1 - Secuencia [0,1,2,3,4] repetida 4 veces
        if opcion == "1":
            print(f"\nEjecutando secuencia 1 utilizando {nombre_algoritmo}")
            total_cost, logs = algoritmo([0,1,2,3,4], sequences[0])
            print_result(logs, total_cost)

        # Problema 2 - Secuencia [4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4]
        elif opcion == "2":
            print(f"\nEjecutando secuencia 2 utilizando {nombre_algoritmo}")
            total_cost, logs = algoritmo([0,1,2,3,4], sequences[1])
            print_result(logs, total_cost)

        # Problema 3 - Mejor caso usando la secuencia [0] 20 veces
        elif opcion == "3":
            print(f"\nMejor caso - {nombre_algoritmo}")
            mejor = [0] * 20
            print(f"Secuencia usada: {mejor}")
            total_cost, logs = algoritmo([0,1,2,3,4], mejor)
            print_result(logs, total_cost)

        # Problema 4 - Peor caso usando la secuencia [4,3,2,1,0] 4 veces
        elif opcion == "4":
            print(f"\nPeor caso - {nombre_algoritmo}")
            peor = [4,3,2,1,0] * 4
            print(f"Secuencia usada: {peor}")
            total_cost, logs = algoritmo([0,1,2,3,4], peor)
            print_result(logs, total_cost)

        # Problema 5 - Desarrollo usando secuencias repetidas de 2 y 3 20 veces cada una
        elif opcion == "5":
            print(f"\nDesarrollo usando {nombre_algoritmo}")
            print("\nSecuencia repetida con 2")
            total_cost_2, logs_2 = algoritmo([0,1,2,3,4], sequences[2])
            print_result(logs_2, total_cost_2)

            print("\nSecuencia repetida con 3")
            total_cost_3, logs_3 = algoritmo([0,1,2,3,4], sequences[3])
            print_result(logs_3, total_cost_3)

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
