def calcular_distancia(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def generar_id():
    import uuid
    return str(uuid.uuid4())