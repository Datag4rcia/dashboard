import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm  # Necessário para trendline="ols"

# ✅ PRIMEIRO comando do Streamlit
st.set_page_config(page_title="Previsões com ExtraTrees", layout="wide")

# Agora o resto do app pode vir
st.title("📊 Dashboard Interativo - Previsões do ativo AAPL")

# Carregamento do CSV (exemplo com upload manual)
uploaded_file = st.file_uploader("📤 Envie o arquivo CSV de previsões", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Tabela de Resultados")
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Gráfico: Valor Real vs Predição")
    fig = px.scatter(
        df,
        x="Valor_Real",
        y="Predicao",
        trendline="ols",
        title="Dispersão entre valores reais e predições",
        labels={"Valor_Real": "Valor Real", "Predicao": "Predição"},
        color_discrete_sequence=["#2E86AB"]
    )
    st.plotly_chart(fig, use_container_width=True)

   # Gráfico de barras
    st.subheader("📊 Gráfico de Barras: Valor Real vs Predição")
    fig_bar = px.bar(
        df,
        x=df.index,
        y=["Valor_Real", "Predicao"],
        labels={"value": "Valor", "index": "Índice"},
        barmode="group",
        color_discrete_map={
            "Valor_Real": "#1f77b4",
            "Predicao": "#ff7f0e"
        },
        title="Comparação entre valores reais e predições"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # Métrica de erro
    erro_abs = (df['Valor_Real'] - df['Predicao']).abs()
    st.metric("Erro Médio Absoluto", f"{erro_abs.mean():.2f}")

    st.markdown("---")
    st.caption("Obrigada!")
else:
    st.warning("Por favor, envie um arquivo CSV para visualizar os dados.")
    st.stop()