import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task


import sympy as sp
from functools import lru_cache
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

_TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor,
)

@lru_cache(maxsize=256)
def _parse_expression_cached(expr_str: str, variable_names: tuple) -> sp.Expr:
    if not isinstance(expr_str, str):
        raise ValueError("L'espressione deve essere una stringa.")

    expr_norm = expr_str.replace("^", "**")
    local_dict = {name: sp.Symbol(name) for name in variable_names}

    try:
        expr = parse_expr(
            expr_norm,
            local_dict=local_dict,
            transformations=_TRANSFORMATIONS,
            evaluate=True
        )
        return sp.simplify(expr)

    except Exception as exc:
        raise ValueError(f"Errore parsing: {exc}")

def calcola_derivata(espressione: str, variabile: str) -> sp.Expr:
    if not isinstance(variabile, str) or not variabile:
        raise ValueError("Variabile non valida.")

    var_symbol = sp.Symbol(variabile)
    expr = _parse_expression_cached(espressione, (variabile,))
    derivata = sp.diff(expr, var_symbol)

    return sp.simplify(derivata)

def main():
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")
    risultato = calcola_derivata(espressione, variabile)
    print("Derivata:", risultato)

if __name__ == "__main__":
    main()
pass

import sympy as sp
from functools import lru_cache
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

_TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor,
)

@lru_cache(maxsize=256)
def _parse_expression_cached(expr_str: str, variable_names: tuple) -> sp.Expr:
    if not isinstance(expr_str, str):
        raise ValueError("L'espressione deve essere una stringa.")

    expr_norm = expr_str.replace("^", "**")
    local_dict = {name: sp.Symbol(name) for name in variable_names}

    try:
        expr = parse_expr(
            expr_norm,
            local_dict=local_dict,
            transformations=_TRANSFORMATIONS,
            evaluate=True
        )
        return sp.simplify(expr)

    except Exception as exc:
        raise ValueError(f"Errore parsing: {exc}")
def calcola_integrale_definito(espressione: str, variabile: str, a: float, b: float) -> sp.Expr:
    if not isinstance(variabile, str) or not variabile:
        raise ValueError("Variabile non valida.")

    var_symbol = sp.Symbol(variabile)
    expr = _parse_expression_cached(espressione, (variabile,))

    try:
        integrale = sp.integrate(expr, (var_symbol, a, b))
    except Exception as exc:
        raise ValueError(f"Errore nel calcolo dell'integrale: {exc}")

    return sp.simplify(integrale)

def main():
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")
    a = float(input("Inserisci estremo inferiore: "))
    b = float(input("Inserisci estremo superiore: "))

    risultato = calcola_integrale_definito(espressione, variabile, a, b)
    print("Integrale definito:", risultato)

if __name__ == "__main__":
    main()
    pass

def calcola_limite(espressione: str, variabile: str, punto: float) -> sp.Expr:
    if not isinstance(variabile, str) or not variabile:
        raise ValueError("Variabile non valida.")

    var_symbol = sp.Symbol(variabile)
    expr = _parse_expression_cached(espressione, (variabile,))

    try:
        limite = sp.limit(expr, var_symbol, punto)
    except Exception as exc:
        raise ValueError(f"Errore nel calcolo del limite: {exc}")

    return sp.simplify(limite)

def main():
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")
    punto = float(input("Inserisci il punto: "))

    risultato = calcola_limite(espressione, variabile, punto)
    print("Limite:", risultato)

if __name__ == "__main__":
    main()



    pass

def calcola_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sp.Expr:
    if not isinstance(variabile, str) or not variabile:
        raise ValueError("Variabile non valida.")

    var_symbol = sp.Symbol(variabile)
    expr = _parse_expression_cached(espressione, (variabile,))

    try:
        serie = sp.series(expr, var_symbol, punto, ordine + 1).removeO()
    except Exception as exc:
        raise ValueError(f"Errore nel calcolo del polinomio di Taylor: {exc}")

    return sp.simplify(serie)

def main():
    espressione = input("Inserisci l'espressione: ")
    variabile = input("Inserisci la variabile: ")
    punto = float(input("Inserisci il punto di sviluppo: "))
    ordine = int(input("Inserisci l'ordine del polinomio: "))

    risultato = calcola_taylor(espressione, variabile, punto, ordine)
    print("Polinomio di Taylor:", risultato)

if __name__ == "__main__":
    main()

    pass


    def calcola_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sp.Expr:
        if not isinstance(variabile, str) or not variabile:
            raise ValueError("Variabile non valida.")

        var_symbol = sp.Symbol(variabile)
        expr = _parse_expression_cached(espressione, (variabile,))

        try:
            serie = sp.series(expr, var_symbol, punto, ordine + 1).removeO()
        except Exception as exc:
            raise ValueError(f"Errore nel calcolo del polinomio di Taylor: {exc}")

        return sp.simplify(serie)


    def main():
        espressione = input("Inserisci l'espressione: ")
        variabile = input("Inserisci la variabile: ")
        punto = float(input("Inserisci il punto di sviluppo: "))
        ordine = int(input("Inserisci l'ordine del polinomio: "))

        risultato = calcola_taylor(espressione, variabile, punto, ordine)
        print("Polinomio di Taylor:", risultato)


    if __name__ == "__main__":
        main()

    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
