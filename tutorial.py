### Example script to demonstrate some of the functionalities of the Python version

import jtspy as jts
import pandas as pd

### get some example JTS data
jts_data_0101 = jts.get_jts(table_code = 'jts0101', sheet = 'JTS0101')
jts_df = jts.get_jts(type_code = 'jts05', spec = 'employment', sheet = 2019, base_url = 'https://github.com/ITSLeeds/jts/releases/download/2/', table_code = None)

### get some example IMD data
imd_df = jts.get_imd(domain = 'health', year  = 2019, rank = True, level = 'lsoa')

### get a merged data frame with JTS and IMD data
df = jts.jts_imd_lsoa('jts05', 'primary', 'PSWalkt', 'education')

### get the LSOA boundaries and plot a map of JTS data (log scale for ease of interpretation)
### NOTE: this section can take a little while to run as it downloads a large
### file and then plots it
lsoa_gdf = jts.get_lsoa_boundaries()
jts.choropleth_map(lsoa_gdf, 'LSOA11CD', jts_df, 'LSOA_code', '100EmpPTt' , title = 'JTS travel time to employment centres by public transport', logscale = True)

### a map of the IMD data can also be plotted
jts.choropleth_map(lsoa_gdf, 'LSOA11CD', imd_df, 'LSOA code (2011)', 'Health Deprivation and Disability Rank (where 1 is most deprived)' ,
                   title = 'Health deprivation and disability rank (where 1 is most deprived)')

### the maps can be saved by specifying an outpath in the call of the function; file format can also be specified
output_path = ''
output_format = 'pdf'
jts.choropleth_map(lsoa_gdf, 'LSOA11CD', imd_df, 'LSOA code (2011)', 'Health Deprivation and Disability Rank (where 1 is most deprived)' ,
                   title = 'Health deprivation and disability rank (where 1 is most deprived)', outpath = output_path, fmt = output_format)




#get a different JTS data set and plot it by mode of transport over the years
#NOTE: we have to drop some rows because the mode "Walking" by itself is only available
#for 2019 so it cannot be compared over time.
jts_df =  jts.get_jts(table_code = 'jts0101', sheet = 'JTS0101')
drop_idx = jts_df.index[jts_df['Mode'] == 'Walking3']
jts_df.drop(drop_idx, axis = 0, inplace = True)

jts_pivoted = pd.pivot_table(jts_df, values='Food store', columns='Mode', index='Year')
fig = jts_pivoted.plot(title = 'Travel time to food stores by mode of transport', ylabel = 'Minutes').get_figure()
fig.savefig('/Users/fb394/Documents/GitHub/jts/figures/food_by_mode.pdf')

