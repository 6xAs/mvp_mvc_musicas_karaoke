import streamlit as st
from models.df_karaoke import main as df_karaoke_main

# Esta é a controller - responsável por intermediar a view e a model

def main():
    #st.title("Karaoke Music List - (Teste Teste 😎)")
    df_karaoke_main()

def buscar_musicas():
    # Função para buscar músicas - lógica de busca pode ser implementada aqui
    st.text_input("Buscar Músicas", "")
    st.button("Buscar", on_click=buscar_musicas)
    
    