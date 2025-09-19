class Triangulo:
    """
    Representa un triángulo con tres lados y permite calcular su área.

    Atributos:
        a (float): Longitud del primer lado.
        b (float): Longitud del segundo lado.
        c (float): Longitud del tercer lado.
    """

    def __init__(self, a, b, c):
        """
        Inicializa un triángulo con tres lados.

        Parámetros:
            a (float): Longitud del primer lado.
            b (float): Longitud del segundo lado.
            c (float): Longitud del tercer lado.
        """
        self.a = a
        self.b = b
        self.c = c
