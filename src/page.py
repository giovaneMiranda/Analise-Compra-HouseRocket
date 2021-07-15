import streamlit as st
import pandas as pd
import plotly.express as px


def highlight_suggestion(val):
    color = '#5fba7d' if val == 'Buy' else '#d65f5f'
    return 'background-color: %s' % color


def purchase_analysis_ui(df_purchase, f_column_buying, f_buying_price, f_only_buy):
    if f_only_buy:
        df_purchase = df_purchase.query('buying_analysis == "Buy"')

    df_purchase_filtered = df_purchase.loc[df_purchase['price'] <= f_buying_price, f_column_buying].copy()
    df_purchase_style = df_purchase_filtered.style.applymap(highlight_suggestion,
                                                            subset=pd.IndexSlice[:, ['buying_analysis']])
    st.dataframe(df_purchase_style)

    return None


def sale_analysis_ui(df_sale, f_column_sale):

    df_sale_filtered = df_sale.loc[:, f_column_sale]
    st.dataframe(df_sale_filtered)
    df_season_profit = df_sale_filtered[['seasonality', 'expected_profit']].groupby('seasonality').sum()

    fig_season_profit = px.bar(df_season_profit)
    st.plotly_chart(fig_season_profit, use_container_width=True)
    return None


def run_ui(df_house_purchase, df_house_sale, df_house_profit):
    """Generate main page"""

    # creating sidebar
    st.sidebar.title('House Rocket Filter')
    st.sidebar.subheader('Buying Suggestions')

    # filter : Properties Attributes
    f_column_purchase = st.sidebar.multiselect('Properties Attributes', options=list(df_house_purchase.columns),
                                               default=['id', 'zipcode', 'price', 'condition',
                                                        'median_price_zip', 'buying_analysis'])
    # filter: house max price
    f_buying_price = st.sidebar.slider('Select maximum price', min_value=int(df_house_purchase['price'].min()),
                                       max_value=int(df_house_purchase['price'].max()),
                                       value=int(df_house_purchase['price'].max()), step=1)
    # filter: buying_analysis
    f_only_buy = st.sidebar.checkbox('Check to see only properties suggestted to be purchased')

    st.sidebar.subheader('Selling Suggestions')
    # filter : Properties Attributes
    f_column_sale = st.sidebar.multiselect('Properties Attributes', options=list(df_house_sale.columns),
                                                default=['id', 'zipcode', 'price','seasonality',
                                                         'median_price_seasonality', 'condition',
                                                         'selling_price_suggestion', 'expected_profit'])

    # creating main content
    st.title('House Rocket Data Report')

    st.subheader('Buying Suggestions')
    purchase_analysis_ui(df_house_purchase, f_column_purchase, f_buying_price, f_only_buy)

    st.subheader('Selling Suggestion')
    st.write('Once the house is owned by the company, below we show the analysis of the '
             'best time to sell them and what the sale price would be.')
    sale_analysis_ui(df_house_profit, f_column_sale)

    exp_profit = st.beta_expander('Click here to expand and see full analysis selling table')

    with exp_profit:
        st.dataframe(df_house_sale)

    return None