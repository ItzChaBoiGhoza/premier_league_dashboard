# import libraries
import pandas as pd
import numpy as np

# preprocessing data

# load player data
def player_data(file_path):
    df = pd.read_csv(file_path)
    
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
    
    # creating an abbreviation column
    team_abbreviation = {
        'Arsenal': 'ARS',
        'Chelsea': 'CHE',
        'Manchester City': 'MCI',
        'Manchester United': 'MUN',
        'Tottenham Hotspur': 'TOT',
        'West Ham United': 'WHU',
        'Liverpool FC': 'LIV',
        'Leeds United': 'LEE',
        'Newcastle United': 'NEW',
        'Aston Villa': 'AVL',
        'Brighton': 'BHA',
        'Wolverhampton Wanderers': 'WOL',
        'Everton': 'EVE',
        'Fulham': 'FUL',
        'Crystal Palace': 'CRY',
        'Burnley': 'BUR',
        'West Bromwich Albion': 'WBA',
        'Leicester City': 'LEI',
        'Sheffield United': 'SHU',
        'Southampton': 'SOU'
    }
    df['Team_Abbreviation'] = df['Club'].map(team_abbreviation)

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

    return df[df['Matches'] == 38]

# function for vertical expansion
def exploding_column(df, column):
    explode_df = df.explode(column).reset_index(drop=True)

    return explode_df

# load team data
def team_data(file_path):
    df = pd.read_csv(file_path)
    
    # eliminate the betting columns
    new_df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'Referee', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']].copy()
    pd.set_option('display.max_columns', None)
    
    # standardizing date by converting the data type
    new_df['Date'] = pd.to_datetime(new_df['Date'], format='%d/%m/%Y')
    new_df['Date'] = new_df['Date'].dt.strftime('%m/%d/%Y')
    
    # standardizing column names
    column_name = [
        'Date',
        'Home_Team',
        'Away_Team',
        'Home_Goals',
        'Away_Goals',
        'Match_Results',
        'Referee',
        'Home_Shots',
        'Away_Shots',
        'Home_Shots_on_Target',
        'Away_Shots_on_Target',
        'Home_Fouls_Committed',
        'Away_Fouls_Committed',
        'Home_Corners',
        'Away_Corners',
        'Home_Yellow_Cards',
        'Away_Yellow_Cards',
        'Home_Red_Cards',
        'Away_Red_Cards'
    ]
    new_df.columns = column_name
    # matchday stadium
    stadium_name = {
        'Liverpool': 'Anfield',
        'Man City': 'Etihad Stadium',
        'Man United': 'Old Trafford',
        'West Brom': 'The Hawthorns',
        'Newcastle': 'St. James\' Park',
        'Wolves': 'Molineux Stadium',
        'Leicester': 'King Power Stadium',
        'West Ham': 'London Stadium',
        'Tottenham': 'Tottenham Hotspur Stadium',
        'Leeds': 'Elland Road',
        'Fulham': 'Craven Cottage',
        'Crystal Palace': 'Selhurst Park',
        'Arsenal': 'Emirates Stadium',
        'Aston Villa': 'Villa Park',
        'Chelsea': 'Stamford Bridge',
        'Everton': 'Goodison Park',
        'Sheffield United': 'Bramall Lane',
        'Burnley': 'Turf Moor',
        'Southampton': 'St. Mary\'s Stadium',
        'Brighton': 'American Express Stadium' 
    }
    new_df['Matchday_Stadium'] = new_df['Home_Team'].map(stadium_name)

    # standardizing team name
    full_team_name = {
        'Liverpool': 'Liverpool FC',
        'Man City': 'Manchester City',
        'Man United': 'Manchester United',
        'West Brom': 'West Bromwich Albion',
        'Newcastle': 'Newcastle United',
        'Wolves': 'Wolverhampton Wanderers',
        'Leicester': 'Leicester City',
        'West Ham': 'West Ham United',
        'Tottenham': 'Tottenham Hotspur',
        'Leeds': 'Leeds United',
        'Fulham': 'Fulham',
        'Crystal Palace': 'Crystal Palace',
        'Arsenal': 'Arsenal',
        'Aston Villa': 'Aston Villa',
        'Chelsea': 'Chelsea',
        'Everton': 'Everton',
        'Sheffield United': 'Sheffield United',
        'Burnley': 'Burnley',
        'Southampton': 'Southampton',
        'Brighton': 'Brighton'
    }
    new_df['Home_Team'] = new_df['Home_Team'].map(full_team_name)
    new_df['Away_Team'] = new_df['Away_Team'].map(full_team_name)
    
    # creating a team abbreviation
    team_abbreviation = {
        'Arsenal': 'ARS',
        'Chelsea': 'CHE',
        'Manchester City': 'MCI',
        'Manchester United': 'MUN',
        'Tottenham Hotspur': 'TOT',
        'West Ham United': 'WHU',
        'Liverpool FC': 'LIV',
        'Leeds United': 'LEE',
        'Newcastle United': 'NEW',
        'Aston Villa': 'AVL',
        'Brighton': 'BHA',
        'Wolverhampton Wanderers': 'WOL',
        'Everton': 'EVE',
        'Fulham': 'FUL',
        'Crystal Palace': 'CRY',
        'Burnley': 'BUR',
        'West Bromwich Albion': 'WBA',
        'Leicester City': 'LEI',
        'Sheffield United': 'SHU',
        'Southampton': 'SOU'
    }
    new_df['Home_Abbreviation'] = new_df['Home_Team'].map(team_abbreviation)
    new_df['Away_Abbreviation'] = new_df['Away_Team'].map(team_abbreviation)
    
    # incorrect input referee
    # 'A Moss' has never officiated a game, rather it was 'J Moss'
    #print("row number: ", new_df[new_df['Referee'] == 'A Moss'].index.to_list())
    new_df.loc[359,'Referee'] = 'J Moss'
    
    # standardizing referee names
    referee_full_name = {
        'C Kavanagh': 'Chris Kavanagh',
        'J Moss': 'Jonathan Moss',
        'M Oliver': 'Michael Oliver',
        'S Attwell': 'Stuart Attwell',
        'A Taylor': 'Anthony Taylor',
        'M Atkinson': 'Martin Atkinson',
        'C Pawson': 'Craig Pawson',
        'M Dean': 'Mike Dean',
        'D Coote': 'David Coote',
        'K Friend': 'Kevin Friend',
        'P Tierney': 'Paul Tierney',
        'L Mason': 'Lee Mason',
        'G Scott': 'Graham Scott',
        'A Marriner': 'Andre Marriner',
        'P Bankes': 'Peter Bankes',
        'S Hooper': 'Simon Hooper',
        'A Madley': 'Andrew Madley',
        'D England': 'Darren England',
        'R Jones': 'Robert Jones',
        'A Moss': 'A Moss'
    }
    new_df['Referee'] = new_df['Referee'].map(referee_full_name)
    
    return new_df

print("This is from the team dataset: ", team_data('./data/EPL_20_21.csv'))
#print("This is from the player dataset: ", player_data('./data/EPL_20_21_PLAYERS.csv'))