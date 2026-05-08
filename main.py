INF = 10**9


def cambio_monedas_dp(monto):
    monedas = [1, 5, 10, 25]

    dp = [INF] * (monto + 1)
    anterior = [-1] * (monto + 1)

    dp[0] = 0

    for cantidad in range(1, monto + 1):
        for moneda in monedas:
            if cantidad >= moneda:
                if dp[cantidad - moneda] + 1 < dp[cantidad]:
                    dp[cantidad] = dp[cantidad - moneda] + 1
                    anterior[cantidad] = moneda

    resultado = {25: 0, 10: 0, 5: 0, 1: 0}
    actual = monto

    while actual > 0:
        moneda = anterior[actual]
        resultado[moneda] += 1
        actual -= moneda

    return resultado, dp[monto]


def mostrar_cambio_monedas():
    monto = int(input("Ingrese el monto en centavos: "))

    monedas, total = cambio_monedas_dp(monto)
    nombres = {
        25: "Q0.25",
        10: "Q0.10",
        5: "Q0.05",
        1: "Q0.01"
    }

    print("\nResultado usando programacion dinamica")
    print(f"Monto: Q{monto / 100:.2f}")

    for moneda in [25, 10, 5, 1]:
        if monedas[moneda] > 0:
            print(f"{nombres[moneda]}: {monedas[moneda]} moneda(s)")

    print(f"Total de monedas: {total}")


def knapsack_fraccionado_diccionarios(articulos, capacidad):
    articulos_ordenados = sorted(
        articulos,
        key=lambda articulo: articulo["precio"] / articulo["peso"],
        reverse=True
    )

    solucion = []
    valor_total = 0
    espacio = capacidad

    for articulo in articulos_ordenados:
        if espacio <= 0:
            break

        cantidad_tomada = min(articulo["peso"], espacio)
        valor_por_unidad = articulo["precio"] / articulo["peso"]
        valor_obtenido = cantidad_tomada * valor_por_unidad

        solucion.append({
            "nombre": articulo["nombre"],
            "cantidad": cantidad_tomada,
            "valor": valor_obtenido
        })

        valor_total += valor_obtenido
        espacio -= cantidad_tomada

    return solucion, valor_total


def mostrar_knapsack():
    n = int(input("Ingrese la cantidad de articulos: "))
    articulos = []

    for i in range(n):
        print(f"\nArticulo {i + 1}")
        precio = float(input("Precio: "))
        peso = float(input("Peso disponible: "))

        articulos.append({
            "nombre": f"Articulo {i + 1}",
            "precio": precio,
            "peso": peso
        })

    capacidad = float(input("\nCapacidad maxima de la bolsa: "))

    solucion, valor_total = knapsack_fraccionado_diccionarios(articulos, capacidad)

    print("\nResultado usando ordenamiento por valor por unidad")

    for item in solucion:
        print(
            f"{item['nombre']}: tomar {item['cantidad']} unidad(es), "
            f"valor obtenido = ${item['valor']:.2f}"
        )

    print(f"Valor total obtenido: ${valor_total:.2f}")


def obtener_posiciones_validas(teclado):
    posiciones = {}

    for fila in range(len(teclado)):
        for columna in range(len(teclado[fila])):
            tecla = teclado[fila][columna]

            if tecla != "*" and tecla != "#":
                posiciones[tecla] = (fila, columna)

    return posiciones


def contar_combinaciones_nokia_matriz(n):
    teclado = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["*", "0", "#"]
    ]

    movimientos = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (0, 0)
    ]

    dp = {}

    for digito in "0123456789":
        dp[digito] = 1

    for _ in range(2, n + 1):
        nuevo = {}

        for fila in range(len(teclado)):
            for columna in range(len(teclado[fila])):
                tecla_actual = teclado[fila][columna]

                if tecla_actual == "*" or tecla_actual == "#":
                    continue

                total = 0

                for df, dc in movimientos:
                    nueva_fila = fila + df
                    nueva_columna = columna + dc

                    if 0 <= nueva_fila < len(teclado):
                        if 0 <= nueva_columna < len(teclado[nueva_fila]):
                            tecla_vecina = teclado[nueva_fila][nueva_columna]

                            if tecla_vecina != "*" and tecla_vecina != "#":
                                total += dp[tecla_vecina]

                nuevo[tecla_actual] = total

        dp = nuevo

    total_general = sum(dp.values())
    return total_general, dp


def mostrar_nokia():
    n = int(input("Ingrese la cantidad de digitos: "))

    total, dp = contar_combinaciones_nokia_matriz(n)

    print("\nResultado usando matriz del teclado")
    print(f"Cantidad de digitos: {n}")

    for digito in sorted(dp.keys()):
        print(f"f({n}, {digito}) = {dp[digito]}")

    print(f"Total de combinaciones: {total}")


def mostrar_menu():
    print("\n" + "=" * 45)
    print("MENU PRINCIPAL - VERSION ALTERNATIVA")
    print("=" * 45)
    print("1. Hacer sencillo con programacion dinamica")
    print("2. Knapsack fraccionado con diccionarios")
    print("3. Combinaciones Nokia usando matriz")
    print("4. Salir")
    print("=" * 45)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_cambio_monedas()
        elif opcion == "2":
            mostrar_knapsack()
        elif opcion == "3":
            mostrar_nokia()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()