import pandas as pd
import streamlit as st

from controllers.musicaskaraokecontroller import (
    SEARCH_STATE_KEY,
    clear_search,
    get_all_musicas,
    get_filtered_musicas,
    get_search_query,
    set_search_query,
)


def main():
    _inject_styles()
    _ensure_session_defaults()

    search_query = _render_search_section()
    full_df, display_full = get_all_musicas()
    filtered_df, display_filtered = get_filtered_musicas(search_query, full_df)

    _render_summary_metrics(len(display_full), len(display_filtered), search_query)
    _render_dataframe(display_filtered)


def _inject_styles() -> None:
    """Aplica ajustes visuais nas áreas de busca e tabela."""
    st.markdown(
        """
        <style>
        div[data-testid="stTextInput"] > label {
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.04rem;
            text-transform: uppercase;
            color: #1c355e;
        }
        div[data-testid="stTextInput"] input {
            font-size: 1.2rem;
            font-weight: 600;
            padding: 0.85rem 1rem;
            border-radius: 0.8rem;
            border: 2px solid #1c75bc;
            background-color: #f5fbff;
            color: #0b1f33;
        }
        div[data-testid="stMetricValue"] {
            font-weight: 700 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Garante que as chaves de sessão necessárias estejam inicializadas
def _ensure_session_defaults() -> None:
    if SEARCH_STATE_KEY not in st.session_state:
        set_search_query("")


def _render_search_section() -> str:
    st.markdown("#### 🔎 Encontre sua música em segundos")
    st.caption("Pesquise por número do catálogo, nome da música, artista ou gênero.")

    with st.container():
        search_col, clear_col = st.columns([6, 1])
        with search_col:
            st.text_input(
                "Busca no catálogo",
                key=SEARCH_STATE_KEY,
                placeholder="Ex.: 01039, Todo Azul do Mar, 14 Bis...",
                label_visibility="collapsed",
            )
        with clear_col:
            st.button("Limpar", on_click=clear_search, use_container_width=True)

    return get_search_query()


def _render_summary_metrics(total_count: int, filtered_count: int, query: str) -> None:
    col1, col2, col3 = st.columns([1, 1, 2])
    col1.metric("Total no catálogo", f"{total_count:,}".replace(",", "."))
    col2.metric("Resultados", f"{filtered_count:,}".replace(",", "."))

    if query:
        col3.success(f"Mostrando resultados para “{query}”.")
    else:
        col3.info("Use o campo de busca para filtrar rapidamente o catálogo.")


def _render_dataframe(display_df: pd.DataFrame) -> None:
    st.markdown("#### 🎵 Catálogo de músicas")

    if display_df.empty:
        st.warning("Nenhuma música corresponde à sua busca. Tente ajustar os termos.")
        return

    styled_df = display_df.style.set_properties(
        subset=["numero", "musica"], **{"font-weight": "bold"}
    )

    # Altura adaptativa para a grade, limitando a 20 linhas visíveis
    visible_rows = min(len(display_df), 20)
    height = 70 + visible_rows * 33

    st.dataframe(
        styled_df,
        use_container_width=True,
        height=height,
        hide_index=True,
        column_config={
            "numero": st.column_config.TextColumn("Número", width="small"),
            "musica": st.column_config.TextColumn("Música", width="large"),
            "artista": st.column_config.TextColumn("Artista"),
            "genero": st.column_config.TextColumn("Gênero"),
        },
    )
