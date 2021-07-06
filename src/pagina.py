import streamlit as st
import pandas as pd


def highlight_suggestion(val):
    color = '#5fba7d' if val == 'Comprar' else '#d65f5f'
    return 'background-color: %s' % color


def purchase_analysis_ui(df_purchase, filter_column_purchase, filter_only_purchase):
    if filter_only_purchase:
        df_purchase = df_purchase.query('purchase_analysis == "Comprar"')

    df_purchase_filtered = df_purchase.loc[:, filter_column_purchase].copy()
    df_purchase_style = df_purchase_filtered.style.applymap(highlight_suggestion,
                                                            subset=pd.IndexSlice[:, ['purchase_analysis']])
    st.dataframe(df_purchase_style)

    return None


def sale_analysis_ui(df_sale, filter_coloum_sale ):
    df_sale_filtered = df_sale.loc[:, filter_coloum_sale].copy()
    st.dataframe(df_sale_filtered)

    return None


def run_ui(df_house_purchase, df_house_sale):
    """Generate main page"""

    st.sidebar.title('Filtros House Rocket ')
    st.sidebar.subheader('Análise de Compra')

    filter_column_purchase = st.sidebar.multiselect('Quais campos deseja mostrar', options=list(df_house_purchase.columns),
                                               default= ['id', 'zipcode', 'price', 'condition',
                                                          'price_median', 'purchase_analysis'])

    filter_only_purchase = st.sidebar.checkbox('Mostrar apenas os sugeridos para compra?')

    st.sidebar.subheader('Análise de Venda')
    filter_coloum_sale = st.sidebar.multiselect('Quais campos deseja mostrar', options=list(df_house_sale.columns),
                                                default=['id', 'zipcode', 'price','seasonality',
                                                         'seasonality_median_price', 'condition', 'sale_price', 'profit'])

    st.title('House Rocket - Análise do Portifolio')

    st.subheader('Análise de Compra')
    purchase_analysis_ui(df_house_purchase, filter_column_purchase, filter_only_purchase)

    st.subheader('Análise de Venda')
    sale_analysis_ui(df_house_sale, filter_coloum_sale)

    return None