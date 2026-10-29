 

def solicitar_entero(mensaje, minimo, maximo=None):

    """Pide un entero válido sin terminar el programa ante errores."""

    while True:

        texto = input(mensaje).strip()

        if not (texto.isascii() and texto.isdigit()):

            print("Error: escribe únicamente números enteros, sin letras ni signos.")

            continue

        numero = int(texto)

        if numero < minimo or (maximo is not None and numero > maximo):

            if maximo is None:

                print(f"Error: escribe un número entero mayor o igual que {minimo}.")

            else:

                print(f"Error: el número debe estar entre {minimo} y {maximo}.")

            continue

        return numero

 

 

def solicitar_nombre():

    """Repite la captura hasta recibir un nombre válido de alimento."""

    signos_permitidos = "(),.-/"

    while True:

        nombre = " ".join(input("Nombre del producto: ").split())

        letras = sum(caracter.isalpha() for caracter in nombre)

        valido = (nombre and nombre[0].isalpha() and letras >= 2

                  and all(c.isalpha() or c.isspace() or c in signos_permitidos

                          for c in nombre))

        if valido:

            return nombre

        print("Error: ingresa un nombre válido de al menos dos letras y sin números.")

 

 

def contar_letras(nombre):

    """Cuenta letras; no considera espacios, números ni signos."""

    return sum(caracter.isalpha() for caracter in nombre)

 

 

def ordenar_caducidad_burbuja(productos):

    """Burbuja ascendente: intercambia productos vecinos si están invertidos."""

    ordenados = productos.copy()

    n = len(ordenados)

    for pasada in range(n - 1):

        hubo_cambios = False

        for j in range(n - 1 - pasada):

            if ordenados[j]["dias"] > ordenados[j + 1]["dias"]:

                ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]

                hubo_cambios = True

        if not hubo_cambios:

            break

    return ordenados

 

 

def ordenar_nombres_burbuja(productos):

    """Burbuja descendente por letras; empates en orden alfabético."""

    ordenados = productos.copy()

    n = len(ordenados)

    for pasada in range(n - 1):

        hubo_cambios = False

        for j in range(n - 1 - pasada):

            actual = ordenados[j]

            siguiente = ordenados[j + 1]

            letras_actual = contar_letras(actual["nombre"])

            letras_siguiente = contar_letras(siguiente["nombre"])

            # Si el de la izquierda tiene menos letras, intercambiar.

            # Con iguales cantidades, ordenar alfabéticamente.

            intercambiar = (letras_actual < letras_siguiente or

                           (letras_actual == letras_siguiente and

                            actual["nombre"].casefold() >

                            siguiente["nombre"].casefold()))

            if intercambiar:

                ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]

                hubo_cambios = True

        if not hubo_cambios:

            break

    return ordenados

 

 

def registrar_productos():

    cantidad = solicitar_entero("¿Cuántos productos deseas registrar? ", 1)

    productos = []

    for numero in range(1, cantidad + 1):

        print(f"\nProducto {numero} de {cantidad}")

        nombre = solicitar_nombre()

        dias = solicitar_entero("Días para caducar (1 a 365): ", 1, 365)

        productos.append({"nombre": nombre, "dias": dias})

    return productos

 

 

def mostrar_resultados(productos):

    por_caducidad = ordenar_caducidad_burbuja(productos)

    print("\nPLAN DE ENVÍO PRIORITARIO (BURBUJA: MENOS DÍAS PRIMERO)")

    print("-" * 60)

    for posicion, producto in enumerate(por_caducidad, 1):

        print(f"{posicion:2}) {producto['nombre']} - {producto['dias']} días")

 

    por_letras = ordenar_nombres_burbuja(productos)

    print("\nNOMBRES (BURBUJA: MÁS LETRAS PRIMERO)")

    print("-" * 60)

    for posicion, producto in enumerate(por_letras, 1):

        print(f"{posicion:2}) {producto['nombre']} - "

              f"{contar_letras(producto['nombre'])} letras")

    return por_caducidad, por_letras

 

 

def main():

    print("SISTEMA DE CONTROL DE ENVÍO DE ALIMENTOS")

    productos = registrar_productos()

    mostrar_resultados(productos)

 

 

if __name__ == "__main__":

    