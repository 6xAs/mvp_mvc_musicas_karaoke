import streamlit as st
import pandas as pd
# Esta é a model - responsável por manipular os dados

def main():
    df_musicas = pd.read_csv("./data/lista_musica_para_karaoke_id_genero.csv", sep=",")
    # Definir colunas para exibir
    colunas_exibir = ["musica","artista", "genero", "numero"]
    df_musicas = df_musicas[colunas_exibir]
    st.dataframe(df_musicas)