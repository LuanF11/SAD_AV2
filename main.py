import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Título do aplicativo
st.title("Detecção de Bordas de Imagem")

# Carregador de arquivos
arquivo_carregado = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if arquivo_carregado is not None:
    # Converte o arquivo para uma imagem OpenCV
    imagem = Image.open(arquivo_carregado)
    imagem = np.array(imagem)
    
    # Exibe a imagem original
    st.image(imagem, caption='Imagem Carregada', use_container_width=True)
    
    # Converte para escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Usa a detecção de bordas de Canny
    bordas = cv2.Canny(cinza, 100, 200)
    
    # Exibe a imagem processada
    st.image(bordas, caption='Bordas Detectadas', use_container_width=True)