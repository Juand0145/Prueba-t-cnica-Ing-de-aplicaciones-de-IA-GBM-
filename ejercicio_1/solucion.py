def es_palindromo(cadena):
    """
    Funcion que acepta un string y verifica si es palindromo:
    Args:
        cadena: str de la palabra que se desea evaluar
    Return:
        True si la cadena e sun palindromo false si no
    """
    return cadena == cadena[::-1]
