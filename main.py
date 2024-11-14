import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para", ["Home", "Processamento de Imagem"])

if pagina == "Home":
    st.title("Detecção de Bordas de Imagem")

    # Carregador de arquivos
    arquivo_carregado = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

    if arquivo_carregado is not None:
        # Converte o arquivo para uma imagem OpenCV
        imagem = Image.open(arquivo_carregado)
        imagem = np.array(imagem)
        
        # Exibe a imagem 
        st.image(imagem, caption='Imagem Carregada')

else:
    st.title("Processamento de Imagem")

    # Carregador de arquivos
    arquivo_carregado = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

    if arquivo_carregado is not None:
        # Converte o arquivo para uma imagem OpenCV
        imagem = Image.open(arquivo_carregado)
        imagem = np.array(imagem)
        
        # Exibe a imagem 
        st.image(imagem, caption='Imagem Carregada')
        
        # Converte para escala de cinza
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        
        # Sliders para ajustar os parâmetros de detecção de bordas de Canny
        limiar_inferior = st.slider("Limiar Inferior", 0, 255, 100)
        limiar_superior = st.slider("Limiar Superior", 0, 255, 200)
        
        # Usa a detecção de bordas de Canny com parâmetros ajustáveis
        bordas = cv2.Canny(cinza, limiar_inferior, limiar_superior)
        
        # Exibe a imagem processada
        st.image(bordas, caption='Bordas Detectadas')
        
        # Opções de processamento de imagem
        if st.checkbox("Aplicar Desfoque"):
            tipo_desfoque = st.selectbox("Tipo de Desfoque", ["Gaussian", "Median", "Bilateral"])
            if tipo_desfoque == "Gaussian":
                bordas = cv2.GaussianBlur(bordas, (5, 5), 0)
            elif tipo_desfoque == "Median":
                bordas = cv2.medianBlur(bordas, 5)
            elif tipo_desfoque == "Bilateral":
                bordas = cv2.bilateralFilter(bordas, 9, 75, 75)
            st.image(bordas, caption='Imagem com Desfoque')
        
        if st.checkbox("Aplicar Equalização de Histograma"):
            bordas = cv2.equalizeHist(bordas)
            st.image(bordas, caption='Imagem com Equalização de Histograma')
        
        if st.checkbox("Aplicar Nitidez"):
            kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
            bordas = cv2.filter2D(bordas, -1, kernel)
            st.image(bordas, caption='Imagem com Nitidez')
        
        # Baixar a imagem processada
        if st.button("Baixar Imagem Processada"):
            imagem_bordas = Image.fromarray(bordas)
            imagem_bordas.save("bordas_detectadas.png")
            st.success("Imagem salva como bordas_detectadas.png")