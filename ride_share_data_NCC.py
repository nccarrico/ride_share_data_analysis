# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"

# Read the City and Ride Data
city_df = pd.read_csv(city_data_to_load)
ride_df = pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset
city_ride_df = pd.merge(city_df, ride_df)

# Display the data table for preview
city_ride_df.head()

# Determine what values exist in the data for type
city_ride_df['type'].unique()

# Make dataframes for each city type
urban_only = city_ride_df.loc[city_ride_df['type'] == 'Urban']
suburban_only = city_ride_df.loc[city_ride_df['type'] == 'Suburban']
rural_only = city_ride_df.loc[city_ride_df['type'] == 'Rural']


# ## Bubble Plot of Ride Sharing Data
# Calculate values for x and y axes
urban_x = urban_only.groupby('city')['ride_id'].count()
urban_y = urban_only.groupby('city')['fare'].mean()
urban_drivers = urban_only.groupby('city')['driver_count'].mean()

suburban_x = suburban_only.groupby('city')['ride_id'].count()
suburban_y = suburban_only.groupby('city')['fare'].mean()
suburban_drivers = suburban_only.groupby('city')['driver_count'].mean()

rural_x = rural_only.groupby('city')['ride_id'].count()
rural_y = rural_only.groupby('city')['fare'].mean()
rural_drivers = rural_only.groupby('city')['driver_count'].mean()

# Build the scatter plots for each city types
plt.scatter(urban_x, urban_y, s=urban_drivers*10, color='lightcoral', alpha=0.5, label='Urban',edgecolors='black')
plt.scatter(suburban_x, suburban_y, s=suburban_drivers*10, color='lightskyblue', alpha=0.5, label='Suburban', edgecolors='black')
plt.scatter(rural_x, rural_y, s=rural_drivers*10, color='gold', alpha=0.5, label='Rural', edgecolors='black')
plt.legend(title='City Types')
plt.title('Pyber Ride Sharing Data (2016)')
plt.xlabel('Total Number of Rides (per city)')
plt.ylabel('Average Fare ($)')
plt.grid()

# Incorporate a text label regarding circle size
plt.annotate("Note: Circle size correlates with driver count per city", xy=(42,35),annotation_clip=False)

# Save Figure
plt.savefig('pyber_ride_share_fig.png',bbox_inches="tight")

# Show Figure
plt.show()


# ## Total Fares by City Type

# Calculate Type Percents
total_fares = city_ride_df['fare'].sum()
urban_fares = urban_only['fare'].sum()
suburban_fares = suburban_only['fare'].sum()
rural_fares = rural_only['fare'].sum()
fares = [urban_fares / total_fares * 100, suburban_fares / total_fares * 100, rural_fares / total_fares *100]
fares

# Build Pie Chart
plt.pie(fares, explode=(0.1, 0, 0), labels=['Urban', 'Suburban', 'Rural'],         colors=('lightcoral', 'lightskyblue', 'gold'), autopct="%1.1f%%", shadow=True, startangle=270)
plt.title("Total Fares by City Type")
# Save Figure
plt.savefig('ride_share_fares_pie.png')

# Show Figure
plt.show()


# ## Total Rides by City Type

# Calculate Ride Percents
total_rides = city_ride_df['ride_id'].count()
urban_count = city_ride_df['type'].value_counts()['Urban']
suburban_count = city_ride_df['type'].value_counts()['Suburban']
rural_count = city_ride_df['type'].value_counts()['Rural']
type_pct = [urban_count / total_rides * 100, suburban_count / total_rides * 100, rural_count / total_rides * 100]
type_pct

# Build Pie Chart
plt.pie(type_pct, explode=(0.1, 0, 0), labels=['Urban', 'Suburban', 'Rural'],         colors=('lightcoral', 'lightskyblue', 'gold'), autopct="%1.1f%%", shadow=True, startangle=270)
plt.title("Total Rides by City Type")
# Save Figure
plt.savefig('ride_share_types_pie.png')

# Show Figure
plt.show()


# ## Total Drivers by City Type

# Calculate Driver Percents
urban_drv_count = urban_drivers.sum() 
suburban_drv_count = suburban_drivers.sum()
rural_drv_count = rural_drivers.sum()
total_drv = urban_drv_count + suburban_drv_count + rural_drv_count
driver_pct = [urban_drv_count / total_drv * 100, suburban_drv_count / total_drv * 100, rural_drv_count / total_drv *100]
driver_pct

# Build Pie Charts
plt.pie(driver_pct, explode=(0.1, 0, 0), labels=['Urban', 'Suburban', 'Rural'],         colors=('lightcoral', 'lightskyblue', 'gold'), autopct="%1.1f%%", shadow=True, startangle=270)
plt.title("Total Drivers by City Type")
# Save Figure
plt.savefig('ride_share_drivers_pie.png')

# Show Figure
plt.show()


# # Pyber Ride Share Data Summary
# * The number of rides is most abundant in urban cities followed by suburban and rural cities, while the fares for each ride are generally lower in urban cities and increasingly higher as they go from suburban to rural cities
# * While the individual fares are generally lower in urban cities, due to the greater number of total rides (68.4% of all rides), the overall fares collected is greatest in urban cities (62.7% of all fares collected)
# * The percentage of drivers in urban cities (80.9%) greatly outnumbers drivers in suburban and rural cities 
