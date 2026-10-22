import streamlit as st
precioAlfajores=1000
st.title("Kiosko The Killing")
st.write("Prome 3x2!!!")

cantidad=st.number_input("Cantidad de alfajores", min_value=0, step=1)
total=cantidad*precioAlfajores
div=total/3
if cantidad>=3:
    ahorro=total-precioAlfajores*(cantidad//3)
    total-=ahorro
    st.write(f"ahorraste ${total}")
    st.write(f"tu total a pagar es ${ahorro}")
else:
    st.write(f"total a pagar: ${total}")