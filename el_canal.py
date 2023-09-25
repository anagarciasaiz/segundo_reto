# Función para determinar si es posible que todos los suscriptores hayan leído la publicación
def comprobar_suscriptores(n, a, q, notificaciones):
    # Si al principio no hay suscriptores en línea o si todos están en línea, se garantiza que todos leyeron
    if a == 0 or a == n:
        return "YES"
    
    # Si hay notificaciones para cada suscriptor en línea, se garantiza que todos leyeron
    if a <= q <= n - a:
        return "YES"
    
    # Si quedan notificaciones, pero no se garantiza que todos hayan leído, entonces "MAYBE"
    if q > n - a:
        return "MAYBE"
    
    # En otros casos, es imposible que todos hayan leído
    return "NO"

# Leer el número de casos de prueba
t = int(input())

# Procesar cada caso de prueba
for _ in range(t):
    n, a, q = map(int, input().split())
    notificaciones = input()
    result = comprobar_suscriptores(n, a, q, notificaciones)
    print(result)









