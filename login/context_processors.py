def materias_context(request):
    MATERIAS = [
        {'id': 'algebra', 'nombre': 'Álgebra Lineal 📚', 'activities': [
            'Conceptos Clave y Vectores', 
            'Sistema de Ecuaciones Lineales', 
            'Matrices y Determinantes', 
            'Transformaciones Lineales'
        ]},
        {'id': 'calculo', 'nombre': 'Cálculo Avanzado 📈', 'activities': [
            'Introducción a las Derivadas',
            'Derivadas usando limites', 
            'Derivadas y Reglas', 
            'Integrales Definidas'
        ]},
        {'id': 'geometria', 'nombre': 'Geometría Analítica 📐', 'activities': [
            'Planos Cartesianos', 
            'Cónicas y Elipses'
        ]},
    ]
    return {'materias': MATERIAS}
