import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu


#Personalizando el nombre de lengueta
img = Image.open('assets/bola.ico')
st.set_page_config('Betovoley', page_icon=img, layout='wide', initial_sidebar_state='auto')

def main():
    st.title("Bem-vindo a Betovoley-Sada Cruzeiro Stats")

# Header con color verde HEX #116F4B
    st.markdown(
    """
    <h1 style="color: #116F4B;">Site dedicado ao trabalho estatístico e de análise do clube SADA CRUZEIRO VOLEI</h1>
    """, 
    unsafe_allow_html=True
)
    
# Texto enmarcao
    st.markdown("""
<div style="border: 1px solid black; padding: 10px; border-radius: 5px;">
    <p style="font-size: 24px;">Neste site você encontrará estatísticas básicas de desempenho para todos os fundamentos da nossa equipe, por jogador e por torneio.
Você também encontrará estatísticas avançadas com métricas criadas internamente para avaliar o desempenho coletivo e individual.</p>
</div>
""", unsafe_allow_html=True)

# Colores personalizados de tu paleta
SIDEBAR_COLOR = "#116F4B"  # Verde oscuro para el fondo del sidebar
CONTAINER_COLOR = "#116F4B"  # Igual que el fondo del sidebar
TEXT_COLOR = "#F5F9F8"  # Blanco para texto e iconos
MENU_SELECTED_COLOR = "#194D9D"  # Azul intermedio para la opción seleccionada
HOVER_COLOR = "#3F69AD"  # Azul claro para el hover

# CSS para personalizar el fondo del sidebar
st.markdown(
    f"""
    <style>
        [data-testid="stSidebar"] {{
            background-color: {SIDEBAR_COLOR};
            color: {TEXT_COLOR};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar con opción de menú
with st.sidebar:
    selected = option_menu(
        menu_title="Explore as seguintes opções",  # Título del menú
        options=[
            "Análisis por equipo básico",
            "Análisis por equipo avanzado (em breve)",
            "Análisis por jugador básico (em breve)",
            "Análisis por jugador avanzado (em breve)",
        ],  # Opciones
        icons=["rocket-takeoff", "rocket-takeoff-fill", "train-freight-front", "train-freight-front-fill"],  # Iconos válidos de Bootstrap
        menu_icon="trophy-fill",  # Icono principal del menú
        default_index=0,  # Opción seleccionada por defecto
        styles={
            "container": {"padding": "5px", "background-color": "#ffffff"},  # Fondo blanco
            "icon": {"color": "#194D9D", "font-size": "18px"},  # Iconos azul
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": "#000000",  # Texto en negro para opciones no seleccionadas
                "--hover-color": "#f0f0f0",  # Color al pasar el mouse (gris claro)
            },
            "nav-link-selected": {
                "background-color": "#3F69AD",  # Fondo azul para la opción seleccionada
                "color": "white",  # Texto en blanco para la opción seleccionada
            },
            "menu-title": {
                "font-size": "18px",
                "color": "#194D9D",  # Título del menú en azul
            },
        },
)

# Cuerpo principal
# Agregar el logo
st.image("assets/logo_sada.png", width=200)  # Reemplaza "logo.png" con la ruta o URL de tu logo
#st.title("Bem-vindo ao site de análise de voleibol!")

# Contenido dinámico según la selección
if selected == "Análisis por equipo básico":
    st.title(f"Bem-vindo a {selected} site")
elif selected == "Análisis por equipo avanzado (em breve)":
    st.title(f"Bem-vindo a {selected} site")
elif selected == "Análisis por jugador básico (em breve)":
    st.title(f"Bem-vindo a {selected} site")
elif selected == "Análisis por jugador avanzado (em breve)":
    st.title(f"Bem-vindo a {selected} site")
    

# Título del sidebar
#    st.sidebar.header('Explore as seguintes opções')


# Imagen en la barra lateral
HORIZONTAL_RED = "assets/camiseta_sada.png"
ICON_RED = "assets/logo_sada.png"
HORIZONTAL_BLUE = "assets/logo_sada.png"
ICON_BLUE = "assets/logo_sada.png"

# Asignar las imágenes que deseas usar para el sidebar y el cuerpo principal
#sidebar_logo = HORIZONTAL_RED  # Por ejemplo, imagen estática para el sidebar
# main_body_logo = ICON_BLUE  # Por ejemplo, imagen estática para el cuerpo principal

# Mostrar el logo en el sidebar
#st.sidebar.image(sidebar_logo, use_container_width=True)
#st.sidebar.image(sidebar_logo, use_container_width=False, width=100)

# Mostrar el logo en el cuerpo principal
# st.image(main_body_logo, use_container_width=False, width=100)


# Footer
st.markdown(
    """
    <footer style="background-color: #2C3E3F; color: white; padding: 10px; text-align: center; position: fixed; left: 0; bottom: 0; width: 100%; font-size: 14px;">
        © 2024 Sada Cruzeiro Vôlei. Todos os direitos reservados.
        Site criado por Betovoley
        <br>
        <a href="https://www.sadacruzeiro.com.br" target="_blank" style="color: white;">Visite nosso site</a>
    </footer>
    """, 
    unsafe_allow_html=True
)



if __name__ == "__main__":
    main()