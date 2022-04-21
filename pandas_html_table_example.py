import pandas as pd
import numpy as np

# Webpage url
# NASA Planetary Data
url = 'https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html'
# Wikipedia Table of Specific Heats
# url = 'https://en.wikipedia.org/wiki/Table_of_specific_heat_capacities'

# Extract tables
dataframes = pd.read_html(url)

# Get first table and transpose rows with columns
planetary_data = dataframes[0].transpose()

# Name the columns after the zeroth row
planetary_data.columns = planetary_data.iloc[0]

# Drop the zeroth row from the data
planetary_data = planetary_data.drop([0])

# Replace the blank cells (which import as NumPy not-a-number [nan])
planetary_data.rename(columns={np.nan: "Name"},
                      inplace=True)


# Create dictionary to store units
column_units = {}
column_headers = []
for column in planetary_data:
    try:
        name, unit = column.split(' (')
        column_units[name] = '('+unit
    except:
        name = column
        column_units[name] = ''
    column_headers.append(name.strip('?'))
planetary_data = planetary_data.set_axis(column_headers, axis=1, inplace=False)

# Drop duplicate last column
planetary_data = planetary_data.loc[:, ~planetary_data.columns.duplicated()]

# Drop Pluto (last row)
planetary_data = planetary_data[:-1]

# Extract planet name with mass
planetary_masses = planetary_data[['Name', 'Mass']]
for index, planet in planetary_masses.iterrows():
    print(f"{planet['Name']}\t{planet['Mass']}")
