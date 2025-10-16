from pathlib import Path
import unicodedata

import pandas as pd
import streamlit as st


# Caminho para o arquivo CSV com o catálogo completo.
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "lista_musica_para_karaoke_id_genero.csv"


def _normalize_text(text: str) -> str:
    """Remove acentos e transforma o texto em minúsculo para facilitar comparações."""
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(char for char in normalized if not unicodedata.combining(char)).lower()


@st.cache_data(show_spinner=False)
def load_karaoke_data() -> pd.DataFrame:
    """
    Lê o arquivo CSV apenas uma vez e mantém o resultado em cache.

    O cache do Streamlit evita que o arquivo seja lido repetidamente a cada interação.
    """
    df = pd.read_csv(DATA_FILE, sep=",", encoding="utf-8-sig").fillna("")

    # Garantimos que todas as colunas importantes estejam em texto limpo.
    for column in ("numero", "musica", "artista", "genero"):
        df[column] = df[column].astype(str).str.strip()

    return df


def filter_karaoke_data(df: pd.DataFrame, query: str) -> pd.DataFrame:
    """
    Filtra o dataframe considerando número, música, artista ou gênero.

    A busca ignora acentos, caixa alta/baixa e aceita trechos parciais.
    """
    if not query:
        return df

    normalized_query = _normalize_text(query)

    # Criamos um texto único por linha para facilitar a busca.
    search_text = (
        df["numero"] + " " + df["musica"] + " " + df["artista"] + " " + df["genero"]
    ).map(_normalize_text)

    mask = search_text.str.contains(normalized_query, na=False)
    return df[mask]
