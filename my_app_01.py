import streamlit as st

st.title("Mi primera aplicación")

st.write("Bienvenido a mi aplicación web my_app_01")

nombre = st.text_input("Escribe tu nombre:")

if nombre:
    st.success(f"¡Hola {nombre}! Bienvenido.")
