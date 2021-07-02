import streamlit as st
import pandas as pd


def highlight_suggestion(val):
    color = '#5fba7d' if val == 'Comprar' else '#d65f5f'
    return 'background-color: %s' % color


def purchase_analysis_ui(df_purchase):
    df_purchase_style = df_purchase.style.applymap(highlight_suggestion, subset=pd.IndexSlice[:, ['purchase_analysis']])
    st.dataframe(df_purchase_style)

    return None


def sale_analysis_ui(df_sale):



    return None


def run_ui(df_house_purchase, df_house_sale):
    """Generate main page"""

    st.sidebar.title('Filtros House Rocket ')
    st.sidebar.subheader('Analise de Compra')

    filter_df_purchase = st.sidebar.multiselect('Quais campos deseja mostrar', options=list(df_house_purchase.columns),
                                               default= ['id', 'zipcode', 'price', 'condition',
                                                          'price_median', 'purchase_analysis'])

    st.sidebar.subheader('Analise de Compra')
    filter_df_sale = st.sidebar.multiselect('Quais campos deseja mostrar', options=list(df_house_sale.columns),
                                                default=['id', 'zipcode', 'price', 'condition',
                                                         'seasonality_median_price', 'sale_price'])


    df_purchase_filtered = df_house_purchase.loc[:, filter_df_purchase].copy()


    st.title('House Rocket - Analise de Compra e Venda')
    purchase_analysis_ui(df_purchase_filtered)

    return None