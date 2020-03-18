from util.pandas import csv_to_dataframe, df_haversine


def run(radius_mi: int, loc: tuple):
    print(f'Number of Confirmed COVID-19 cases within a {radius_mi:,} mile radius of {loc[2]} ({loc[0]}, {loc[1]}).')
    print('\nData source provided by JHU CSSE')
    print('https://systems.jhu.edu/research/public-health/ncov/')
    print('https://github.com/CSSEGISandData/COVID-19\n')

    csv_path = '../csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'

    df = csv_to_dataframe(csv_path)
    df = df[(df['Country/Region'] == 'US')]
    df['distance'] = df.apply(lambda row: df_haversine(row['Lat'], row['Long'], loc[0], loc[1]), axis=1)

    df = df[(df['distance'] <= radius_mi)]
    df.sort_values('distance', inplace=True)

    df.drop([
        'Province/State',
        'Country/Region',
        'Lat',
        'Long',
        'distance',
    ], axis=1, inplace=True)

    sum_all_series = df.sum()
    sum_all_df = sum_all_series.to_frame()
    sum_all_df = sum_all_df.rename(columns={0: 'count'})

    sum_all_df['% change (1 day)'] = sum_all_df['count'].pct_change(periods=1).fillna(0).round(2)
    sum_all_df['% change (5 day)'] = sum_all_df['count'].pct_change(periods=5).fillna(0).round(2)
    sum_all_df['% change (8 day)'] = sum_all_df['count'].pct_change(periods=8).fillna(0).round(2)
    print(sum_all_df.tail(14))


if __name__ == "__main__":
    HOME = (33.6394877, -118.3298942, 'Orange County, CA')
    run(radius_mi=400, loc=HOME)
