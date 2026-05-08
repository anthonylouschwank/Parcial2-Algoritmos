# Pseudocódigo y explicación de los tres ejercicios

## Ejercicio 1: Hacer sencillo con Programación Dinámica

### Pseudocódigo

```text
HACER-SENCILLO-DP(m):
  // m representa el monto en centavos
  monedas <- [1, 5, 10, 25]

  crear arreglo dp[0...m]
  crear arreglo ultima_moneda[0...m]

  PARA i DESDE 0 HASTA m HACER
    dp[i] <- infinito
    ultima_moneda[i] <- -1
  FIN PARA

  dp[0] <- 0

  PARA cantidad DESDE 1 HASTA m HACER
    PARA CADA moneda EN monedas HACER
      SI cantidad >= moneda ENTONCES
        candidato <- dp[cantidad - moneda] + 1

        SI candidato < dp[cantidad] ENTONCES
          dp[cantidad] <- candidato
          ultima_moneda[cantidad] <- moneda
        FIN SI
      FIN SI
    FIN PARA
  FIN PARA

  resultado <- {1: 0, 5: 0, 10: 0, 25: 0}
  actual <- m

  MIENTRAS actual > 0 HACER
    moneda <- ultima_moneda[actual]
    resultado[moneda] <- resultado[moneda] + 1
    actual <- actual - moneda
  FIN MIENTRAS

  RETORNAR resultado, dp[m]
```

```text
candidato = dp[cantidad - moneda] + 1
```

Esto significa que si ya conozco la mejor forma de formar `cantidad - moneda`, entonces puedo formar `cantidad` agregando una moneda más.

Además, el arreglo `ultima_moneda` guarda cuál fue la moneda que permitió obtener la mejor solución para cada monto. Al final, el algoritmo reconstruye la respuesta empezando desde `m` y restando la última moneda usada hasta llegar a 0.

### Complejidad

Sea `m` el monto a formar y `k` la cantidad de denominaciones disponibles.

```text
Complejidad temporal: O(m x k)
```

Como las denominaciones son fijas `{1, 5, 10, 25}`, entonces `k = 4`, por lo que:

```text
Complejidad temporal: O(m)
```

El algoritmo usa dos arreglos de tamaño `m + 1`, por lo tanto:

```text
Complejidad espacial: O(m)
```

### Explicación general

Este enfoque es distinto al greedy porque no elige directamente la moneda más grande. En lugar de eso, compara todas las posibilidades y construye la mejor solución usando respuestas previamente calculadas.

La idea principal es que la solución óptima para un monto depende de soluciones óptimas para montos menores. Por eso, este problema puede resolverse con programación dinámica.

---

## Ejercicio 2: Knapsack fraccionado por selección iterativa

```text
KNAPSACK-FRACCIONADO-SELECCION(articulos, W):
  // articulos[i] = (precio pᵢ, peso disponible wᵢ)
  // W es la capacidad máxima de la bolsa

  n <- cantidad de articulos
  usado[1...n] <- falso

  capacidad_restante <- W
  valor_total <- 0
  solucion <- []

  MIENTRAS capacidad_restante > 0 HACER
    mejor <- -1
    mejor_razon <- -1

    PARA i DESDE 1 HASTA n HACER
      SI usado[i] = falso Y wᵢ > 0 ENTONCES
        razon <- pᵢ / wᵢ

        SI razon > mejor_razon ENTONCES
          mejor_razon <- razon
          mejor <- i
        FIN SI
      FIN SI
    FIN PARA

    SI mejor = -1 ENTONCES
      ROMPER
    FIN SI

    tomar <- MIN(w_mejor, capacidad_restante)

    agregar (mejor, tomar) a solucion

    valor_total <- valor_total + tomar × (p_mejor / w_mejor)
    capacidad_restante <- capacidad_restante - tomar

    usado[mejor] <- verdadero
  FIN MIENTRAS

  RETORNAR solucion, valor_total
```

### Explicación de iteraciones

El algoritmo empieza con una capacidad disponible `W` y una lista vacía llamada `solucion`.

En cada iteración, busca el artículo que todavía no ha sido usado y que tenga la mejor razón:

```text
razon = precio / peso
```

Esta razón representa cuánto valor se obtiene por cada unidad de peso. Por eso, el artículo con mayor razón es el más conveniente en ese momento.

Cuando encuentra el mejor artículo, el algoritmo decide cuánto tomar:

```text
tomar = MIN(peso_del_articulo, capacidad_restante)
```

Si el artículo completo cabe en la bolsa, se toma completo. Si no cabe completo, se toma solamente la parte que cabe. Después se actualiza el valor total y se reduce la capacidad restante.

