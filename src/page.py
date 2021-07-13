import streamlit as st
import pandas as pd


def highlight_suggestion(val):
    color = '#5fba7d' if val == 'Buy' else '#d65f5f'
    return 'background-color: %s' % color


def purchase_analysis_ui(df_purchase, f_column_buying, f_only_buy):
    if f_only_buy:
        df_purchase = df_purchase.query('buying_analysis == "Buy"')

    df_purchase_filtered = df_purchase.loc[:, f_column_buying].copy()
    df_purchase_style = df_purchase_filtered.style.applymap(highlight_suggestion,
                                                            subset=pd.IndexSlice[:, ['buying_analysis']])
    st.dataframe(df_purchase_style)

    return None


def sale_analysis_ui(df_sale, filter_column_sale ):
    df_sale_filtered = df_sale.loc[:, filter_column_sale]
    st.dataframe(df_sale_filtered)

    return None



def run_ui(df_house_purchase, df_house_sale, df_house_profit):
    """Generate main page"""

    st.sidebar.title('Filtros House Rocket ')
    st.sidebar.subheader('Buying Suggestions')

    # filter : Properties Attributes
    f_column_purchase = st.sidebar.multiselect('Properties Attributes', options=list(df_house_purchase.columns),
                                               default=['id', 'zipcode', 'price', 'condition',
                                                        'median_price_zip', 'buying_analysis'])
    # filter: buying_analysis
    f_only_buy = st.sidebar.checkbox('Check to see only properties suggestted to be purchased')

    st.sidebar.subheader('Selling Suggestions')
    filter_column_sale = st.sidebar.multiselect('Properties Attributes', options=list(df_house_sale.columns),
                                                default=['id', 'zipcode', 'price','seasonality',
                                                         'median_price_seasonality', 'condition',
                                                         'selling_price_suggestion', 'expected_profit'])

    st.title('House Rocket Data Report')

    st.subheader('Buying Suggestions')
    purchase_analysis_ui(df_house_purchase, f_column_purchase, f_only_buy)

    st.subheader('Selling Suggestion')
    sale_analysis_ui(df_house_sale, filter_column_sale)

    exp_profit = st.beta_expander('Click here to expand and see estimated profit table')

    with exp_profit:
        st.dataframe(df_house_profit)

    return None