# import libraries
import pandas as pd
import numpy as np

# preprocessing data
def player_data(file_path):
    df = pd.read_csv(file_path)
    pd.set_option('display.max_columns', None)

    # wrangling position column
    df['Position'] = df['Position'].str.replace(" ", "")
    df['Position_in_List'] = df['Position'].str.split(',')

    # calculating for passes completed
    df['Passes_Completed'] =  ((df['Perc_Passes_Completed'] / 100) * df['Passes_Attempted']).round(0).astype('int64')

    # standardizing the nationality column
    nationality_dict = {
    'ENG': 'England',
    'SEN': 'Senegal',
    'GER': 'Germany',
    'ESP': 'Spain',
    'FRA': 'France',
    'ITA': 'Italy',
    'BRA': 'Brazil',
    'CRO': 'Croatia',
    'USA': 'United States',
    'DEN': 'Denmark',
    'MAR': 'Morocco',
    'SCO': 'Scotland',
    'ARG': 'Argentina',
    'POR': 'Portugal',
    'BEL': 'Belgium',
    'ALG': 'Algeria',
    'UKR': 'Ukraine',
    'NED': 'Netherlands',
    'SWE': 'Sweden',
    'URU': 'Uruguay',
    'SRB': 'Serbia',
    'WAL': 'Wales',
    'CIV': "Côte d'Ivoire",
    'NGA': 'Nigeria',
    'EGY': 'Egypt',
    'TUR': 'Turkey',
    'CMR': 'Cameroon',
    'GUI': 'Guinea',
    'SUI': 'Switzerland',
    'JPN': 'Japan',
    'IRL': 'Ireland',
    'GRE': 'Greece',
    'NIR': 'Northern Ireland',
    'GHA': 'Ghana',
    'AUT': 'Austria',
    'JAM': 'Jamaica',
    'RSA': 'South Africa',
    'CZE': 'Czech Republic',
    'POL': 'Poland',
    'PAR': 'Paraguay',
    'COD': 'Democratic Republic of the Congo',
    'KOR': 'South Korea',
    'COL': 'Colombia',
    'GAB': 'Gabon',
    'NOR': 'Norway',
    'AUS': 'Australia',
    'BIH': 'Bosnia and Herzegovina',
    'ISL': 'Iceland',
    'MKD': 'North Macedonia',
    'BFA': 'Burkina Faso',
    'ZIM': 'Zimbabwe',
    'SVK': 'Slovakia',
    'MEX': 'Mexico',
    'CAN': 'Canada',
    'MLI': 'Mali',
    'IRN': 'Iran',
    'NZL': 'New Zealand',
    'MTN': 'Mauritania', 
    'SKN': 'Saint Kitts and Nevis'
    }
    df['Nationality'] = df['Nationality'].map(nationality_dict)

    # goal contribution calculation
    df['Goal_Contribution'] = (df['Goals'] + df['Assists']).astype('int64')

    # xG overperformance
    df['xG_Overperformance'] = (df['Goals'] - df['xG']).round(2)

    # xA overperformance
    df['xA_Overperformance'] = (df['Assists'] - df['xA']).round(2)

    # per 90 performance
    df['Goals_per_90'] = ((df['Goals'] / df['Mins'].replace(0, np.nan)) * 90).round(2)
    df['Goals_Contribution_per_90'] = (((df['Goals'] + df['Assists']) / df['Mins'].replace(0, np.nan)) * 90).round(2)
    df['Assists_per_90'] = ((df['Assists'] / df['Mins'].replace(0, np.nan)) * 90).round(2)
    df['Passes_per_90'] = ((df['Passes_Attempted'] / df['Mins'].replace(0, np.nan)) * 90).round(2)
    df['Yellow_per_90'] = ((df['Yellow_Cards'] / df['Mins'].replace(0, np.nan)) * 90).round(2)
    df['Red_per_90'] = ((df['Red_Cards'] / df['Mins'].replace(0, np.nan)) * 90).round(2)

    return df
