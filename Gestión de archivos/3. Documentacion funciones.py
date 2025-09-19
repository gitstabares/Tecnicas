def calcular_area_triangulo(a, b, c):
    """
    Calcula el área de un triángulo dados sus tres lados utilizando la fórmula de Herón.

    Parámetros:
        a (float): Longitud del primer lado.
        b (float): Longitud del segundo lado.
        c (float): Longitud del tercer lado.

    Retorna:
        float: Área del triángulo.
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


resultado = calcular_area_triangulo(3, 4, 5)
