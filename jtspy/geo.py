import geopandas as gpd
from urllib.request import urlopen
import json
import pandas as pd

def get_lsoa_boundaries():
    '''
    

    Parameters
    ----------
    
    Returns
    -------
    lsoa_gdf: geopandas dataframe
        A geodatafrmae containing the LSOA boundaries.

    '''
    
    print('\n\n\n')
    print('Hang on, this may take a little while...')
    print('\n\n\n')
    
    url = 'https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/LSOA_Dec_2021_Boundaries_Generalised_Clipped_EW_BGC_2022/FeatureServer/0/query?where=1%3D1&outFields=*&returnIdsOnly=true&outSR=4326&f=json'

    response = urlopen(url)
    json_data = response.read().decode()

    id_list = json.loads(json_data)['objectIds']

    lsoa_gdf = gpd.GeoDataFrame()

    while id_list:
        
        temp_id = id_list[0:250]
        
        temp_url = 'https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/LSOA_Dec_2021_Boundaries_Generalised_Clipped_EW_BGC_2022/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json&objectIds=' + ','.join(str(x) for x in temp_id)
        
        temp_gdf = gpd.read_file(temp_url)
        
        lsoa_gdf = gpd.GeoDataFrame(pd.concat([lsoa_gdf, temp_gdf]))
        
        id_list = [x for x in id_list if x not in temp_id]
        
    lsoa_gdf.to_crs(' EPSG:3857', inplace = True)
    
    return lsoa_gdf

def get_la_boundaries():
    '''
    

    Parameters
    ----------
    
    Returns
    -------
    la_gdf: geopandas dataframe
        A geodatafrmae containing the LA boundaries.

    '''
    
    print('\n\n\n')
    print('Hang on, this may take a little while...')
    print('\n\n\n')
    
    la_gdf = gpd.read_file('https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2011_FCB_EW_2022/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')
    #lsoa_gdf.to_crs('EPSG:27700', inplace = True)
    la_gdf.to_crs(' EPSG:3857', inplace = True)
    
    return la_gdf




