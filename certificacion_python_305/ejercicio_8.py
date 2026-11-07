def calcular_venta_neta(producto1, producto2, producto3):
    return producto1 + producto2 + producto3
def calcular_iva(venta_neta):
    return venta_neta * 0.16
def mostrar_compra_total(venta_neta, iva_generado):
    total = venta_neta + iva_generado
    print(f"la venta neta es {venta_neta}")
    print(f"el iva generado es {iva_generado}")
    print(f"la compra total es {total}")
producto1 = 150
producto2 = 200
producto3 = 50
venta_neta = calcular_venta_neta(producto1, producto2, producto3)
iva_generado = calcular_iva(venta_neta)
mostrar_compra_total(venta_neta, iva_generado)