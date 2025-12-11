def obtener_fracciones(frac_str):
    if isinstance(frac_str, int) or isinstance(frac_str, float):
        return frac_str

    if "/" in frac_str:
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
    else:
        return float(frac_str)


"""def suma(a, b):
    sumando_a = obtener_fracciones(a)
    sumando_b = obtener_fracciones(b)
    return sumando_a + sumando_b"""

# esta funcion realiza la operacion de suma
# x toma cualquier valor y lo convierte a float
# y toma cualquier valor y lo convierte a float


def suma(x, y):
    # esta funcion realiza la operacion de suma
    # x toma cualquier valor y lo convierte a float
    # y toma cualquier valor y lo convierte a float

    try:
        try:
            if len(x.split("/")) > 0:
                x = float(x.split("/")[0]) / float(x.split("/")[1])

            if len(y.split("/")) > 0:
                y = float(y.split("/")[0]) / float(y.split("/")[1])

        except:
            x = float(x)
            y = float(y)

        return x + y

    except:
        print("No se puede realizar la operacion :(")


def resta(a, b):
    minuendo = obtener_fracciones(a)
    sustraendo = obtener_fracciones(b)
    return minuendo - sustraendo


def multiplica(a, b):
    multiplicando = obtener_fracciones(a)
    multiplicador = obtener_fracciones(b)
    return multiplicando * multiplicador


def divide(a, b):
    dividendo = obtener_fracciones(a)
    divisor = obtener_fracciones(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division entre cero"
