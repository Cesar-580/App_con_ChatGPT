import streamlit as st

# Título y autor de la app
st.title("Mi primera app")
st.write("Esta app fue elaborada por “Cesar Augusto Ospina Muñoz”.")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Verificar si se ingresó un nombre
if nombre_usuario:
    # Mostrar el mensaje de bienvenida
    mensaje_bienvenida = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje_bienvenida)
