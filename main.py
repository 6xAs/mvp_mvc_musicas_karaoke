import streamlit as st

from views.musicas_karaoke import main as musicas_karaoke_view_main

# Configuração da página
st.set_page_config(
        page_title="Karaoke Music Application",
        page_icon="🎤",
        layout="wide"
    )


def main():
    # Exibir dataframe de músicas de karaokê
    st.title("Karaoke Music Application")
    musicas_karaoke_view_main()
    
if __name__ == "__main__":
    main()