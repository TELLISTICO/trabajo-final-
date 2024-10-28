import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calcular_trajectory(v0, angle, g=9.81):
    angle_rad = np.radians(angle)
    t_flight = (2 * v0 * np.sin(angle_rad)) / g
    t = np.linspace(0, t_flight, num=500)
    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - (0.5 * g * t**2)
    return x, y

# Título de la app
st.title("Simulador de Trayectoria de un Proyectil")

# Parámetros del usuario
v0 = st.number_input("Ingrese la velocidad inicial (m/s)", min_value=0.0, value=10.0)
angle = st.number_input("Ingrese el ángulo de tiro (grados)", min_value=0.0, max_value=90.0, value=45.0)

# Calcular la trayectoria
x, y = calcular_trajectory(v0, angle)

# Mostrar el gráfico
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Distancia (m)")
ax.set_ylabel("Altura (m)")
ax.set_title("Trayectoria del Proyectil")
ax.grid()
st.pyplot(fig)

# Distancia máxima
distancia_maxima = x[-1]
st.write(f"La distancia máxima alcanzada es: {distancia_maxima:.2f} m")

