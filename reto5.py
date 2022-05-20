def calcularCosto(alto, ancho, profundo):
  volumen = alto*ancho*profundo
  costo = volumen * 5
  if alto > 30:
    costo += 2000
  if costo > 10000:
    costo *= 1.19
  return costo

def costoTotal(listaPaquetes, descuento):
  total = 0
  for paquete in listaPaquetes:
    alto = paquete['ALTO']
    ancho = paquete['ANCHO']
    profundo = paquete['PROFUNDO']
    total += calcularCosto(alto, ancho, profundo)
  return total*(1-descuento/100)
