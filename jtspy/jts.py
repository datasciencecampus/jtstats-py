import pandas as pd
import numpy as np
import pkg_resources
import jtspy.geo as jtsgeo
import geopandas as gpd

def get_jts(type_code = 'jts05', spec = 'employment', sheet = 2019, base_url = 'https://github.com/ITSLeeds/jts/releases/download/2/', table_code = None, geo = False):
    '''
    

    Parameters
    ----------
    type_code : string
        The jts type of data. Options are: jts01, jts02, jts03, jts04, jts05, jts09, jts10.
        The default is 'jts05'.
    spec : string
        Specifier of the data required. The default is employment.
    sheet : integer/string
        The sheet within the JTS dataset for which data is required. 
        Can be a year (2014, 2015, 2016, 2017, 2019) or a text string to identify
        a particular sheet. The function can handle both integer and string inputs
        for this variable. The default is 2019.
    table_code : string
        Exact JTS table code if already known. The default is None.
    base_url : string
        URL of where the data is. The default is 'https://github.com/datasciencecampus/jtstats/releases/tag/0'.
    geo: boolean
        Whether geographic boundaries are required or not. The default is False.

    Returns
    -------
    Pandas data frame containing the requested JTS data. If geo is True, the
    returned variable is a Geopandas data frame.

    '''
    
    if not table_code:
        
        tb_code = lookup_jts_table(type_code, spec, sheet)
    else:
        
        stream = pkg_resources.resource_stream(__name__, 'Data/jts_tables.csv')
        jts_tables = pd.read_csv(stream, encoding = 'latin-1')
        jts_idx = jts_tables.index[(jts_tables['table_code'] == table_code) & (jts_tables['sheet'] == str(sheet))].tolist()
        tb_code = jts_tables.iloc[jts_idx].reset_index(drop = True)
        
        type_code = table_code[0:5]
                                   
        
        
    download_url = base_url + tb_code['csv_file'].str.replace('(','.', regex = False).str.replace(')','', regex = False)
    
    #setting low_memory to False solves an issue with data types when reading
    #some of the files; however, this reads the whole file at once, so may
    #reduce efficiency
    try:
        
        df = pd.read_csv(download_url[0], low_memory = False)
        
        
        tcd = tb_code['table_code'][0]
        
        if '01' in type_code:
            
            if tcd == 'jts0101':
                
                cleaned_df = clean_jts(df, 'Year', sheet = sheet)
                
            elif tcd == 'jts0102':
                
                cleaned_df = clean_jts(df, 'Year', sheet = sheet)
                
            elif tcd == 'jts0103':
                
                cleaned_df = clean_jts(df, 'Year', sheet = sheet)
                
            elif tcd == 'jts0104':
                
                cleaned_df = clean_jts(df, 'Region', col_idx = True, sheet = sheet)
            
        elif '02' in type_code:
            
            if tcd == 'jts0203' or tcd == 'jts0204' or tcd == 'jts0205' or tcd == 'jts0206':
                
                cleaned_df = clean_jts(df, 'Year', sheet = sheet, flag_2 = True)
            
            else:
                
                cleaned_df = clean_jts(df, 'Year', sheet = sheet)
            
        elif '03' in type_code:
            
               cleaned_df = clean_jts(df, 'Year', sheet = sheet, flag_3 = True)
               
            
        elif '04' in type_code:
            
           cleaned_df = clean_jts(df, 'Region', sheet = sheet)
           
        elif '05' in type_code:
            
            cleaned_df = clean_jts(df, 'LSOA_code', sheet = sheet)
            
        elif '09' in type_code:
            
            if tcd == 'jts0901' or tcd == 'jts0903' or tcd == 'jts0904' or tcd == 'jts0921' or tcd == 'jts0923' or tcd == 'jts0924':
                
                cleaned_df = clean_jts(df, 'LA Code', sheet = sheet)
                
            elif tcd == 'jts0902' or tcd == 'jts0922':
                
                cleaned_df = clean_jts(df, 'Ref', sheet = sheet)
                
            elif tcd == 'jts0905' or tcd == 'jts0925' or tcd == 'jts0926':
                
                cleaned_df = clean_jts(df, 'LSOA Code', sheet = sheet)
                
            elif tcd == 'jts0930' and sheet == 'JTS0930_LA':
                
                #raise Warning('Not implemented yet')
                cleaned_df = clean_jts(df, 'Region', sheet = sheet)
                
            elif tcd == 'jts0930' and sheet == 'JTS0930_LSOA':
                 
                 #raise Warning('Not implemented yet')
                 cleaned_df = clean_jts(df, 'LSOA_Code', sheet = sheet)
                
        elif '10' in type_code:
            
            raise Warning('Not implemented yet')
            cleaned_df = pd.DataFrame()
        
        if geo:
            
            if any('LSOA' in x for x in cleaned_df.columns.values):
                
                geo_gdf = jtsgeo.get_lsoa_boundaries()
                return gpd.GeoDataFrame(geo_gdf.merge(cleaned_df, left_on = 'LSOA11CD', right_on = 'LSOA_code', how = 'inner'))
            elif any('LA_Code' in x for x in cleaned_df.columns.values):
                
                geo_gdf = jtsgeo.get_la_boundaries()
                return gpd.GeoDataFrame(geo_gdf.merge(cleaned_df, left_on = 'lad11cd', right_on = 'LA_Code', how = 'inner'))
            
        return cleaned_df

    except KeyError:
        
        raise Warning('One of the input values provided is not valid')
    

