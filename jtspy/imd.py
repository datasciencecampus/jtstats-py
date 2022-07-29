import pandas as pd
import jtspy.geo as jtsgeo
import geopandas as gpd


def _imd_dictionary():
    '''
    

    Returns
    -------
    imd_dict : python dictionary.
        Returns a dictionary used to transform short labels of IMD domains into
        the correct labels used in the IMD data set.

    '''
    
    
    # TODO: could add supplementary indices and even sub domains if needed
    imd_dict = {'imd_rank_2015': 'Index of Multiple Deprivation (IMD) Rank (where 1 is most deprived)',
                'imd_rank_2019': 'Index of Multiple Deprivation (IMD) Rank',
                'income_rank': 'Income Rank (where 1 is most deprived)',
                'employment_rank': 'Employment Rank (where 1 is most deprived)',
                'education_rank': 'Education, Skills and Training Rank (where 1 is most deprived)',
                'health_rank': 'Health Deprivation and Disability Rank (where 1 is most deprived)',
                'crime_rank': 'Crime Rank (where 1 is most deprived)',
                'barriers_rank': 'Barriers to Housing and Services Rank (where 1 is most deprived)',
                'environment_rank': 'Living Environment Rank (where 1 is most deprived)',
                'imd_score': 'Index of Multiple Deprivation (IMD) Score',
                'income_score': 'Income Score (rate)',
                'employment_score': 'Employment Score (rate)',
                'education_score': 'Education, Skills and Training Score',
                'health_score': 'Health Deprivation and Disability Score',
                'crime_score': 'Crime Score',
                'barriers_score': 'Barriers to Housing and Services Score',
                'environment_score': 'Living Environment Score'}
    
    return imd_dict

def _imd_url(year, rank = True, domain = False):
    '''
    

    Parameters
    ----------
    year : integer
        Year for which IMD data is required.
    rank : boolean, optional
        Whether IMD ranks or scores are required. The default is True.
    domain : boolea , optional
        Whether the general IMD data or data from the IMD domains is required.
        The default is False.

    Returns
    -------
    url : string
        The url at which the required IMD data can be downloaded from.

    '''
    
    # TODO: improve this section
    
    if year == 2015 and rank and not domain:
        
        url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/467764/File_1_ID_2015_Index_of_Multiple_Deprivation.xlsx'
        
    elif year == 2015 and not rank:
        
        url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/467768/File_5_ID_2015_Scores_for_the_Indices_of_Deprivation.xlsx'
        
    elif year == 2015 and rank and domain:
        
        url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/467765/File_2_ID_2015_Domains_of_deprivation.xlsx'
        
    elif year == 2019 and rank and not domain:
        
        url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/833970/File_1_-_IMD2019_Index_of_Multiple_Deprivation.xlsx'
        
    elif year ==2019 and not rank:
        
        url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/833978/File_5_-_IoD2019_Scores.xlsx'
        
    elif year == 2019 and rank and domain:
        
        url = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/833973/File_2_-_IoD2019_Domains_of_Deprivation.xlsx'
        
    return url


def get_imd(domain, year, rank = True, level = 'lsoa', geo = False):
    '''
    

    Parameters
    ----------
    domain : string
        The short label of the domain of the IMD required. See dictionary in method _imd_dictionary
        for a description of the possible values. Note that you do not need to
        add the suffixes rank or score to the domain label.
    year : integer
        The year of IMD data required.
    rank : boolean, optional
        Whether rank or scores of IMD are required. The default is True.
    level : string, optional
        Spatial level at which IMD data is required. The default is 'lsoa'.
    geo: boolean
        Whether geographic boundaries are required or not. The default is False.

    Returns
    -------
    imd_df : pandas dataframe
        Data frame containing the IMD data.

    '''
    
    # TODO: implement option for local authority level data
    # TODO: rethink structure for efficiency
    
    imd_dict = _imd_dictionary()
    
    if domain == 'imd':
        
        url = _imd_url(year, rank = rank, domain = False)
        
    else:
        
        url = _imd_url(year, rank = rank, domain = True)
    
    if rank:
        
        if domain == 'imd' and year == 2015:
            
            sheet_name = 'IMD ' + str(year)
            
        elif domain == 'imd' and year == 2019:
            
            sheet_name = 'IMD' + str(year)
            
        else:
            
            sheet_name = 'ID' + str(year) + ' Domains'
            
    else:
        
        sheet_name = 'ID' + str(year) + ' Scores'
    
    sheet_name = 1
    imd_data = pd.read_excel(url, sheet_name = sheet_name)
    
    if level == 'lsoa' and rank:
        
        if domain == 'imd':
            
            imd_df = imd_data[['LSOA code (2011)', imd_dict[domain + '_rank_'  + str(year)]]]
        
        else:
            
            imd_df = imd_data[['LSOA code (2011)', imd_dict[domain +'_rank']]]
        
        if geo:
            
            geo_gdf = jtsgeo.get_lsoa_boundaries()
            return gpd.GeoDataFrame(geo_gdf.merge(imd_df, left_on = 'LSOA11CD', right_on = 'LSOA code (2011)', how = 'inner'))
        
    elif level == 'lsoa' and not rank:
        
        imd_df = imd_data[['LSOA code (2011)', imd_dict[domain + '_score']]]
        
        if geo:
            
            geo_gdf = jtsgeo.get_lsoa_boundaries()
            return gpd.GeoDataFrame(geo_gdf.merge(imd_df, left_on = 'LSOA11CD', right_on = 'LSOA code (2011)', how = 'inner'))
    
    return imd_df
        
        
