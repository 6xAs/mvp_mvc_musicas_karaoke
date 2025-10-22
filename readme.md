# Karaoke Music Application

Aplicativo Streamlit simples organizado no padrão MVP/MVC para consulta de um catálogo de músicas de karaokê.

## Estrutura do Projeto

- `main.py`: ponto de entrada, configura a página e chama a view principal.
- `views/musicas_karaoke.py`: monta a interface Streamlit (busca, métricas e tabela).
- `controllers/musicaskaraokecontroller.py`: conecta view e modelo, controla estado da busca e filtros.
- `models/df_karaoke.py`: carrega o CSV e aplica normalização e filtros nos dados.
- `data/lista_musica_para_karaoke_id_genero.csv`: catálogo completo utilizado pela aplicação.
- `requirements.txt`: dependências necessárias (principalmente `streamlit` e `pandas`).

## Passo a Passo para Rodar

1. (Opcional) Remova qualquer ambiente virtual antigo (`.venv`) antes de criar um novo.
2. Crie um ambiente virtual: `python -m venv .venv`
3. Ative o ambiente:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute a aplicação: `streamlit run main.py`
6. Acesse o link exibido no terminal para interagir com o catálogo.

## Fluxo de Funcionamento

1. `main.py` inicia o Streamlit e chama `views.musicas_karaoke.main`.
2. A view garante que o estado da busca esteja pronto, exibe o campo de filtro e pede dados ao controller.
3. O controller delega ao modelo o carregamento completo (`load_karaoke_data`) e o filtro (`filter_karaoke_data`).
4. O dataframe filtrado volta para a view, que monta métricas e a tabela estilizada para o usuário.

## Dicas

- Adicione músicas ao arquivo CSV mantendo as colunas `numero`, `musica`, `artista` e `genero`.
- Ajuste estilos ou componentes da interface editando `views/musicas_karaoke.py`.
- Se alterar funções do modelo, limpe o cache do Streamlit (`st.cache_data`) reiniciando o app.
