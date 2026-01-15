def add(a: float, b: float) -> float:
    return a + b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