El proceso se repite hasta que la bolsa se llena o hasta que ya no quedan artículos disponibles.

### Complejidad

En cada iteración se recorre la lista completa de artículos para buscar el mejor disponible. En el peor caso, se puede hacer esto una vez por cada artículo.

```text
Complejidad temporal: O(n^2)
```

También se usa un arreglo `usado` para marcar los artículos seleccionados, además de la lista de solución.

```text
Complejidad espacial: O(n)
```

### Explicación general

Este enfoque sigue siendo greedy porque en cada paso toma la decisión localmente más conveniente: elegir el artículo con mayor valor por unidad.

La diferencia con el enfoque tradicional es que aquí no se ordena toda la lista al inicio. En cambio, el algoritmo busca el mejor artículo disponible en cada iteración. Esto hace que el procedimiento sea más fácil de explicar paso a paso, aunque sea menos eficiente que ordenar una sola vez.

---

## Ejercicio 3: Combinaciones Nokia usando matriz del teclado

### Pseudocódigo

```text
NOKIA-MATRIZ(n):
  teclado <- [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [*, 0, #]
  ]

  movimientos <- [
    (-1, 0),   // arriba
    (1, 0),    // abajo
    (0, -1),   // izquierda
    (0, 1),    // derecha
    (0, 0)     // quedarse en la misma tecla
  ]

  crear tabla dp_actual

  PARA d DESDE 0 HASTA 9 HACER
    dp_actual[d] <- 1
  FIN PARA

  PARA longitud DESDE 2 HASTA n HACER
    crear tabla dp_nuevo

    PARA CADA posicion (fila, columna) EN teclado HACER
      tecla <- teclado[fila][columna]

      SI tecla ≠ * Y tecla ≠ # ENTONCES
        dp_nuevo[tecla] <- 0

        PARA CADA movimiento (df, dc) EN movimientos HACER
          nueva_fila <- fila + df
          nueva_columna <- columna + dc

          SI nueva_fila y nueva_columna están dentro del teclado ENTONCES
            tecla_vecina <- teclado[nueva_fila][nueva_columna]

            SI tecla_vecina ≠ * Y tecla_vecina ≠ # ENTONCES
              dp_nuevo[tecla] <- dp_nuevo[tecla] + dp_actual[tecla_vecina]
            FIN SI
          FIN SI
        FIN PARA
      FIN SI
    FIN PARA

    dp_actual <- dp_nuevo
  FIN PARA

  total <- 0

  PARA d DESDE 0 HASTA 9 HACER
    total <- total + dp_actual[d]
  FIN PARA

  RETORNAR total
```

### Explicación de iteraciones

El algoritmo representa el teclado Nokia como una matriz de 4 filas y 3 columnas:

```text
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[*, 0, #]
```

Las teclas `*` y `#` se ignoran porque no se pueden presionar.

Para `n = 1`, cada dígito del 0 al 9 tiene exactamente una combinación posible, porque se puede comenzar desde cualquier dígito. Por eso, inicialmente:

```text
dp_actual[d] = 1
```

Luego, para cada longitud desde `2` hasta `n`, el algoritmo calcula una nueva tabla `dp_nuevo`.

Para cada tecla válida, revisa los movimientos posibles: arriba, abajo, izquierda, derecha y quedarse en la misma tecla. Si el movimiento lleva a una tecla válida, se suma la cantidad de combinaciones que llegaban a esa tecla en la longitud anterior.

La idea central es:

```text
dp_nuevo[tecla] = suma de combinaciones anteriores de las teclas vecinas válidas
```

Después de procesar todas las teclas, `dp_actual` se actualiza con `dp_nuevo`. Al terminar, se suman todas las combinaciones que terminan en cada dígito.

### Complejidad

Para cada longitud se revisan las 10 teclas válidas y hasta 5 movimientos posibles.

```text
Complejidad temporal: O(n × 10 × 5)
```

Como 10 y 5 son constantes:

```text
Complejidad temporal: O(n)
```

Solo se guardan dos tablas de tamaño fijo, una para la longitud actual y otra para la nueva.

```text
Complejidad espacial: O(10) = O(1)
```

### Explicación general

Este algoritmo utiliza programación dinámica porque el número de combinaciones de longitud `k` depende de las combinaciones calculadas para la longitud `k - 1`.

El enfoque es distinto porque no escribe manualmente los vecinos de cada dígito. En vez de eso, usa la posición de cada tecla dentro de la matriz y calcula automáticamente los movimientos válidos.

Esto hace que el algoritmo sea más general y más fácil de adaptar si se quisiera cambiar la forma del teclado.
