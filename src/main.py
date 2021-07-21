import pandas as pd
import streamlit as st
import page as pg


@st.cache(allow_output_mutation=True)
def extraction_dataset(path):
    data = pd.read_csv(path)

    return data


def apply_date_seasonality(month):
    return 'Winter' if (month == 1) | (month == 2) | (month == 12) \
        else ('Spring' if (month >= 3) & (month <= 5)
              else ('Summer' if (month >= 6) & (month <= 8) else 'Fall'))


def convert_sqft_m2(foot):
    return foot / 10.764


def calculate_percentage(value, percentage):
    return value * (percentage / 100)


def transform_date(data):
    """Generates a column seasonality based on date"""

    data['date'] = pd.to_datetime(data['date']).dt.date

    return data


def gen_buying_table(df_house):
    """Generates a columns with buying suggestion"""

    df_purchase = df_house.copy()
    df_purchase['median_price_zip'] = df_purchase.groupby('zipcode')['price'].transform('median')

    for index, row in df_purchase.iterrows():
        if (row['price'] < row['median_price_zip']) & (row['condition'] >= 3):
            df_purchase.loc[index, 'buying_analysis'] = 'Buy'

        else:
            df_purchase.loc[index, 'buying_analysis'] = 'Not Buy'

    df_purchase.to_csv('../data/processed/kc_house_purchase.csv', index=False)

    return df_purchase


def gen_sale_agg_table(df_house):
    """Generate sale analysis DF, calculating the median price per zipcode and seasonality"""

    df_sale = df_house[['id', 'zipcode', 'price', 'date']].copy()

    # creating new column seasonality, describing witch season the property was available.
    df_sale['seasonality'] = pd.to_datetime(df_sale['date']).dt.month.apply(apply_date_seasonality)

    # generate df of median price per zipcode and seasonality
    df_median_seasonality = df_sale.groupby(['zipcode', 'seasonality'])['price'].median().to_frame(
        name='median_price_season').reset_index()

    df_house_merge_median = df_house.merge(df_median_seasonality, on='zipcode')

    for index, row in df_house_merge_median.iterrows():
        if row['price'] > row['median_price_season']:
            df_house_merge_median.loc[index, 'selling_price_suggestion'] = row['price'] + calculate_percentage(
                row['price'], 10)
        else:
            df_house_merge_median.loc[index, 'selling_price_suggestion'] = row['price'] + calculate_percentage(
                row['price'], 30)

    df_house_merge_median['expected_profit'] = df_house_merge_median['selling_price_suggestion'] - \
                                               df_house_merge_median['price']

    df_house_merge_median.to_csv('../data/processed/kc_house_sale.csv', index=False)

    return df_house_merge_median


def gen_profit_table(data_purchase, data_sale):
    """Generate profit analysis DF, based on each house and price per season"""

    df_purchase_filtered = data_purchase.query('buying_analysis == "Buy"').copy()
    df_sale_filtered = data_sale[['id', 'seasonality', 'median_price_season',
                                                       'selling_price_suggestion', 'expected_profit']].copy()
    data_merge = df_purchase_filtered.merge(df_sale_filtered, on='id')

    l_house = list(data_merge['id'].unique())
    l_profit = []

    # iterate each house price per season, taking the one with max profit
    for id_house in l_house:
        row = data_merge[data_merge['id'] == id_house]['expected_profit'].idxmax()
        l_profit.append(data_merge.loc[row].to_dict())

    df_profit = pd.DataFrame(l_profit)
    df_profit = df_profit.rename(columns={'seasonality': 'season_selling'})
    df_profit.to_csv('../data/processed/kc_house_profit.csv', index=False)
    return df_profit


if __name__ == '__main__':

    st.set_page_config(
        page_title="House Rocket Insights",
        page_icon="🏠",
        initial_sidebar_state="expanded",
        layout='wide')

    path = '../data/raw/kc_house_data.csv'

    data_raw = extraction_dataset(path)
    data_normalize = transform_date(data_raw)

    data_purchase_processing = gen_buying_table(data_normalize)
    data_sale_processing = gen_sale_agg_table(data_normalize)
    data_profit = gen_profit_table(data_purchase_processing, data_sale_processing)

    pg.run_ui(data_purchase_processing, data_sale_processing, data_profit)
