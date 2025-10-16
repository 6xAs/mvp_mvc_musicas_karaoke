import streamlit as st

from models.df_karaoke import filter_karaoke_data, load_karaoke_data


SEARCH_STATE_KEY = "karaoke_search"
DISPLAY_COLUMNS = ["numero", "musica", "artista", "genero"]


def get_search_query() -> str:
    """Retorna a busca atual armazenada na sessão."""
    return st.session_state.get(SEARCH_STATE_KEY, "")


def set_search_query(value: str) -> None:
    """Atualiza o valor da busca no estado da aplicação."""
    st.session_state[SEARCH_STATE_KEY] = value


def clear_search() -> None:
    """Limpa o campo de busca."""
    st.session_state[SEARCH_STATE_KEY] = ""


def get_all_musicas():
    """Obtém o dataframe completo."""
    df = load_karaoke_data()
    return df, df[DISPLAY_COLUMNS]


def get_filtered_musicas(query: str, df=None):
    """Obtém o dataframe filtrado de acordo com a busca."""
    if df is None:
        df = load_karaoke_data()
    filtered = filter_karaoke_data(df, query)
    return filtered, filtered[DISPLAY_COLUMNS]
