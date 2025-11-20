# Week 1 - Data Collection and Cleaning
import pandas as pd
import numpy as np
# reading the csv file
# make sure to put the file in same folder as this code
df = pd.read_csv('aqi_data.csv')
print("First few rows of data:")
print(df.head())
# checking what columns we have
print("Column names:")
print(df.columns)
# standardizing column names - kaggle datasets have different formats
# converting all column names to have consistent format
df.columns = df.columns.str.strip()  # remove any spaces
# handling different possible column name variations
column_mapping = {}
for col in df.columns:
    col_lower = col.lower()
    if 'date' in col_lower or 'time' in col_lower:
        column_mapping[col] = 'Date'
    elif col_lower == 'city' or col_lower == 'location':
        column_mapping[col] = 'City'
    elif col_lower == 'aqi' or col_lower == 'air quality index':
        column_mapping[col] = 'AQI'
    elif 'pm2.5' in col_lower or 'pm25' in col_lower:
        column_mapping[col] = 'PM2.5'
    elif 'pm10' in col_lower:
        column_mapping[col] = 'PM10'
    elif 'no2' in col_lower:
        column_mapping[col] = 'NO2'
    elif 'so2' in col_lower:
        column_mapping[col] = 'SO2'
    elif col_lower == 'co':
        column_mapping[col] = 'CO'
    elif col_lower == 'o3' or 'ozone' in col_lower:
        column_mapping[col] = 'O3'
if column_mapping:
    df = df.rename(columns=column_mapping)
    print("Column names standardized")
    print("New column names:")
    print(df.columns)
# basic info about dataset
print("Dataset information:")
print(df.info())
# checking for missing values
print("Missing values in each column:")
print(df.isnull().sum())
# removing rows where AQI value is missing because we need it
df = df.dropna(subset=['AQI'])
# for other columns, filling missing values with 0
df = df.fillna(0)
print("After handling missing values:")
print(df.isnull().sum())
# checking if there are any duplicate rows
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed")
# removing outliers - AQI should be between 0 and 500
print(f"Max AQI value before cleaning: {df['AQI'].max()}")
print(f"Min AQI value before cleaning: {df['AQI'].min()}")
# keeping only values between 0 and 500
df = df[(df['AQI'] >= 0) & (df['AQI'] <= 500)]
print(f"Max AQI value after cleaning: {df['AQI'].max()}")
print(f"Min AQI value after cleaning: {df['AQI'].min()}")
# converting date column to proper date format
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
# creating season column
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Summer'
    elif month in [6, 7, 8, 9]:
        return 'Monsoon'
    else:
        return 'Post-Monsoon'
df['Season'] = df['Month'].apply(get_season)
# creating health category based on AQI value
def aqi_category(aqi):
    if aqi <= 50:
        return 'Good'
    elif aqi <= 100:
        return 'Moderate'
    elif aqi <= 150:
        return 'Unhealthy for Sensitive Groups'
    elif aqi <= 200:
        return 'Unhealthy'
    elif aqi <= 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'
df['Health_Category'] = df['AQI'].apply(aqi_category)
print("New columns added:")
print(df.columns)
# saving cleaned data
df.to_csv('cleaned_aqi_data.csv', index=False)
print("Cleaned data saved as 'cleaned_aqi_data.csv'")
# some basic statistics
print("=== BASIC STATISTICS ===")
print(f"Total number of records: {len(df)}")
print(f"Number of cities: {df['City'].nunique()}")
print(f"Cities included: {df['City'].unique()}")
print(f"\nAverage AQI: {df['AQI'].mean():.2f}")
print(f"Median AQI: {df['AQI'].median():.2f}")
print(f"Highest AQI recorded: {df['AQI'].max():.2f}")
print(f"Lowest AQI recorded: {df['AQI'].min():.2f}")