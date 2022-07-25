import jtspy.plot as jtsplt
import jtspy.jts as jts
import jtspy.imd as imd

def jts_imd_lsoa(type_code, jts_spec, jts_variable, imd_domain, year = 2019, rank = True, level = 'lsoa', plot = False, sheet_jts09 = None):
    '''
    

    Parameters
    ----------
    type_code : string
        The jts type of data. Options are: jts01, jts02, jts03, jts04, jts05, jts09, jts10.
    jts_spec: string
        Trip spec of the data required.
    jts_variable : string
        The jts variable to use.
    imd_domain : string
        The short label of the domain of the IMD required. See dictionary in method _imd_dictionary
        for a description of the possible values.
    year : integer, optional
        The year for which the analysis is required. The default is 2019.
    rank : boolean, optional
        Whether rank or scores of IMD are required. The default is True.
    level : string, optional
        Spatial level at which IMD data is required. The default is 'lsoa'.
    plot : boolean, optional
        Whether a scatter plot of the data is wanted as output. The default is False.

    Returns
    -------
    merged_df : pandas dataframe
        A datafrmae containing the IMD and JTS data for all LSOAs.

    '''
    
    if level == 'lsoa':
        
        if type_code == 'jts05':
            
            jts_df = jts.get_jts(type_code = type_code, spec = jts_spec, sheet = year)[['LSOA_code', jts_variable]]
            
        elif type_code == 'jts09':
            
            jts_df = jts.get_jts(type_code = type_code, spec = jts_spec, sheet = sheet_jts09)[['LSOA Code', jts_variable]]
        
        imd_df = imd.get_imd(imd_domain, year, rank, level)
        
        
        if type_code == 'jts05':
            
            merged_df = imd_df.merge(jts_df, left_on = 'LSOA code (2011)', right_on = 'LSOA_code', how = 'inner')
            merged_df.drop(['LSOA_code'], axis = 1, inplace = True)
            
        elif type_code == 'jts09':
            
            merged_df = imd_df.merge(jts_df, left_on = 'LSOA code (2011)', right_on = 'LSOA Code', how = 'inner')
            merged_df.drop(['LSOA Code'], axis = 1, inplace = True)
            
        if plot:
            
            imd_dict = imd._imd_dictionary()
            
            if imd_domain == 'imd' and rank:
                
                i = imd_domain + '_rank_' + str(year)
                
            elif imd_domain != 'imd' and rank:
                
                i = imd_domain + '_rank'
                
            elif not rank:
                
                i = imd_domain + '_score'
                
            jtsplt.create_scatter_plot(merged_df, jts_variable, imd_dict[i])
            
    return merged_df

