
import streamlit as st

from fpdf import FPDF


def armar_pdf(cliente, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica","B",20)
    pdf.cell(0, 12, "kiosco The Killing", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica","",12)
    pdf.cell(0,9,f"cliente: {cliente}",new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0,9,f"cliente: ${total:.2f}",new_x="LMARGIN", new_y="NEXT")
    return bytes (pdf.output())
EFECTIVO = "Efectivo"

TRANSFERENCIA = "Transferencia"


def buscar_posicion(lista, nombre):
    """Busca la posicion de un elemento en una lista."""
    for i in range(len(lista)):
        if lista[i] == nombre:
            return i
    return -1


def aplicar_descuento(monto, pago):
    """Aplica un 10% de descuento si el pago es en efectivo."""
    if pago == EFECTIVO:
        monto = monto - (monto * 10 / 100)
    return round(monto, 2)


def calcular_iva(monto):
    """Calcula el 21% de IVA sobre un monto."""
    return round(monto * 21 / 100, 2)

st.title("Kiosko The Killing")

productos=["Alfajor", "Gaseosa", "Chcle", "Agua"]
precios=[1500, 2400, 500, 300]

productos_seleccionados =st.selectbox("Seleccione un producto: ", productos)
cantidad=st.number_input("Cantidad: ", min_value=1, step=1)
forma_pago=st.radio("Forma de pago: ", [EFECTIVO, TRANSFERENCIA])

pos=buscar_posicion(productos,productos_seleccionados)
precio_unitario=precios[pos]

subtotal=precio_unitario*cantidad
monto_con_descuento=aplicar_descuento(subtotal, forma_pago)
descuento_monto= subtotal-monto_con_descuento

iva=calcular_iva(monto_con_descuento)
total=round(monto_con_descuento+iva, 2)

st.markdown("---")
st.subheader("Resumen de compra")
st.write(f"Precio unitario: ${precio_unitario}")
st.write(f"Subtotal: ${subtotal}")

if descuento_monto > 0:
    st.write(f"Descuento (10% en efectivo): ${descuento_monto}")
    st.write(f"Monto con descuento: ${monto_con_descuento}")

st.wite(f"IVA (21%): ${iva}")
st.markdown(f"Total a pagar: ${total}")