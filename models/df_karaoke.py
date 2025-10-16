from pathlib import Path
import unicodedata

import pandas as pd
import streamlit as st


_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "lista_musica_para_karaoke_id_genero.csv"


def _normalize_text(value: str) -> str:
    """Remove acentos e coloca em minúsculo para comparações consistentes."""
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch)).lower()


@st.cache_data(show_spinner=False)
def load_karaoke_data() -> pd.DataFrame:
    """Carrega, higieniza e cacheia os dados de músicas de karaokê."""
    df = pd.read_csv(_DATA_PATH, sep=",", encoding="utf-8-sig")
    df = df.fillna("")
    df["numero"] = df["numero"].astype(str).str.strip()
    df["musica"] = df["musica"].astype(str).str.strip()
    df["artista"] = df["artista"].astype(str).str.strip()
    df["genero"] = df["genero"].astype(str).str.strip()

    # Índice auxiliar para buscas rápidas ignorando acentos
    search_index = (
        df["numero"] + " " + df["musica"] + " " + df["artista"] + " " + df["genero"]
    ).map(_normalize_text)
    df = df.assign(_search_index=search_index)
    return df


def filter_karaoke_data(df: pd.DataFrame, query: str) -> pd.DataFrame:
    """Aplica filtro por número, música, artista ou gênero."""
    if not query:
        return df

    normalized_query = _normalize_text(query)
    mask = df["_search_index"].str.contains(normalized_query, na=False)
    return df[mask]
