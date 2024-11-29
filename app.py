import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


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



# Título en la barra lateral
    st.sidebar.header('Explore as seguintes opções')

# Imagen en la barra lateral
HORIZONTAL_RED = "assets/camiseta_sada.png"
ICON_RED = "assets/logo_sada.png"
HORIZONTAL_BLUE = "assets/logo_sada.png"
ICON_BLUE = "assets/logo_sada.png"

# Asignar las imágenes que deseas usar para el sidebar y el cuerpo principal
sidebar_logo = HORIZONTAL_RED  # Por ejemplo, imagen estática para el sidebar
main_body_logo = ICON_BLUE  # Por ejemplo, imagen estática para el cuerpo principal

# Mostrar el logo en el sidebar
#st.sidebar.image(sidebar_logo, use_container_width=True)
st.sidebar.image(sidebar_logo, use_container_width=False, width=100)

# Mostrar el logo en el cuerpo principal
st.image(main_body_logo, use_container_width=False, width=100)



if __name__ == "__main__":
    main()