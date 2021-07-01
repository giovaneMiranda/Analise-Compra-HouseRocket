import pandas as pd
import streamlit as st
import pagina as pg



@st.cache(allow_output_mutation=True)
def extraction_dataset(path):
    data = pd.read_csv(path)

    return data


def apply_seasonality(month):
    return 'Winter' if (month == 1) | (month == 2) | (month == 12) \
        else ('Spring' if (month >= 3) & (month <= 5)
              else ('Summer' if (month >= 6) & (month <= 8) else 'Fall'))


def transform_date(data):
    """Generates a column seasonality based on date"""
    data['date'] = pd.to_datetime(data['date']).dt.date
    data['seasonality'] = pd.to_datetime(data['date']).dt.month.apply(apply_seasonality)

    return data


def gen_purchase_table(df_house):
    """Generates a columns with the purchase suggestion"""
    df_purchase = df_house[['id','zipcode', 'price', 'condition']].copy()
    df_purchase['price_median'] = df_purchase.groupby('zipcode')['price'].transform('median')

    for index, row in df_purchase.iterrows():
        if (row['price'] < row['price_median']) & (row['condition'] >= 3):
            df_purchase.loc[index, 'purchase_analysis'] = 'Comprar'

        else:
            df_purchase.loc[index, 'purchase_analysis'] = 'Nao Comprar'

    df_purchase.columns = ['Id Casa', 'CEP', 'Preco', 'Condicao', 'Mediana do Preco na Regiao', 'Analise de Compra']

    return df_purchase


if __name__ == '__main__':


    st.set_page_config(
        page_title="House Rocket",
        page_icon="🏠",
        initial_sidebar_state="expanded",
        layout='wide')

    path = '../data/kc_house_data.csv'

    data_raw = extraction_dataset(path)
    data_normalize = transform_date(data_raw)
    data_processing = gen_purchase_table(data_normalize)

    pg.run_ui(data_processing)
