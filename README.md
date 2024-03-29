# Journey Time Statistics (JTS)

This Python package allows to easily access Journey Time Statistics (JTS) data released by the Department for Transport (DfT).

More information on this project can be found in the parent repository [JTS](https://github.com/datasciencecampus/jtstats).

To install this package, download this repository and run the following from the root directory of the repo:

```bash
# # If you have not previously installed poetry before...
# type the following for osx/linux/bashonwindows:
curl -sSL https://install.python-poetry.org | python3 -
# See https://python-poetry.org/docs/#installing-with-the-official-installer
poetry install
```

To open a Python session with all the dependencies you can run the following:

```bash
poetry shell
python
# From the Python shell, load the package to test it's installed:
import jtspy as jts
```

The you should be able to run the commands in [tutorial.py](tutorial.py).

To install the package with pip try the following:

```
pip install .   
```

from within the folder. Installation directly via ```PyPI``` without downloading the code is not available yet.

To use the package, import it in your script:

````
import jtspy as jts
````

You can get some example JTS data as follows:

````
jts_data_0101 = jts.get_jts(table_code = 'jts0101', sheet = 'JTS0101')
jts_df = jts.get_jts(type_code = 'jts05', spec = 'employment', sheet = 2019, table_code = None)
````

You can also plot JTS data at the Local Authority (LA) or at the Lower Super Output Area level (LSOA) for the JTS table for which this is available
by setting the ```geo``` flag to ```True``` and using a function from the package:

````
jts_df = jts.get_jts(type_code = 'jts05', spec = 'employment', sheet = 2019, geo = True)
jts.choropleth_map(jts_df, '500EmpPTt', title = 'JTS travel time to employment centres by public transport', logscale = True)
````
<img src = "Figures/jts_emp_pt.png"/>


The map can be saved by specifying an outpath in the call of the function; the file format can also be specified.
````
output_path = ''
output_format = 'pdf'
jts.choropleth_map(jts_df, '500EmpPTt',
                   title = 'Travel time to employment centres', outpath = output_path, fmt = output_format)
````

You can also retrieve data from the Index of Multiple Deprivation (IMD) with this package:
````
imd_df = jts.get_imd(domain = 'health', year  = 2019, rank = True, level = 'lsoa')
````

Or you can get a joint data frame with JTS and IMD data at the lower super output area (LSOA) level:
````
df = jts.jts_imd_lsoa('jts05', 'primary', 'PSWalkt', 'education')
````

The package also allows to retrieve LSOA (and LA) boundaries separately from the data:
````
lsoa_gdf = jts.get_lsoa_boundaries()
````

Get a different JTS data set and plot it by mode of transport over the years (NOTE: we have to drop some rows because the mode "Walking" by itself is only available for 2019 so it cannot be compared over time).
````
jts_df =  jts.get_jts(table_code = 'jts0101', sheet = 'JTS0101')
drop_idx = jts_df.index[jts_df['Mode'] == 'Walking3']
jts_df.drop(drop_idx, axis = 0, inplace = True)

jts_pivoted = pd.pivot_table(jts_df, values='Food store', columns='Mode', index='Year')
styles = ['-.','--','-']
jts_pivoted.plot(title = 'Travel time to food stores by mode of transport', ylabel = 'Minutes', style = styles)
````

<img src = "Figures/food_by_mode.png" />

You can also find the above code on how to use this package in the [```tutorial.py```](https://github.com/datasciencecampus/jtstats-py/blob/main/tutorial.py) file, which provides a brief overview of the main functionalities of this package.
More information is avaliable in the associated [paper] and in a [blog post] on the [Office for National Statistics Data Science Campus](https://datasciencecampus.ons.gov.uk).

## Development

The package includes a series of tests written using ````pytest```` which can be used when developing the package further to test that the basic functionalities are not affected.
The tests check that, for each JTS table, the package returns the correct number of columns with the correct names, and it also checks a predefined set of values to ensure the tables are parsed correctly.
Note that changes to the way the tables are parsed or changes in the shape of the resulting data frame will break the tests.
## 🛡 License

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/datasciencecampus/jtstats-py/blob/main/LICENSE) for more details.

