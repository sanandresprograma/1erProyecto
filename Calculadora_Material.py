# importando el módulo para los decimales
from decimal import Decimal

# solicitando datos
ancho = Decimal(input('Ingrese el ancho de la superficie en mt: '))
largo = Decimal(input('Ingrese el largo de la superficie en mt: '))
anchoMaterial = Decimal(input('Ingrese el ancho del material que desea adquirir: '))
precioMaterial = Decimal(input('Ahora ingrese el costo del material: '))

# operación para calcular metro cuadrado
metroCuadrado = (ancho*largo)/anchoMaterial
costoTotal = (precioMaterial*metroCuadrado)
metroCuadrado = str(metroCuadrado)
costoTotal = str(costoTotal)

# mostrar resultado
print ('El total del material que necesita es de: ' + metroCuadrado + ' mt cuadrados y cuesta: $' + costoTotal)
