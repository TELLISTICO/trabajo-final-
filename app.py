# app.py
import streamlit as st
import random

st.title("Conservación de la Energía: Conversión entre Energía Potencial y Cinética")

st.write("""
Este sitio te permite practicar preguntas de conservación de la energía, enfocándose en la conversión entre energía potencial y energía cinética.
""")

# Pregunta aleatoria de conversión entre energía potencial y cinética
def generar_pregunta():
    masa = random.randint(1, 10)  # masa en kg
    altura = random.randint(1, 20)  # altura en metros
    velocidad = random.randint(1, 10)  # velocidad en m/s
    
    # Pregunta con solo energía potencial a cinética
    tipo_pregunta = random.choice(["potencial-a-cinetica", "cinetica-a-potencial"])
    
    if tipo_pregunta == "potencial-a-cinetica":
        energia_potencial = masa * 9.81 * altura
        pregunta = f"Si un objeto de {masa} kg se encuentra a una altura de {altura} m, ¿cuál será su velocidad justo antes de tocar el suelo?"
        respuesta_correcta = (2 * energia_potencial / masa) ** 0.5
    else:
        energia_cinetica = 0.5 * masa * velocidad ** 2
        pregunta = f"Si un objeto de {masa} kg se mueve a una velocidad de {velocidad} m/s, ¿a qué altura alcanzaría si toda su energía cinética se convierte en energía potencial?"
        respuesta_correcta = energia_cinetica / (masa * 9.81)

    return pregunta, round(respuesta_correcta, 2)

# Mostrar pregunta
pregunta, respuesta_correcta = generar_pregunta()
st.write(pregunta)

# Entrada del usuario
respuesta_usuario = st.number_input("Tu respuesta:", format="%.2f")
if st.button("Comprobar respuesta"):
    if abs(respuesta_usuario - respuesta_correcta) < 0.1:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta correcta era {respuesta_correcta}.")

# Generar una nueva pregunta
if st.button("Nueva pregunta"):
    st.experimental_rerun()
