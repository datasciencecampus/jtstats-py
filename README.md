# Journey Time Statistics (JTS)

This Python package allows to easily access Journey Time Statistics (JTS) data released by the Department for Transport (DfT).

More information on this project can be found in the parent repository [JTS](https://github.com/datasciencecampus/jtstats).

To install this package, download this repository and run:

```
poetry install
```

or:

```
pip install .   
```

from within the folder. Installation directly via ```pip``` without downloading the code is not available yet.

To use the package, import it in your script:

````
import jtspy as jts
````

You can get some example JTS data as follows:

````
jts_data_0101 = jts.get_jts(table_code = 'jts0101', sheet = 'JTS0101')
jts_df = jts.get_jts(type_code = 'jts05', spec = 'employment', sheet = 2019, base_url = 'https://github.com/ITSLeeds/jts/releases/download/2/', table_code = None)
````

You can also retrieve data from the Index of Multiple Deprivation (IMD) with this package:
````
imd_df = jts.get_imd(domain = 'health', year  = 2019, rank = True, level = 'lsoa')
````

Or you can get a joint data frame with JTS and IMD data at the lower super output area (LSOA) level:
````
df = jts.jts_imd_lsoa('jts05', 'primary', 'PSWalkt', 'education')
````

The package also allows to retrieve LSOA boundaries so that the data can be plotted on a map (note: this takes a little while as the LSOA boundary file is large):
````
lsoa_gdf = jts.get_lsoa_boundaries()
jts.choropleth_map(lsoa_gdf, 'LSOA11CD', jts_df, 'LSOA_code', '100EmpPTt' , title = 'JTS travel time to employment centres by public transport', logscale = True)

jts.choropleth_map(lsoa_gdf, 'LSOA11CD', imd_df, 'LSOA code (2011)', 'Health Deprivation and Disability Rank (where 1 is most deprived)' ,
                   title = 'Health deprivation and disability rank (where 1 is most deprived)')
````

The maps can be saved by specifying an outpath in the call of the function; the file format can also be specified.
````
output_path = ''
output_format = 'pdf'
jts.choropleth_map(lsoa_gdf, 'LSOA11CD', imd_df, 'LSOA code (2011)', 'Health Deprivation and Disability Rank (where 1 is most deprived)' ,
                   title = 'Health deprivation and disability rank (where 1 is most deprived)', outpath = output_path, fmt = output_format)
````


Get a different JTS data set and plot it by mode of transport over the years (NOTE: we have to drop some rows because the mode "Walking" by itself is only available for 2019 so it cannot be compared over time).
````
jts_df =  jts.get_jts(table_code = 'jts0101', sheet = 'JTS0101')
drop_idx = jts_df.index[jts_df['Mode'] == 'Walking3']
jts_df.drop(drop_idx, axis = 0, inplace = True)

jts_pivoted = pd.pivot_table(jts_df, values='Food store', columns='Mode', index='Year')
fig = jts_pivoted.plot(title = 'Travel time to food stores by mode of transport', ylabel = 'Minutes').get_figure()
fig.savefig('/Users/fb394/Documents/GitHub/jts/figures/food_by_mode.pdf')
````

You can also find the above code on how to use this package in the [```tutorial.py```](https://github.com/datasciencecampus/jtstats-py/blob/main/tutorial.py) file, which provides a brief overview of the main functionalities of this package.
More information is avaliable in the associated [paper] and in a [blog post] on the [Office for National Statistics Data Science Campus](https://datasciencecampus.ons.gov.uk).

## 🛡 License

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/n10ds/jts/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{jts,
  author = {10DS},
  title = {R and Python packages to import JTS data},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/10ds/jts}}
}
```