def lookup_jts_table(type_code = 'jts05', spec = 'employment', sheet = 2019):
    '''
    

    Parameters
    ----------
    type_code : string
        The jts type of data. Options are: jts01, jts02, jts03, jts04, jts05, jts09, jts10.
        The default is 'jts05'.
    spec : string
    sheet : integer/string
        The sheet within the JTS dataset for which data is required. 
        Can be a year (2014, 2015, 2016, 2017, 2019) or a text string to identify
        a particular sheet. The function can handle both integer and string inputs
        for this variable. The default is 2019.

    Returns
    -------
   tables_sheet: pandas dataframe
       Dataframe with name of jts table for downloading.

    '''
    
    # TODO: need to check the following line
    # jts_tables = pd.read_csv('Data/jts_tables.csv')
    
    stream = pkg_resources.resource_stream(__name__, 'Data/jts_tables.csv')
    jts_tables = pd.read_csv(stream, encoding = 'latin-1')
    
    match_type = jts_tables['table_type'].str.lower().str.contains(type_code.lower())
    tables_type = jts_tables[match_type]
    
    match_spec = tables_type['table_title'].str.lower().str.contains(spec.lower())
    tables_spec = tables_type[match_spec]
    
    match_sheet = tables_spec['csv_file'].str.lower().str.contains(str(sheet).lower())
    tables_sheet = tables_spec[match_sheet]
    
    return tables_sheet.reset_index(drop = True)
    


