import pandas as pd
import streamlit as st


@st.cache(allow_output_mutation=True)
def extraction_dataset(path):
    data = pd.read_csv(path)

    return data


def apply_seasonality(month):
    return 'Winter' if (month == 1) | (month == 2) | (month == 12) \
        else ('Spring' if (month >= 3) & (month <= 5)
              else ('Summer' if (month >= 6) & (month <= 8) else 'Fall'))


def transform_data(data):
    data['date'] = pd.to_datetime(data['date']).dt.date
    data['seasonality'] = pd.to_datetime(data['date']).dt.month.apply(apply_seasonality)

    return data


def run_ui(df_house):
    st.title('House Rocket - Analise de Compra e Venda')

    return None


if __name__ == '__main__':
    st.set_page_config(
        page_title="House Rocket",
        page_icon="🏠",
        initial_sidebar_state="expanded",
        layout='wide')

    path = '../data/kc_house_data.csv'

    data_raw = extraction_dataset(path)
    data_processing = transform_data(data_raw)
    run_ui(data_processing)
