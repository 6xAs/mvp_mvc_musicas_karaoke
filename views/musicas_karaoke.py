import streamlit as st
from controllers.musicaskaraokecontroller import main as musicas_karaoke_main
from controllers.musicaskaraokecontroller import buscar_musicas as musicas_karaoke_buscar_musicas

# Essa é a view - responsável por exibir a interface para o usuário
def main():
    #st.title("Karaoke Music Application - View")
    musicas_karaoke_buscar_musicas()
    musicas_karaoke_main()
