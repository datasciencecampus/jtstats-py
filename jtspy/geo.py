import geopandas as gpd


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
    
    lsoa_gdf = gpd.read_file('https://opendata.arcgis.com/datasets/1f23484eafea45f98485ef816e4fee2d_0.geojson')
    #lsoa_gdf.to_crs('EPSG:27700', inplace = True)
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
    
    la_gdf = gpd.read_file('https://opendata.arcgis.com/datasets/0c09b7cde8b44c4ab6e2a1e47a91e400_0.geojson')
    #lsoa_gdf.to_crs('EPSG:27700', inplace = True)
    la_gdf.to_crs(' EPSG:3857', inplace = True)
    
    return la_gdf
