
numeroPaquetes= int(input())
costoTotal=0

for i in range (1,numeroPaquetes+1):
    alto=  float(input())
    ancho= float(input())
    profundo= float(input())
    volumen= (alto*ancho*profundo)
    costo= volumen*5
    if alto>30:
        costo=costo+2000
        print(costo)
    if costo>10000:
            costo=costo+(costo*0.19)
    print(volumen)
    print(costo)
    costoTotal=costoTotal+costo
    

print(costoTotal)
