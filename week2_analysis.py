# Week 2 - Exploratory Data Analysis
import pandas as pd
import numpy as np
# loading cleaned data from week 1
df = pd.read_csv('cleaned_aqi_data.csv')
print("=== EXPLORATORY DATA ANALYSIS ===\n")
# 1. City-wise analysis
print("1. CITY-WISE AQI ANALYSIS")
print("-" * 50)
city_stats = df.groupby('City')['AQI'].agg(['mean', 'median', 'min', 'max', 'std'])
city_stats = city_stats.sort_values('mean', ascending=False)
print(city_stats)
# finding which city has worst air quality
worst_city = city_stats.index[0]
print(f"City with worst average AQI: {worst_city}")
print(f"Average AQI: {city_stats.loc[worst_city, 'mean']:.2f}\n")
# 2. Seasonal patterns
print("2. SEASONAL ANALYSIS")
print("-" * 50)
seasonal_avg = df.groupby('Season')['AQI'].mean().sort_values(ascending=False)
print("Average AQI by season:")
print(seasonal_avg)
print(f"Worst season for air quality: {seasonal_avg.index[0]}")
print(f"Best season for air quality: {seasonal_avg.index[-1]}\n")
# 3. Monthly trends
print("3. MONTHLY TRENDS")
print("-" * 50)
monthly_avg = df.groupby('Month')['AQI'].mean().sort_values(ascending=False)
print("Average AQI by month:")
for month, aqi in monthly_avg.items():
    print(f"Month {month}: {aqi:.2f}")
# 4. Health category distribution
print("4. HEALTH CATEGORY DISTRIBUTION")
print("-" * 50)
health_dist = df['Health_Category'].value_counts()
print(health_dist)
total_days = len(df)
hazardous_days = len(df[df['Health_Category'] == 'Hazardous'])
print(f"Percentage of hazardous days: {(hazardous_days/total_days)*100:.2f}%\n")
# 5. Pollutant analysis
print("5. POLLUTANT ANALYSIS")
print("-" * 50)
# checking which pollutants are available in dataset
pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
available_pollutants = [p for p in pollutants if p in df.columns]
print(f"Available pollutants: {available_pollutants}\n")
if available_pollutants:
    print("Average pollutant levels:")
    for pollutant in available_pollutants:
        avg = df[pollutant].mean()
        print(f"{pollutant}: {avg:.2f}")
    # finding correlation between pollutants and AQI
    print("Correlation with AQI:")
    for pollutant in available_pollutants:
        corr = df['AQI'].corr(df[pollutant])
        print(f"{pollutant}: {corr:.3f}")
# 6. Year-over-year comparison
print("6. YEAR-OVER-YEAR TRENDS")
print("-" * 50)
if 'Year' in df.columns:
    yearly_avg = df.groupby('Year')['AQI'].mean()
    print("Average AQI by year:")
    print(yearly_avg)
    # checking if air quality is improving or getting worse
    years = sorted(df['Year'].unique())
    if len(years) >= 2:
        first_year_aqi = df[df['Year'] == years[0]]['AQI'].mean()
        last_year_aqi = df[df['Year'] == years[-1]]['AQI'].mean()
        if last_year_aqi < first_year_aqi:
            print(f"Air quality is IMPROVING (from {first_year_aqi:.2f} to {last_year_aqi:.2f})")
        else:
            print(f"Air quality is WORSENING (from {first_year_aqi:.2f} to {last_year_aqi:.2f})")
# 7. Hazardous days per city
print("7. HAZARDOUS DAYS BY CITY")
print("-" * 50)
hazardous_by_city = df[df['Health_Category'] == 'Hazardous'].groupby('City').size()
hazardous_by_city = hazardous_by_city.sort_values(ascending=False)
print("Number of hazardous days per city:")
print(hazardous_by_city)
# 8. City-Season combination analysis
print("8. CITY-SEASON ANALYSIS")
print("-" * 50)
city_season = df.groupby(['City', 'Season'])['AQI'].mean().unstack()
print("Average AQI by City and Season:")
print(city_season)
# saving analysis results
print("Saving analysis results")
# creating summary dataframe
summary = {
    'Total_Records': len(df),
    'Number_of_Cities': df['City'].nunique(),
    'Average_AQI': df['AQI'].mean(),
    'Median_AQI': df['AQI'].median(),
    'Worst_City': worst_city,
    'Worst_Season': seasonal_avg.index[0],
    'Hazardous_Days': hazardous_days,
    'Hazardous_Percentage': (hazardous_days/total_days)*100
}
summary_df = pd.DataFrame([summary])
summary_df.to_csv('analysis_summary.csv', index=False)
print("Analysis complete! Summary saved to 'analysis_summary.csv'")