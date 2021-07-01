import streamlit as st
import pandas as pd


def highlight_suggestion(val):
    color = '#5fba7d' if val == 'Comprar' else '#d65f5f'
    return 'background-color: %s' % color


def purchase_analysis_ui(df_purchase):
    df_purchase_style = df_purchase.style.applymap(highlight_suggestion, subset=pd.IndexSlice[:, ['Analise de Compra']])

    st.dataframe(df_purchase_style)


def run_ui(df_house):
    st.sidebar.title('Filtros House Rocket ')
    st.sidebar.subheader('Analise de Compra')
    st.sidebar.multiselect('Quais campos deseja mostrar', options = df_house.columns)

    st.title('House Rocket - Analise de Compra e Venda')
    purchase_analysis_ui(df_house)

    return None