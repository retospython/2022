
def calcularCosto(alto, ancho, profundo):
    volumenPaquete = alto*ancho*profundo
    costoEnvio = volumenPaquete * 5
    if alto > 30:
        costoEnvio = costoEnvio + 2000
    if costoEnvio> 10000:
        costoEnvio = costoEnvio * 1.19
    return costoEnvio

def costoTotal(numeroPaquetes, descuento):
    volumenPaquete = 0
    costoEnvio = 0
    costoTotal = 0
    for i in range(numeroPaquetes):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())
        costoEnvio = calcularCosto(alto, ancho, profundo)
        costoTotal = costoTotal + costoEnvio
    return costoTotal - (costoTotal*(descuento/100))
