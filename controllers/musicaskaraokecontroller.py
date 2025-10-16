import streamlit as st

from models.df_karaoke import filter_karaoke_data, load_karaoke_data


# Nome da chave que usaremos para guardar a busca no estado global do Streamlit.
SEARCH_STATE_KEY = "karaoke_search"
# Colunas que queremos mostrar no DataFrame final.
VISIBLE_COLUMNS = ["numero", "musica", "artista", "genero"]


def ensure_search_state() -> None:
    """Garante que exista um valor padrão para o campo de busca."""
    if SEARCH_STATE_KEY not in st.session_state:
        st.session_state[SEARCH_STATE_KEY] = ""


def get_search_value() -> str:
    """Retorna o texto que o usuário digitou no campo de busca."""
    return st.session_state[SEARCH_STATE_KEY]


def clear_search_value() -> None:
    """Limpa o campo de busca."""
    st.session_state[SEARCH_STATE_KEY] = ""


def get_full_catalog():
    """Carrega o catálogo completo e devolve tanto o DataFrame bruto quanto o conjunto de colunas visíveis."""
    df = load_karaoke_data()
    return df, df[VISIBLE_COLUMNS]


def get_filtered_catalog(search_text: str, source_df=None):
    """
    Aplica o filtro sobre o catálogo.

    Recebe o DataFrame completo para evitar leituras repetidas quando já temos os dados em mãos.
    """
    df = source_df if source_df is not None else load_karaoke_data()
    filtered_df = filter_karaoke_data(df, search_text)
    return filtered_df, filtered_df[VISIBLE_COLUMNS]
