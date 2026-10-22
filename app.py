import streamlit as st
from calculos import EFECTIVO, TRANSFERENCIA, buscar_posicion, a

st.title("Kiosko The Killing")

productos=["Alfajor", "Gaseosa", "Chcle", "Agua"]
precios=[1500, 2400, 500, 300]

productos_seleccionados =st.selectbox("Seleccione un producto: ")
cantidad=st.number_input("Cantidad: ", min_value=1, step=1)
forma_pago=st.radio("Forma de pago: ", [EFECTIVO, TRANSFERENCIA])

pos=buscar_posicion(productos,productos_seleccionados)
precio_unitario=precios[pos]

subtotal=precio_unitario*cantidad
monto_con_descuento= aplicar_descuento(subtotal, forma_pago)
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