def clean_jts(df, starting_string, col_idx = False, sheet = 2019, flag_2 = False, flag_3 = False):
    '''
    

    Parameters
    ----------
    df : pandas dataframe
        Dataframe with JTS data before cleaning.
    starting_string: string
        A string representing the label of the row where the data starts.
        Example is 'year'.
    cold_idx: boolean
        A boolean used as flag to clean a specific version of the data.
        The default is False as this is the most common occurrence.
    sheet : integer/string
        The sheet within the JTS dataset for which data is required. 
        Can be a year (2014, 2015, 2016, 2017, 2019) or a text string to identify
        a particular sheet. The function can handle both integer and string inputs
        for this variable. The default is 2019.
    Returns
    -------
    clean_df: pandas dataframe
        Dataframe with JTS data after cleaning.

    '''
    
    column_names = df.columns
    rows_with_starting_string = df[column_names[0]].str.lower().str.contains(starting_string.lower())
    row_indices = np.where(rows_with_starting_string.fillna(False))[0]
    
    if col_idx:
        
        temp_index = row_indices[0]-1
    
    if len(row_indices) == 1:
        
        df_semiclean = df[row_indices[0]:len(df.index)].reset_index(drop = True)
        
    elif len(row_indices) > 1:
        
        df_semiclean = df[row_indices[0]:len(df.index)].reset_index(drop = True)
    
    else:
        
        raise ValueError('Could not clean data. String provided is not present in dataframe')
        
    
    if not col_idx:
        
        df_semiclean.columns = df_semiclean.iloc[0]
        df_semiclean = df_semiclean.drop([0])
        
        if sheet == 'JTS0101':
            
            # df_semiclean.columns.values[len(df_semiclean.columns)-2] = 'Average of 8 services'
            df_semiclean.rename(columns = {df_semiclean.columns[len(df_semiclean.columns)-2]: 'Average of 8 services'}, inplace = True)
            
        if sheet == 'JTS0904' or sheet == 'JTS0921_Nearest' or sheet == 'JTS0923' or sheet == 'JTS0924':
            
            df_semiclean.rename(columns = {df_semiclean.columns[2]: 'Local Authority Name'}, inplace = True)
        
        if sheet == 'JTS0922':
            
            df_semiclean.rename(columns = {df_semiclean.columns[17]: 'Population within 20km'}, inplace = True)
            
        
    elif col_idx:
        
        temp_cols = df_semiclean.iloc[0].reset_index(drop = True)
        new_idx = temp_cols[temp_cols == str(sheet)].index
        
        df_semiclean.columns = df_semiclean.iloc[0]
        df_semiclean.columns.values[new_idx] = df.iloc[temp_index][new_idx].values
        df_semiclean = df_semiclean.drop([0])
        col_names = df_semiclean.columns.values
        col_names[1] = 'LA Code'
        col_names[2] = 'Local authority'
        df_semiclean.columns = col_names

    if flag_2:
        
        #df_semiclean.columns.values[1] = 'Users with access'
        df_semiclean.rename(columns ={df_semiclean.columns[1]:'Users with access'}, inplace = True)
        df_semiclean['Users with access'].ffill(inplace = True)
        idx1 = np.where(df_semiclean[starting_string].str.lower().str.contains('Number'.lower()).fillna(False))[0][0]
        idx2 = np.where(df_semiclean[starting_string].str.lower().str.contains('Percentage'.lower()).fillna(False))[0][0]
        
        df_semiclean['Users with access'].iloc[idx1:idx2] = df_semiclean['Users with access'].iloc[idx1:idx2] + ' - Number'
        df_semiclean['Users with access'].iloc[idx2:] = df_semiclean['Users with access'].iloc[idx2:] + ' - Percentage'
        
        df_semiclean.drop([idx1+1,idx2], axis = 0, inplace = True)
    
    if flag_3:
        
        # if len(df_semiclean.columns.values < 20):
            
        #     df_semiclean.columns.values[len(df_semiclean.columns)-1] = 'Average of 8 services'
            
        # else:
            
            
        #     df_semiclean.columns.values[len(df_semiclean.columns)-1] = 'Average of 8 services'
        
        # df_semiclean.columns.values[df_semiclean.columns.get_loc('Town Centres')+1] = 'Average of 8 services'
        
        cols_names = df_semiclean.columns.values
        
        if pd.isnull(cols_names[1]):
            
            cols_names[1] = 'Distance (minutes)'
        
        if str(sheet) == '2019' or str(sheet) == '2017':
            
            cols_names[df_semiclean.columns.get_loc('Town Centres')+1] = 'Average of 8 services'
        
        df_semiclean.columns = cols_names
        # df_semiclean.rename(columns = {df_semiclean.columns[df_semiclean.columns.get_loc('Town Centres')+1]: 'Average of 8 services'}, inplace = True)
    
    
    if df_semiclean.columns.isna().any():
        
        df_semiclean.columns = df_semiclean.columns.fillna('todrop')
    
        clean_df = df_semiclean.drop('todrop',axis = 1)
    else:
        
        clean_df = df_semiclean
    
    clean_df.ffill(inplace = True)
    
    clean_df.dropna(axis = 0, how = 'all', inplace = True)
    
    if flag_3:
        
        # clean_df.drop(axis =0, index = [1,2], inplace = True)
        clean_df.dropna(axis = 0, how = 'any', inplace = True)
    
    if 'Year' in clean_df.columns:
        
        drop_idx = [x for x in clean_df.index if len(clean_df['Year'][x]) > 10]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        
    if 'LSOA Code' in clean_df.columns:

        drop_idx = [x for x in clean_df.index if len(clean_df['LSOA Code'][x]) > 9]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        
    if 'Region' == clean_df.columns[0]:

        drop_idx = [x for x in clean_df.index if (len(clean_df['Region'][x].replace(' ','')) > 21 or any(map(str.isdigit,clean_df['Region'][x])) or not all(map(str.isalnum, clean_df['Region'][x].replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        
    if 'LSOA_Code' == clean_df.columns[0]:

        drop_idx = [x for x in clean_df.index if len(clean_df['LSOA_Code'][x]) > 9]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        
    if sheet == 'JTS0901_Nearest':
        
        
        drop_idx = [x for x in clean_df.index if (len(clean_df['LA Code'][x].replace(' ','')) > 9 or not all(map(str.isalnum, clean_df['LA Code'][x].replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LA Code', 'Local Authority', 'Nearest airport by travel time (by public transport', 'Average travel time (minutes, by public transport)',
                            'Nearest airport by travel time (by car)', 'Average travel time (minutes, by car)']
        clean_df.replace(to_replace = '..', value = 240, inplace = True)
        
    if sheet == 'JTS0901_Selected':
        
        drop_idx = [x for x in clean_df.index if (len(clean_df['LA Code'][x].replace(' ','')) > 9 or not all(map(str.isalnum, clean_df['LA Code'][x].replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LA Code', 'Local Authority', 'Heathrow T2 by public transport', 'Heathrow T3 by public transport', 'Heathrow T4 by public transport', 'Heathrow T5 by public transport',
                            'Gatwick North Terminal by public transport', 'Gatwick South Terminal by public transport', 'Manchester T1 by public transport',
                            'Manchester T2 by public transport', 'Manchester T3 by public transport', 'Stansted by public transport', 'Luton by public transport', 'Edinburgh by public transport', 
                            'Birmingham by public transport', 'Glasgow by public transport', 'Bristol by public transport', 'Liverpool John Lennon by public transport', 'Newcastle by public transport',
                            'East Midlands by public transport', 'Aberdeen by public transport', 'London City by public transport', 'Leeds by public transport',
                            'Heathrow T2 by car', 'Heathrow T3 by car', 'Heathrow T4 by car', 'Heathrow T5 by car', 'Gatwick North Terminal by car', 'Gatwick South Terminal by car',
                            'Manchester T1 by car','Manchester T2 by car', 'Manchester T3 by car', 'Stansted by car', 'Luton by car', 'Edinburgh by car', 'Birmingham by car',
                            'Glasgow by car', 'Bristol by car', 'Liverpool John Lennon by car', 'Newcastle by car', 'East Midlands by car',
                            'Aberdeen by car', 'London City by car', 'Leeds by car']
        clean_df.replace(to_replace = '..', value = 240, inplace = True)
    
    if sheet == 'JTS0902':
        
        drop_idx = [x for x in clean_df.index if (len(clean_df['Ref'][x].replace(' ','')) > 9 or not all(map(str.isalnum, clean_df['Ref'][x].replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['Ref', 'Airport name', 'People within 30 minutes by public transport', 'People within 60 minutes by public transport', 'People within 120 minutes by public transport',
                            'People within 30 minutes by car', 'People within 60 minutes by car', 'People within 120 minutes by car',
                            '%People within 20km and within 30 minutes by public transport', '%People within 20km and within 60 minutes by public transport', '%People within 20km and within 120 minutes by public transport',
                            '%People within 20km and within 30 minutes by car', '%People within 20km and within 60 minutes by car', '%People within 20km and within 120 minutes by car']
        
    if sheet == 'JTS0903':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LA Code'][x]).replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LA Code', 'Local Authority', 'Population', '%People within 30 minutes by public transport', '%People within 60 minutes by public transport', '%People within 120 minutes by public transport',
                            '%People within 30 minutes by car', '%People within 60 minutes by car', '%People within 120 minutes by car']
        clean_df.at[clean_df.index.values[0], 'LA Code'] = 'England'
    
    if sheet == 'JTS0904':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LA Code'][x]).replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LA Code', 'Local Authority Area', 'Local Authority Name', 'Number airports within 30 mins by public transport', 'Number airports within 60 mins by public transport', 'Number airports within 120 mins by public transport',
                            'Number airports within 30 mins by car', 'Number airports within 60 mins by car', 'Number airports within 120 mins by car']
        
    if sheet == 'JTS0905_Selected':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LSOA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LSOA Code'][x]).replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LSOA Code', 'LSOA Name', 'Upper tier local authority code', 'Upper tier local authority name', 'LSOA population (2015)',
                            'Heathrow T2 by public transport', 'Heathrow T3 by public transport', 'Heathrow T4 by public transport', 'Heathrow T5 by public transport', 'Gatwick North Terminal by public transport', 'Gatwick South Terminal by public transport',
                            'Manchester T1 by public transport', 'Manchester T2 by public transport', 'Manchester T3 by public transport', 'Stansted by public transport', 'Luton by public transport',
                            'Birmingham by public transport', 'Bristol by public transport','Liverpool John Lennon by public transport', 'Newcastle by public transport', 'East Midlands by public transport',
                            'London City by public transport', 'Leeds by public transport',
                            'Heathrow T2 by car', 'Heathrow T3 by car', 'Heathrow T4 by car', 'Heathrow T5 by car', 'Gatwick North Terminal by car', 'Gatwick South Terminal by car',
                            'Manchester T1 by car', 'Manchester T2 by car', 'Manchester T3 by car', 'Stansted by car', 'Luton by car',
                            'Birmingham by car', 'Bristol by car','Liverpool John Lennon by car', 'Newcastle by car', 'East Midlands by car',
                            'London City by car', 'Leeds by car']
        clean_df.replace(to_replace = '..', value = 240, inplace = True)
        
    if sheet == 'JTS0905_Summary':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LSOA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LSOA Code'][x]).replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LSOA Code', 'LSOA Name', 'Upper tier local authority code', 'Upper tier local authority name', 'LSOA population (2015)',
                            'Nearest airport by public transport/walking travel time', 'Average minimum journey time by public transport/walking','Nearest airport by car time',
                            'Average minimum journey by car']
        clean_df.replace(to_replace = '..', value = 240, inplace = True)
    
    if sheet == 'JTS0921_Nearest':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LA Code'][x]).replace(' ',''))) or 'E1200' in str(clean_df['LA Code'][x]))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LA Code', 'Local Authority', 'Local Authority Name', 'Nearest station by public transport/walking', 'Average travel time by public transport/walking',
                            'Nearest station by car', 'Average travel time by car']
    
    if sheet == 'car' or sheet == 'PT':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LA Code'][x]).replace(' ',''))) or 'E1200' in str(clean_df['LA Code'][x]))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.replace(to_replace = '..', value = 240, inplace = True)
    
    if sheet == 'JTS0922':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['Ref'][x]).replace(' ','')) > 3 or not all(map(str.isalnum, str(clean_df['Ref'][x]).replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['Ref', 'Rail station name','People within 30 mins of the station by public transport', 'People within 60 mins of the station by public transport', 'People within 120 mins of the station by public transport',
                            'People within 30 mins of the station by car', 'People within 60 mins of the station by car', 'People within 120 mins of the station by car',
                            '%People within 20km and 30 mins of the station by public transport', '%People within 20km and 60 mins of the station by public transport', '%People within 20km and 120 mins of the station by public transport',
                            '%People within 20km and 30 mins of the station by car', '%People within 20km and 60 mins of the station by car', '%People within 20km and 120 mins of the station by car',
                            'Population within 20km']
        clean_df.replace(to_replace = '..', value = 240, inplace = True)
        
    if sheet == 'JTS0923':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LA Code'][x]).replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LA Code', 'Local Authority', 'Local Authority Name', 'Population', '%People within 30 mins to stations by public transport', '%People within 60 mins to stations by public transport', '%People within 120 mins to stations by public transport',
                            '%People within 30 mins to stations by car', '%People within 60 mins to stations by car', '%People within 120 mins to stations by car']
    
    if sheet == 'JTS0924':
        
        drop_idx = [x for x in clean_df.index if (len(str(clean_df['LA Code'][x]).replace(' ','')) > 9 or not all(map(str.isalnum, str(clean_df['LA Code'][x]).replace(' ',''))))]
        clean_df.drop(drop_idx, axis = 0, inplace = True)
        clean_df.columns = ['LA Code', 'Local Authority', 'Local Authority Name', 'Number of stations within 30  mins by public transport', 'Number of stations within 60  mins by public transport', 'Number of stations within 120  mins by public transport',
                            'Number of stations within 30  mins by car', 'Number of stations within 60  mins by car', 'Number of stations within 120  mins by car']
    
    # if sheet == 'JTS0925_Selected' or sheet == 'JTS0925_Summary' or sheet == 'JTS0926_Summary' or sheet == 'JTS0926_Selected':
        
    #     clean_df.replace(to_replace = '..', value = 240, inplace = True)
        
    if sheet == 'JTS0930_LA' or sheet == 'JTS0930_LSOA':
        
        clean_df.replace(to_replace = '--', value = -999, inplace = True)
        
    clean_df.drop_duplicates(inplace = True)
        
    clean_df.replace(to_replace = '..', value = 240, inplace = True)
    #clean_df = clean_df[~clean_df.isin(['..']).any(axis = 1)]
    
    rows_with_string =  [idx for idx, x in clean_df[clean_df.columns[len(clean_df.columns)-1]].iteritems() if any(str(c).isalpha() for c in str(x))]
    
    clean_df.drop(axis = 0, index = rows_with_string, inplace = True)
    
    
    for i in clean_df.columns:
        
        try:
            
            clean_df[i] = clean_df[i].astype('float')
            
        except ValueError:
            
            #print('Cannot convert values in column ' + i + ' to float.')
            # TODO: this needs looking at.
            pass
        
    
    return clean_df.reset_index(drop = True)

