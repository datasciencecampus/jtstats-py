import jtspy as jts
import pytest

def test_jts0101():
    
    jts_df = jts.get_jts(table_code = 'jts0101', sheet = 'JTS0101')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services']).all(), "Column names incorrect"
    
    assert len(jts_df) == 16, "Incorrect number of rows in data frame"
    
    assert jts_df['Average of 8 services'][0] == 17.0, "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][0] == 19.9, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][15] == 28.0, "Incorrect value in last row"
    
    assert jts_df['Town Centres'][15] == 36.6, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][len(jts_df)-2] == 10.3, "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0102():
    
    jts_df = jts.get_jts(type_code = 'jts01', spec = 'urban', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Area type 2', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres',
           'Average of 8 services 3']).all(), "Column names incorrect"
    
    assert len(jts_df) == 48, "Incorrect number of rows in data frame"
    
    assert jts_df['Average of 8 services 3'][0] == 13.6, "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][0] == 15.9, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services 3'][47] == 55.4, "Incorrect value in last row"
    
    assert jts_df['Town Centres'][47] == 79.5, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services 3'][len(jts_df)-2] == 22.2, "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df = jts.get_jts(type_code = 'jts01', spec = 'urban', sheet = '2014')
    assert (jts_df.columns.values ==['Year', 'Mode', 'Area type 1', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services2']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Average of 8 services2'][0] == 13.3, "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][0] == 15.9, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services2'][35] == 13.1, "Incorrect value in last row"
    
    assert jts_df['Town Centres'][35] == 15.9, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services2'][len(jts_df)-2] == 9.7, "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    

def test_jts0103():
    
    jts_df = jts.get_jts(type_code = 'jts01', spec = 'region', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services2']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Average of 8 services2'][0] == 17.3, "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][0] == 21.3, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services2'][35] == 35.0, "Incorrect value in last row"
    
    assert jts_df['Town Centres'][35] == 43.1, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services2'][len(jts_df)-2] == 31.1, "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df = jts.get_jts(type_code = 'jts01', spec = 'region', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services1']).all(), "Column names incorrect"
    
    assert len(jts_df) == 27, "Incorrect number of rows in data frame"
    
    assert jts_df['Average of 8 services1'][0] == 16.8, "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][0] == 21.5, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services1'][26] == 11.1, "Incorrect value in last row"
    
    assert jts_df['Town Centres'][26] == 12.4, "Incorrect value in last row"
    
    assert jts_df['Average of 8 services1'][len(jts_df)-2] == 10.8, "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"


def test_jts0104():
    
    jts_df = jts.get_jts(type_code = 'jts01', spec = 'local authority', sheet = '2019')
    assert (jts_df.columns.values == ['Region', 'LA Code', 'Local authority',
           'Public transport / Walking', 'Cycle', 'Car', 'Walking']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['Walking'][0] == 38.4, "Incorrect value in row 0"
    
    assert jts_df['Walking'][360] == 61.2, "Incorrect value in last row"
    
    assert jts_df['Walking'][len(jts_df)-2] == 32.7, "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df = jts.get_jts(type_code = 'jts01', spec = 'local authority', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA Code', 'Local authority',
           'Public transport / Walking', 'Cycle', 'Car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['Car'][0] == 10.8, "Incorrect value in row 0"
    
    assert jts_df['Car'][360] == 13.3, "Incorrect value in last row"
    
    assert jts_df['Car'][len(jts_df)-2] == 10.8, "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    
    
def test_jts0201():
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = '', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Journey time', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(7758940.29746628), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][31] == pytest.approx(82.2352167631255), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(73.2468856222009), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = '', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Journey time', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 24, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(7447916), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][23] == pytest.approx(99.9943404708448, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(99.9818895067032, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"


def test_jts0202():
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = 'urban', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Area type3', 'Journey time',
           'Places with 100-499 jobs', 'Places with 500-4999 jobs',
           'Places with 5000 or more jobs', 'Primary school',
           'Secondary school', 'Further Education', 'GP', 'Hospital',
           'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 64, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(7330251.647995), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][63] == pytest.approx(29.5522374134526), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(18.2585580350177), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = 'urban', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Area type3', 'Journey time',
           'Places with 100-499 jobs', 'Places with 500-4999 jobs',
           'Places with 5000 or more jobs', 'Primary school',
           'Secondary school', 'Further Education', 'GP', 'Hospital',
           'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 48, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(7040828), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][47] == pytest.approx(99.9713953700883, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(99.9002073770952, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    
def test_jts0203():
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = 'public transport', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Users with access', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 71, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(316331.079627991), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][70] == pytest.approx(96.7561119595649, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(98.626528290775, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = 'public transport', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Users with access', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 71, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(281579), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][70] == pytest.approx(97.6477390860384, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(99.2042616261516, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0204():
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = 'cycle', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Users with access', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 71, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(514717.499008179), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][70] == pytest.approx(98.2005149752097, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(99.63990204083775, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

    jts_df = jts.get_jts(type_code = 'jts02', spec = 'cycle', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Users with access', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 71, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(492920), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][70] == pytest.approx(98.2334316664162, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(99.6457889223337, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    
def test_jts0205():
    
    jts_df = jts.get_jts(type_code = 'jts02', spec = 'car', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Users with access', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 71, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(979307.819965363), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][70] == pytest.approx(99.9607508268787, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(100), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

    jts_df = jts.get_jts(type_code = 'jts02', spec = 'car', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Users with access', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 71, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(909662), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][70] == pytest.approx(99.9560620719897, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(100), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0206():
    
    jts_df = jts.get_jts(table_code = 'jts0206', sheet = 2019)
    assert (jts_df.columns.values == ['Year', 'Users with access', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 71, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(196720.171875), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][70] == pytest.approx(73.7644947482606, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(81.3167546552867, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

   
def test_jts0301():
    
    jts_df = jts.get_jts(type_code = 'jts03', spec = '', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Places with 100-499 jobs', 'Places with 500-4999 jobs',
           'Places with 5000 or more jobs', 'Primary school', 'Secondary school',
           'Further Education', 'GP', 'Hospital', 'Food store', 'Town Centres',
           'Average of 8 services']).all(), "Column names incorrect"
    
    assert len(jts_df) == 19, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.385434724405152, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][18] == pytest.approx(2.46897038990381, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(9.90007527135375, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average of 8 services'][0] == pytest.approx(1.66585348577982, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Average of 8 services'][18] == pytest.approx(5.56188950097338, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][len(jts_df)-2] == pytest.approx(9.7298212697627, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

    jts_df = jts.get_jts(type_code = 'jts03', spec = '', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 15, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.399544738419505, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][14] == pytest.approx(9.94033534204361, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(6.64566869668695, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"


def test_jts0302():
    
    jts_df = jts.get_jts(type_code = 'jts03', spec = 'urban', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Area type 2', 'Journey time',
           'Places with 100-499 jobs', 'Places with 500-4999 jobs',
           'Places with 5000 or more jobs', 'Primary school',
           'Secondary school', 'Further Education', 'GP', 'Hospital',
           'Food store', 'Town Centres', 'Average of 8 services']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.446815619423326, rel = 0.5), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][31] == pytest.approx(0.327117711680803, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(0.189316950617393, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average of 8 services'][0] == pytest.approx(1.91332903986159, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Average of 8 services'][31] == pytest.approx(1.84232811213562, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][len(jts_df)-2] == pytest.approx(1.1188240829406, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

    jts_df = jts.get_jts(type_code = 'jts03', spec = 'urban', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Mode', 'Area type 2', 'Journey time',
           'Places with 100-499 jobs', 'Places with 500-4999 jobs',
           'Places with 5000 or more jobs', 'Primary school',
           'Secondary school', 'Further Education', 'GP', 'Hospital',
           'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 24, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.461780999528524, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][23] == pytest.approx(9.83351587660506, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(9.12814537675404, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"


def test_jts0303():
    
    jts_df = jts.get_jts(type_code = 'jts03', spec = 'public transport', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Distance (minutes)', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.283097284241742, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][35] == pytest.approx(5.54628912957426, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(7.67197846960107, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average of 8 services'][0] == pytest.approx(1.58848924519224, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Average of 8 services'][35] == pytest.approx(7.18357224555022, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][len(jts_df)-2] == pytest.approx(8.06550782180284, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

    jts_df = jts.get_jts(type_code = 'jts03', spec = 'public transport', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Distance (minutes)', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.263466493591932, rel = 0.5), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][35] == pytest.approx(5.69555805122987, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(7.75290796744769, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"

def test_jts0304():
    
    jts_df = jts.get_jts(type_code = 'jts03', spec = 'cycle', sheet = '2019')
    assert (jts_df.columns.values ==['Year', 'Distance (minutes)', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.523147840188616, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][35] == pytest.approx(4.54213988530025, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(5.98309494542215, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average of 8 services'][0] == pytest.approx(2.86480978309329, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Average of 8 services'][35] == pytest.approx(7.02445905394424, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][len(jts_df)-2] == pytest.approx(7.77884987168006, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

    jts_df = jts.get_jts(type_code = 'jts03', spec = 'cycle', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Distance (minutes)', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.518445192312794, rel = 0.5), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][35] == pytest.approx(4.58979374657833, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(5.98686654284956, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"


def test_jts0305():
    
    jts_df = jts.get_jts(type_code = 'jts03', spec = 'car', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Distance (minutes)', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(1.65977142944014, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][35] == pytest.approx(9.76273367893153, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(9.9061406003779, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average of 8 services'][0] == pytest.approx(5.51714737838236, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Average of 8 services'][35] == pytest.approx(9.17872117311965, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][len(jts_df)-2] == pytest.approx(9.65898190003407, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

    jts_df = jts.get_jts(type_code = 'jts03', spec = 'car', sheet = '2014')
    assert (jts_df.columns.values == ['Year', 'Distance (minutes)', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(1.44792637485653, rel = 0.5), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][35] == pytest.approx(9.84734645671367, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(9.91080879863862, rel = 0.01), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"


def test_jts0306():
    
    jts_df = jts.get_jts(table_code = 'jts0306', sheet = '2019')
    assert (jts_df.columns.values == ['Year', 'Distance (minutes)', 'Region', 'Places with 100-499 jobs',
           'Places with 500-4999 jobs', 'Places with 5000 or more jobs',
           'Primary school', 'Secondary school', 'Further Education', 'GP',
           'Hospital', 'Food store', 'Town Centres', 'Average of 8 services']).all(), "Column names incorrect"
    
    assert len(jts_df) == 36, "Incorrect number of rows in data frame"
    
    assert jts_df['Town Centres'][0] == pytest.approx(0.169280310483441, rel = 0.5), "Incorrect value in row 0"
    
    assert jts_df['Town Centres'][35] == pytest.approx(1.4614649338839, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Town Centres'][len(jts_df)-2] == pytest.approx(1.48504519418634, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average of 8 services'][0] == pytest.approx(1.12564046789827, rel = 0.1), "Incorrect value in row 0"
    
    assert jts_df['Average of 8 services'][35] == pytest.approx(4.18808461653862, rel = 0.1), "Incorrect value in last row"
    
    assert jts_df['Average of 8 services'][len(jts_df)-2] == pytest.approx(4.74580080239533, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0401():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'employment', sheet = '2019')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'Empl_pop', '100EmpPTt',
           '100EmpPT15n', '100EmpPT30n', '100EmpPT45n', '100EmpPT60n',
           '100EmpPT15pct', '100EmpPT30pct', '100EmpPT45pct', '100EmpPT60pct',
           '100EmpCyct', '100EmpCyc15n', '100EmpCyc30n', '100EmpCyc45n',
           '100EmpCyc60n', '100EmpCyc15pct', '100EmpCyc30pct',
           '100EmpCyc45pct', '100EmpCyc60pct', '100EmpCart', '100EmpCar15n',
           '100EmpCar30n', '100EmpCar45n', '100EmpCar60n', '100EmpCar15pct',
           '100EmpCar30pct', '100EmpCar45pct', '100EmpCar60pct',
           '100EmpWalkt', '100EmpWalk15n', '100EmpWalk30n', '100EmpWalk45n',
           '100EmpWalk60n', '100EmpWalk15pct', '100EmpWalk30pct',
           '100EmpWalk45pct', '100EmpWalk60pct', '500EmpPTt', '500EmpPT15n',
           '500EmpPT30n', '500EmpPT45n', '500EmpPT60n', '500EmpPT15pct',
           '500EmpPT30pct', '500EmpPT45pct', '500EmpPT60pct', '500EmpCyct',
           '500EmpCyc15n', '500EmpCyc30n', '500EmpCyc45n', '500EmpCyc60n',
           '500EmpCyc15pct', '500EmpCyc30pct', '500EmpCyc45pct',
           '500EmpCyc60pct', '500EmpCart', '500EmpCar15n', '500EmpCar30n',
           '500EmpCar45n', '500EmpCar60n', '500EmpCar15pct', '500EmpCar30pct',
           '500EmpCar45pct', '500EmpCar60pct', '500EmpWalkt', '500EmpWalk15n',
           '500EmpWalk30n', '500EmpWalk45n', '500EmpWalk60n',
           '500EmpWalk15pct', '500EmpWalk30pct', '500EmpWalk45pct',
           '500EmpWalk60pct', '5000EmpPTt', '5000EmpPT15n', '5000EmpPT30n',
           '5000EmpPT45n', '5000EmpPT60n', '5000EmpPT15pct', '5000EmpPT30pct',
           '5000EmpPT45pct', '5000EmpPT60pct', '5000EmpCyct', '5000EmpCyc15n',
           '5000EmpCyc30n', '5000EmpCyc45n', '5000EmpCyc60n',
           '5000EmpCyc15pct', '5000EmpCyc30pct', '5000EmpCyc45pct',
           '5000EmpCyc60pct', '5000EmpCart', '5000EmpCar15n', '5000EmpCar30n',
           '5000EmpCar45n', '5000EmpCar60n', '5000EmpCar15pct',
           '5000EmpCar30pct', '5000EmpCar45pct', '5000EmpCar60pct',
           '5000EmpWalkt', '5000EmpWalk15n', '5000EmpWalk30n',
           '5000EmpWalk45n', '5000EmpWalk60n', '5000EmpWalk15pct',
           '5000EmpWalk30pct', '5000EmpWalk45pct', '5000EmpWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['5000EmpWalk60pct'][0] == pytest.approx(27.6582119602248, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['5000EmpWalk60pct'][360] == pytest.approx(0), "Incorrect value in last row"
    
    assert jts_df['5000EmpWalk60pct'][len(jts_df)-2] == pytest.approx(61.7922362332662, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Empl_pop'][0] == pytest.approx(390394), "Incorrect value in row 0"
    
    assert jts_df['Empl_pop'][360] == pytest.approx(24610), "Incorrect value in last row"
    
    assert jts_df['Empl_pop'][len(jts_df)-2] == pytest.approx(84933), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'employment', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'Empl_pop', '100EmpPTt',
           '100EmpPT15n', '100EmpPT30n', '100EmpPT45n', '100EmpPT60n',
           '100EmpPT15pct', '100EmpPT30pct', '100EmpPT45pct', '100EmpPT60pct',
           '100EmpCyct', '100EmpCyc15n', '100EmpCyc30n', '100EmpCyc45n',
           '100EmpCyc60n', '100EmpCyc15pct', '100EmpCyc30pct',
           '100EmpCyc45pct', '100EmpCyc60pct', '100EmpCart', '100EmpCar15n',
           '100EmpCar30n', '100EmpCar45n', '100EmpCar60n', '100EmpCar15pct',
           '100EmpCar30pct', '100EmpCar45pct', '100EmpCar60pct', '500EmpPTt',
           '500EmpPT15n', '500EmpPT30n', '500EmpPT45n', '500EmpPT60n',
           '500EmpPT15pct', '500EmpPT30pct', '500EmpPT45pct', '500EmpPT60pct',
           '500EmpCyct', '500EmpCyc15n', '500EmpCyc30n', '500EmpCyc45n',
           '500EmpCyc60n', '500EmpCyc15pct', '500EmpCyc30pct',
           '500EmpCyc45pct', '500EmpCyc60pct', '500EmpCart', '500EmpCar15n',
           '500EmpCar30n', '500EmpCar45n', '500EmpCar60n', '500EmpCar15pct',
           '500EmpCar30pct', '500EmpCar45pct', '500EmpCar60pct', '5000EmpPTt',
           '5000EmpPT15n', '5000EmpPT30n', '5000EmpPT45n', '5000EmpPT60n',
           '5000EmpPT15pct', '5000EmpPT30pct', '5000EmpPT45pct',
           '5000EmpPT60pct', '5000EmpCyct', '5000EmpCyc15n', '5000EmpCyc30n',
           '5000EmpCyc45n', '5000EmpCyc60n', '5000EmpCyc15pct',
           '5000EmpCyc30pct', '5000EmpCyc45pct', '5000EmpCyc60pct',
           '5000EmpCart', '5000EmpCar15n', '5000EmpCar30n', '5000EmpCar45n',
           '5000EmpCar60n', '5000EmpCar15pct', '5000EmpCar30pct',
           '5000EmpCar45pct', '5000EmpCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['5000EmpCar60pct'][0] == pytest.approx(99.90523547942, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['5000EmpCar60pct'][360] == pytest.approx(97.0137108914114, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['5000EmpCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Empl_pop'][0] == pytest.approx(384110), "Incorrect value in row 0"
    
    assert jts_df['Empl_pop'][360] == pytest.approx(24579), "Incorrect value in last row"
    
    assert jts_df['Empl_pop'][len(jts_df)-2] == pytest.approx(80518), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0402():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'primary', sheet = '2019')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'PS_pop', 'PSPTt', 'PSPT15n',
           'PSPT30n', 'PSPT45n', 'PSPT60n', 'PSPT15pct', 'PSPT30pct',
           'PSPT45pct', 'PSPT60pct', 'PSCyct', 'PSCyc15n', 'PSCyc30n',
           'PSCyc45n', 'PSCyc60n', 'PSCyc15pct', 'PSCyc30pct', 'PSCyc45pct',
           'PSCyc60pct', 'PSCart', 'PSCar15n', 'PSCar30n', 'PSCar45n',
           'PSCar60n', 'PSCar15pct', 'PSCar30pct', 'PSCar45pct', 'PSCar60pct',
           'PSWalkt', 'PSWalk15n', 'PSWalk30n', 'PSWalk45n', 'PSWalk60n',
           'PSWalk15pct', 'PSWalk30pct', 'PSWalk45pct', 'PSWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['PSWalk60pct'][0] == pytest.approx(99.6643829917067, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['PSWalk60pct'][360] == pytest.approx(92.8424304840371, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['PSWalk60pct'][len(jts_df)-2] == pytest.approx(99.670549476409, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['PS_pop'][0] == pytest.approx(36053), "Incorrect value in row 0"
    
    assert jts_df['PS_pop'][360] == pytest.approx(1942), "Incorrect value in last row"
    
    assert jts_df['PS_pop'][len(jts_df)-2] == pytest.approx(8499), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'primary', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'PS_pop', 'PSPTt', 'PSPT15n',
           'PSPT30n', 'PSPT45n', 'PSPT60n', 'PSPT15pct', 'PSPT30pct',
           'PSPT45pct', 'PSPT60pct', 'PSCyct', 'PSCyc15n', 'PSCyc30n',
           'PSCyc45n', 'PSCyc60n', 'PSCyc15pct', 'PSCyc30pct', 'PSCyc45pct',
           'PSCyc60pct', 'PSCart', 'PSCar15n', 'PSCar30n', 'PSCar45n',
           'PSCar60n', 'PSCar15pct', 'PSCar30pct', 'PSCar45pct', 'PSCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['PSCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['PSCar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['PSCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['PS_pop'][0] == pytest.approx(32661), "Incorrect value in row 0"
    
    assert jts_df['PS_pop'][360] == pytest.approx(1688), "Incorrect value in last row"
    
    assert jts_df['PS_pop'][len(jts_df)-2] == pytest.approx(7388), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    

def test_jts0403():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'secondary', sheet = '2019')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'SS_pop', 'SSPTt', 'SSPT15n',
           'SSPT30n', 'SSPT45n', 'SSPT60n', 'SSPT15pct', 'SSPT30pct',
           'SSPT45pct', 'SSPT60pct', 'SSCyct', 'SSCyc15n', 'SSCyc30n',
           'SSCyc45n', 'SSCyc60n', 'SSCyc15pct', 'SSCyc30pct', 'SSCyc45pct',
           'SSCyc60pct', 'SSCart', 'SSCar15n', 'SSCar30n', 'SSCar45n',
           'SSCar60n', 'SSCar15pct', 'SSCar30pct', 'SSCar45pct', 'SSCar60pct',
           'SSWalkt', 'SSWalk15n', 'SSWalk30n', 'SSWalk45n', 'SSWalk60n',
           'SSWalk15pct', 'SSWalk30pct', 'SSWalk45pct', 'SSWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['SSWalk60pct'][0] == pytest.approx(86.0711055451193, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['SSWalk60pct'][360] == pytest.approx(38.025350233489, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['SSWalk60pct'][len(jts_df)-2] == pytest.approx(82.9042522418282, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['SS_pop'][0] == pytest.approx(28746), "Incorrect value in row 0"
    
    assert jts_df['SS_pop'][360] == pytest.approx(1499), "Incorrect value in last row"
    
    assert jts_df['SS_pop'][len(jts_df)-2] == pytest.approx(6914), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'secondary', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'SS_pop', 'SSPTt', 'SSPT15n',
           'SSPT30n', 'SSPT45n', 'SSPT60n', 'SSPT15pct', 'SSPT30pct',
           'SSPT45pct', 'SSPT60pct', 'SSCyct', 'SSCyc15n', 'SSCyc30n',
           'SSCyc45n', 'SSCyc60n', 'SSCyc15pct', 'SSCyc30pct', 'SSCyc45pct',
           'SSCyc60pct', 'SSCart', 'SSCar15n', 'SSCar30n', 'SSCar45n',
           'SSCar60n', 'SSCar15pct', 'SSCar30pct', 'SSCar45pct', 'SSCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['SSCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['SSCar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['SSCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['SS_pop'][0] == pytest.approx(26874), "Incorrect value in row 0"
    
    assert jts_df['SS_pop'][360] == pytest.approx(1559), "Incorrect value in last row"
    
    assert jts_df['SS_pop'][len(jts_df)-2] == pytest.approx(6304), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0404():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'further', sheet = '2019')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'FE_pop', 'FEPTt', 'FEPT15n',
           'FEPT30n', 'FEPT45n', 'FEPT60n', 'FEPT15pct', 'FEPT30pct',
           'FEPT45pct', 'FEPT60pct', 'FECyct', 'FECyc15n', 'FECyc30n',
           'FECyc45n', 'FECyc60n', 'FECyc15pct', 'FECyc30pct', 'FECyc45pct',
           'FECyc60pct', 'FECart', 'FECar15n', 'FECar30n', 'FECar45n',
           'FECar60n', 'FECar15pct', 'FECar30pct', 'FECar45pct', 'FECar60pct',
           'FEWalkt', 'FEWalk15n', 'FEWalk30n', 'FEWalk45n', 'FEWalk60n',
           'FEWalk15pct', 'FEWalk30pct', 'FEWalk45pct', 'FEWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['FEWalk60pct'][0] == pytest.approx(70.1062343928556, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FEWalk60pct'][360] == pytest.approx(40.6749555950266, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FEWalk60pct'][len(jts_df)-2] == pytest.approx(66.5980230642504, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['FE_pop'][0] == pytest.approx(23627), "Incorrect value in row 0"
    
    assert jts_df['FE_pop'][360] == pytest.approx(1126), "Incorrect value in last row"
    
    assert jts_df['FE_pop'][len(jts_df)-2] == pytest.approx(4856), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'further', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'FE_pop', 'FEPTt', 'FEPT15n',
           'FEPT30n', 'FEPT45n', 'FEPT60n', 'FEPT15pct', 'FEPT30pct',
           'FEPT45pct', 'FEPT60pct', 'FECyct', 'FECyc15n', 'FECyc30n',
           'FECyc45n', 'FECyc60n', 'FECyc15pct', 'FECyc30pct', 'FECyc45pct',
           'FECyc60pct', 'FECart', 'FECar15n', 'FECar30n', 'FECar45n',
           'FECar60n', 'FECar15pct', 'FECar30pct', 'FECar45pct', 'FECar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['FECar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FECar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FECar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['FE_pop'][0] == pytest.approx(25789), "Incorrect value in row 0"
    
    assert jts_df['FE_pop'][360] == pytest.approx(1373), "Incorrect value in last row"
    
    assert jts_df['FE_pop'][len(jts_df)-2] == pytest.approx(5582), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0405():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'gp', sheet = '2019')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'GP_pop', 'GPPTt', 'GPPT15n',
           'GPPT30n', 'GPPT45n', 'GPPT60n', 'GPPT15pct', 'GPPT30pct',
           'GPPT45pct', 'GPPT60pct', 'GPCyct', 'GPCyc15n', 'GPCyc30n',
           'GPCyc45n', 'GPCyc60n', 'GPCyc15pct', 'GPCyc30pct', 'GPCyc45pct',
           'GPCyc60pct', 'GPCart', 'GPCar15n', 'GPCar30n', 'GPCar45n',
           'GPCar60n', 'GPCar15pct', 'GPCar30pct', 'GPCar45pct', 'GPCar60pct',
           'GPWalkt', 'GPWalk15n', 'GPWalk30n', 'GPWalk45n', 'GPWalk60n',
           'GPWalk15pct', 'GPWalk30pct', 'GPWalk45pct', 'GPWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['GPWalk60pct'][0] == pytest.approx(94.9960455962536, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['GPWalk60pct'][360] == pytest.approx(71.4971516657928, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['GPWalk60pct'][len(jts_df)-2] == pytest.approx(91.5257850601125, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['GP_pop'][0] == pytest.approx(234112.999137878), "Incorrect value in row 0"
    
    assert jts_df['GP_pop'][360] == pytest.approx(16149.0000762939), "Incorrect value in last row"
    
    assert jts_df['GP_pop'][len(jts_df)-2] == pytest.approx(51878.9998893738), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'gp', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'GP_pop', 'GPPTt', 'GPPT15n',
           'GPPT30n', 'GPPT45n', 'GPPT60n', 'GPPT15pct', 'GPPT30pct',
           'GPPT45pct', 'GPPT60pct', 'GPCyct', 'GPCyc15n', 'GPCyc30n',
           'GPCyc45n', 'GPCyc60n', 'GPCyc15pct', 'GPCyc30pct', 'GPCyc45pct',
           'GPCyc60pct', 'GPCart', 'GPCar15n', 'GPCar30n', 'GPCar45n',
           'GPCar60n', 'GPCar15pct', 'GPCar30pct', 'GPCar45pct', 'GPCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['GPCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['GPCar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['GPCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['GP_pop'][0] == pytest.approx(225877), "Incorrect value in row 0"
    
    assert jts_df['GP_pop'][360] == pytest.approx(15384), "Incorrect value in last row"
    
    assert jts_df['GP_pop'][len(jts_df)-2] == pytest.approx(46504), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0406():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'hospital', sheet = '2019')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'Hosp_pop', 'HospPTt', 'HospPT15n',
           'HospPT30n', 'HospPT45n', 'HospPT60n', 'HospPT15pct',
           'HospPT30pct', 'HospPT45pct', 'HospPT60pct', 'HospCyct',
           'HospCyc15n', 'HospCyc30n', 'HospCyc45n', 'HospCyc60n',
           'HospCyc15pct', 'HospCyc30pct', 'HospCyc45pct', 'HospCyc60pct',
           'HospCart', 'HospCar15n', 'HospCar30n', 'HospCar45n', 'HospCar60n',
           'HospCar15pct', 'HospCar30pct', 'HospCar45pct', 'HospCar60pct',
           'HospWalkt', 'HospWalk15n', 'HospWalk30n', 'HospWalk45n',
           'HospWalk60n', 'HospWalk15pct', 'HospWalk30pct', 'HospWalk45pct',
           'HospWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['HospWalk60pct'][0] == pytest.approx(9.01104991399226, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['HospWalk60pct'][360] == pytest.approx(0, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['HospWalk60pct'][len(jts_df)-2] == pytest.approx(58.4411708370819, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Hosp_pop'][0] == pytest.approx(234112.999137878), "Incorrect value in row 0"
    
    assert jts_df['Hosp_pop'][360] == pytest.approx(16149.0000762939), "Incorrect value in last row"
    
    assert jts_df['Hosp_pop'][len(jts_df)-2] == pytest.approx(51878.9998893738), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'hospital', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'Hosp_pop', 'HospPTt', 'HospPT15n',
           'HospPT30n', 'HospPT45n', 'HospPT60n', 'HospPT15pct',
           'HospPT30pct', 'HospPT45pct', 'HospPT60pct', 'HospCyct',
           'HospCyc15n', 'HospCyc30n', 'HospCyc45n', 'HospCyc60n',
           'HospCyc15pct', 'HospCyc30pct', 'HospCyc45pct', 'HospCyc60pct',
           'HospCart', 'HospCar15n', 'HospCar30n', 'HospCar45n', 'HospCar60n',
           'HospCar15pct', 'HospCar30pct', 'HospCar45pct', 'HospCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['HospCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['HospCar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['HospCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Hosp_pop'][0] == pytest.approx(225877), "Incorrect value in row 0"
    
    assert jts_df['Hosp_pop'][360] == pytest.approx(15384), "Incorrect value in last row"
    
    assert jts_df['Hosp_pop'][len(jts_df)-2] == pytest.approx(46504), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0407():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'food', sheet = '2019')
    assert (jts_df.columns.values ==['Region', 'LA_Code', 'LA_Name', 'Food_pop', 'FoodPTt', 'FoodPT15n',
           'FoodPT30n', 'FoodPT45n', 'FoodPT60n', 'FoodPT15pct',
           'FoodPT30pct', 'FoodPT45pct', 'FoodPT60pct', 'FoodCyct',
           'FoodCyc15n', 'FoodCyc30n', 'FoodCyc45n', 'FoodCyc60n',
           'FoodCyc15pct', 'FoodCyc30pct', 'FoodCyc45pct', 'FoodCyc60pct',
           'FoodCart', 'FoodCar15n', 'FoodCar30n', 'FoodCar45n', 'FoodCar60n',
           'FoodCar15pct', 'FoodCar30pct', 'FoodCar45pct', 'FoodCar60pct',
           'FoodWalkt', 'FoodWalk15n', 'FoodWalk30n', 'FoodWalk45n',
           'FoodWalk60n', 'FoodWalk15pct', 'FoodWalk30pct', 'FoodWalk45pct',
           'FoodWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['FoodWalk60pct'][0] == pytest.approx(98.4852749890377, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FoodWalk60pct'][360] == pytest.approx(82.5961721884521, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FoodWalk60pct'][len(jts_df)-2] == pytest.approx(95.6168588609437, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Food_pop'][0] == pytest.approx(234112.999137878), "Incorrect value in row 0"
    
    assert jts_df['Food_pop'][360] == pytest.approx(16149.0000762939), "Incorrect value in last row"
    
    assert jts_df['Food_pop'][len(jts_df)-2] == pytest.approx(51878.9998893738), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'food', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'Food_pop', 'FoodPTt', 'FoodPT15n',
           'FoodPT30n', 'FoodPT45n', 'FoodPT60n', 'FoodPT15pct',
           'FoodPT30pct', 'FoodPT45pct', 'FoodPT60pct', 'FoodCyct',
           'FoodCyc15n', 'FoodCyc30n', 'FoodCyc45n', 'FoodCyc60n',
           'FoodCyc15pct', 'FoodCyc30pct', 'FoodCyc45pct', 'FoodCyc60pct',
           'FoodCart', 'FoodCar15n', 'FoodCar30n', 'FoodCar45n', 'FoodCar60n',
           'FoodCar15pct', 'FoodCar30pct', 'FoodCar45pct', 'FoodCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['FoodCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FoodCar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FoodCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Food_pop'][0] == pytest.approx(225877), "Incorrect value in row 0"
    
    assert jts_df['Food_pop'][360] == pytest.approx(15384), "Incorrect value in last row"
    
    assert jts_df['Food_pop'][len(jts_df)-2] == pytest.approx(46504), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0408():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'town', sheet = '2019')
    assert (jts_df.columns.values ==['Region', 'LA_Code', 'LA_Name', 'Town_pop', 'TownPTt', 'TownPT15n',
           'TownPT30n', 'TownPT45n', 'TownPT60n', 'TownPT15pct',
           'TownPT30pct', 'TownPT45pct', 'TownPT60pct', 'TownCyct',
           'TownCyc15n', 'TownCyc30n', 'TownCyc45n', 'TownCyc60n',
           'TownCyc15pct', 'TownCyc30pct', 'TownCyc45pct', 'TownCyc60pct',
           'TownCart', 'TownCar15n', 'TownCar30n', 'TownCar45n', 'TownCar60n',
           'TownCar15pct', 'TownCar30pct', 'TownCar45pct', 'TownCar60pct',
           'TownWalkt', 'TownWalk15n', 'TownWalk30n', 'TownWalk45n',
           'TownWalk60n', 'TownWalk15pct', 'TownWalk30pct', 'TownWalk45pct',
           'TownWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['TownWalk60pct'][0] == pytest.approx(65.4803554893168, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['TownWalk60pct'][360] == pytest.approx(36.2030340576407, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['TownWalk60pct'][len(jts_df)-2] == pytest.approx(76.8009038970301, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Town_pop'][0] == pytest.approx(234112.999137878), "Incorrect value in row 0"
    
    assert jts_df['Town_pop'][360] == pytest.approx(16149.0000762939), "Incorrect value in last row"
    
    assert jts_df['Town_pop'][len(jts_df)-2] == pytest.approx(51878.9998893738), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'town', sheet = '2014')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'Town_pop', 'TownPTt', 'TownPT15n',
           'TownPT30n', 'TownPT45n', 'TownPT60n', 'TownPT15pct',
           'TownPT30pct', 'TownPT45pct', 'TownPT60pct', 'TownCyct',
           'TownCyc15n', 'TownCyc30n', 'TownCyc45n', 'TownCyc60n',
           'TownCyc15pct', 'TownCyc30pct', 'TownCyc45pct', 'TownCyc60pct',
           'TownCart', 'TownCar15n', 'TownCar30n', 'TownCar45n', 'TownCar60n',
           'TownCar15pct', 'TownCar30pct', 'TownCar45pct', 'TownCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['TownCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['TownCar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['TownCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Town_pop'][0] == pytest.approx(225877), "Incorrect value in row 0"
    
    assert jts_df['Town_pop'][360] == pytest.approx(15384), "Incorrect value in last row"
    
    assert jts_df['Town_pop'][len(jts_df)-2] == pytest.approx(46504), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0409():
    
    jts_df =jts.get_jts(type_code = 'jts04', spec = 'pharmacy', sheet = '2015')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name', 'Ph_pop', 'PhCyct', 'PhCyc15n',
           'PhCyc30n', 'PhCyc45n', 'PhCyc60n', 'PhCyc15pct', 'PhCyc30pct',
           'PhCyc45pct', 'PhCyc60pct', 'PhCart', 'PhCar15n', 'PhCar30n',
           'PhCar45n', 'PhCar60n', 'PhCar15pct', 'PhCar30pct', 'PhCar45pct',
           'PhCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['PhCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['PhCar60pct'][360] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['PhCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Ph_pop'][0] == pytest.approx(227875), "Incorrect value in row 0"
    
    assert jts_df['Ph_pop'][360] == pytest.approx(16008), "Incorrect value in last row"
    
    assert jts_df['Ph_pop'][len(jts_df)-2] == pytest.approx(49005), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
   
def test_jts0501():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'employment', sheet = '2019')
    assert (jts_df.columns.values ==['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Empl_pop',
           '100EmpPTt', '100EmpPT15n', '100EmpPT30n', '100EmpPT45n',
           '100EmpPT60n', '100EmpPT15pct', '100EmpPT30pct', '100EmpPT45pct',
           '100EmpPT60pct', '100EmpCyct', '100EmpCyc15n', '100EmpCyc30n',
           '100EmpCyc45n', '100EmpCyc60n', '100EmpCyc15pct', '100EmpCyc30pct',
           '100EmpCyc45pct', '100EmpCyc60pct', '100EmpCart', '100EmpCar15n',
           '100EmpCar30n', '100EmpCar45n', '100EmpCar60n', '100EmpCar15pct',
           '100EmpCar30pct', '100EmpCar45pct', '100EmpCar60pct',
           '100EmpWalkt', '100EmpWalk15n', '100EmpWalk30n', '100EmpWalk45n',
           '100EmpWalk60n', '100EmpWalk15pct', '100EmpWalk30pct',
           '100EmpWalk45pct', '100EmpWalk60pct', '500EmpPTt', '500EmpPT15n',
           '500EmpPT30n', '500EmpPT45n', '500EmpPT60n', '500EmpPT15pct',
           '500EmpPT30pct', '500EmpPT45pct', '500EmpPT60pct', '500EmpCyct',
           '500EmpCyc15n', '500EmpCyc30n', '500EmpCyc45n', '500EmpCyc60n',
           '500EmpCyc15pct', '500EmpCyc30pct', '500EmpCyc45pct',
           '500EmpCyc60pct', '500EmpCart', '500EmpCar15n', '500EmpCar30n',
           '500EmpCar45n', '500EmpCar60n', '500EmpCar15pct', '500EmpCar30pct',
           '500EmpCar45pct', '500EmpCar60pct', '500EmpWalkt', '500EmpWalk15n',
           '500EmpWalk30n', '500EmpWalk45n', '500EmpWalk60n',
           '500EmpWalk15pct', '500EmpWalk30pct', '500EmpWalk45pct',
           '500EmpWalk60pct', '5000EmpPTt', '5000EmpPT15n', '5000EmpPT30n',
           '5000EmpPT45n', '5000EmpPT60n', '5000EmpPT15pct', '5000EmpPT30pct',
           '5000EmpPT45pct', '5000EmpPT60pct', '5000EmpCyct', '5000EmpCyc15n',
           '5000EmpCyc30n', '5000EmpCyc45n', '5000EmpCyc60n',
           '5000EmpCyc15pct', '5000EmpCyc30pct', '5000EmpCyc45pct',
           '5000EmpCyc60pct', '5000EmpCart', '5000EmpCar15n', '5000EmpCar30n',
           '5000EmpCar45n', '5000EmpCar60n', '5000EmpCar15pct',
           '5000EmpCar30pct', '5000EmpCar45pct', '5000EmpCar60pct',
           '5000EmpWalkt', '5000EmpWalk15n', '5000EmpWalk30n',
           '5000EmpWalk45n', '5000EmpWalk60n', '5000EmpWalk15pct',
           '5000EmpWalk30pct', '5000EmpWalk45pct', '5000EmpWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['5000EmpWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['5000EmpWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['5000EmpWalk60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Empl_pop'][0] == pytest.approx(1189), "Incorrect value in row 0"
    
    assert jts_df['Empl_pop'][32843] == pytest.approx(1175), "Incorrect value in last row"
    
    assert jts_df['Empl_pop'][len(jts_df)-2] == pytest.approx(765), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'employment', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Empl_pop',
           '100EmpPTt', '100EmpPT15n', '100EmpPT30n', '100EmpPT45n',
           '100EmpPT60n', '100EmpPT15pct', '100EmpPT30pct', '100EmpPT45pct',
           '100EmpPT60pct', '100EmpCyct', '100EmpCyc15n', '100EmpCyc30n',
           '100EmpCyc45n', '100EmpCyc60n', '100EmpCyc15pct', '100EmpCyc30pct',
           '100EmpCyc45pct', '100EmpCyc60pct', '100EmpCart', '100EmpCar15n',
           '100EmpCar30n', '100EmpCar45n', '100EmpCar60n', '100EmpCar15pct',
           '100EmpCar30pct', '100EmpCar45pct', '100EmpCar60pct', '500EmpPTt',
           '500EmpPT15n', '500EmpPT30n', '500EmpPT45n', '500EmpPT60n',
           '500EmpPT15pct', '500EmpPT30pct', '500EmpPT45pct', '500EmpPT60pct',
           '500EmpCyct', '500EmpCyc15n', '500EmpCyc30n', '500EmpCyc45n',
           '500EmpCyc60n', '500EmpCyc15pct', '500EmpCyc30pct',
           '500EmpCyc45pct', '500EmpCyc60pct', '500EmpCart', '500EmpCar15n',
           '500EmpCar30n', '500EmpCar45n', '500EmpCar60n', '500EmpCar15pct',
           '500EmpCar30pct', '500EmpCar45pct', '500EmpCar60pct', '5000EmpPTt',
           '5000EmpPT15n', '5000EmpPT30n', '5000EmpPT45n', '5000EmpPT60n',
           '5000EmpPT15pct', '5000EmpPT30pct', '5000EmpPT45pct',
           '5000EmpPT60pct', '5000EmpCyct', '5000EmpCyc15n', '5000EmpCyc30n',
           '5000EmpCyc45n', '5000EmpCyc60n', '5000EmpCyc15pct',
           '5000EmpCyc30pct', '5000EmpCyc45pct', '5000EmpCyc60pct',
           '5000EmpCart', '5000EmpCar15n', '5000EmpCar30n', '5000EmpCar45n',
           '5000EmpCar60n', '5000EmpCar15pct', '5000EmpCar30pct',
           '5000EmpCar45pct', '5000EmpCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['5000EmpCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['5000EmpCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['5000EmpCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Empl_pop'][0] == pytest.approx(1188), "Incorrect value in row 0"
    
    assert jts_df['Empl_pop'][32843] == pytest.approx(1189), "Incorrect value in last row"
    
    assert jts_df['Empl_pop'][len(jts_df)-2] == pytest.approx(838), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0502():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'primary', sheet = '2019')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'PS_pop', 'PSPTt',
           'PSPT15n', 'PSPT30n', 'PSPT45n', 'PSPT60n', 'PSPT15pct',
           'PSPT30pct', 'PSPT45pct', 'PSPT60pct', 'PSCyct', 'PSCyc15n',
           'PSCyc30n', 'PSCyc45n', 'PSCyc60n', 'PSCyc15pct', 'PSCyc30pct',
           'PSCyc45pct', 'PSCyc60pct', 'PSCart', 'PSCar15n', 'PSCar30n',
           'PSCar45n', 'PSCar60n', 'PSCar15pct', 'PSCar30pct', 'PSCar45pct',
           'PSCar60pct', 'PSWalkt', 'PSWalk15n', 'PSWalk30n', 'PSWalk45n',
           'PSWalk60n', 'PSWalk15pct', 'PSWalk30pct', 'PSWalk45pct',
           'PSWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['PSWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['PSWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['PSWalk60pct'][len(jts_df)-2] == pytest.approx(99.670549476409, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['PS_pop'][0] == pytest.approx(123), "Incorrect value in row 0"
    
    assert jts_df['PS_pop'][32843] == pytest.approx(28), "Incorrect value in last row"
    
    assert jts_df['PS_pop'][len(jts_df)-2] == pytest.approx(58), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'primary', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'PS_pop', 'PSPTt',
           'PSPT15n', 'PSPT30n', 'PSPT45n', 'PSPT60n', 'PSPT15pct',
           'PSPT30pct', 'PSPT45pct', 'PSPT60pct', 'PSCyct', 'PSCyc15n',
           'PSCyc30n', 'PSCyc45n', 'PSCyc60n', 'PSCyc15pct', 'PSCyc30pct',
           'PSCyc45pct', 'PSCyc60pct', 'PSCart', 'PSCar15n', 'PSCar30n',
           'PSCar45n', 'PSCar60n', 'PSCar15pct', 'PSCar30pct', 'PSCar45pct',
           'PSCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['PSCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['PSCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['PSCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['PS_pop'][0] == pytest.approx(56), "Incorrect value in row 0"
    
    assert jts_df['PS_pop'][32843] == pytest.approx(24), "Incorrect value in last row"
    
    assert jts_df['PS_pop'][len(jts_df)-2] == pytest.approx(51), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    

def test_jts0503():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'secondary', sheet = '2019')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'SS_pop', 'SSPTt',
           'SSPT15n', 'SSPT30n', 'SSPT45n', 'SSPT60n', 'SSPT15pct',
           'SSPT30pct', 'SSPT45pct', 'SSPT60pct', 'SSCyct', 'SSCyc15n',
           'SSCyc30n', 'SSCyc45n', 'SSCyc60n', 'SSCyc15pct', 'SSCyc30pct',
           'SSCyc45pct', 'SSCyc60pct', 'SSCart', 'SSCar15n', 'SSCar30n',
           'SSCar45n', 'SSCar60n', 'SSCar15pct', 'SSCar30pct', 'SSCar45pct',
           'SSCar60pct', 'SSWalkt', 'SSWalk15n', 'SSWalk30n', 'SSWalk45n',
           'SSWalk60n', 'SSWalk15pct', 'SSWalk30pct', 'SSWalk45pct',
           'SSWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['SSWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['SSWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['SSWalk60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['SS_pop'][0] == pytest.approx(56), "Incorrect value in row 0"
    
    assert jts_df['SS_pop'][32843] == pytest.approx(14), "Incorrect value in last row"
    
    assert jts_df['SS_pop'][len(jts_df)-2] == pytest.approx(26), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'secondary', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'SS_pop', 'SSPTt',
           'SSPT15n', 'SSPT30n', 'SSPT45n', 'SSPT60n', 'SSPT15pct',
           'SSPT30pct', 'SSPT45pct', 'SSPT60pct', 'SSCyct', 'SSCyc15n',
           'SSCyc30n', 'SSCyc45n', 'SSCyc60n', 'SSCyc15pct', 'SSCyc30pct',
           'SSCyc45pct', 'SSCyc60pct', 'SSCart', 'SSCar15n', 'SSCar30n',
           'SSCar45n', 'SSCar60n', 'SSCar15pct', 'SSCar30pct', 'SSCar45pct',
           'SSCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['SSCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['SSCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['SSCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['SS_pop'][0] == pytest.approx(26), "Incorrect value in row 0"
    
    assert jts_df['SS_pop'][32843] == pytest.approx(25), "Incorrect value in last row"
    
    assert jts_df['SS_pop'][len(jts_df)-2] == pytest.approx(42), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0504():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'further', sheet = '2019')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'FE_pop', 'FEPTt',
           'FEPT15n', 'FEPT30n', 'FEPT45n', 'FEPT60n', 'FEPT15pct',
           'FEPT30pct', 'FEPT45pct', 'FEPT60pct', 'FECyct', 'FECyc15n',
           'FECyc30n', 'FECyc45n', 'FECyc60n', 'FECyc15pct', 'FECyc30pct',
           'FECyc45pct', 'FECyc60pct', 'FECart', 'FECar15n', 'FECar30n',
           'FECar45n', 'FECar60n', 'FECar15pct', 'FECar30pct', 'FECar45pct',
           'FECar60pct', 'FEWalkt', 'FEWalk15n', 'FEWalk30n', 'FEWalk45n',
           'FEWalk60n', 'FEWalk15pct', 'FEWalk30pct', 'FEWalk45pct',
           'FEWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['FEWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FEWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FEWalk60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['FE_pop'][0] == pytest.approx(26), "Incorrect value in row 0"
    
    assert jts_df['FE_pop'][32843] == pytest.approx(20), "Incorrect value in last row"
    
    assert jts_df['FE_pop'][len(jts_df)-2] == pytest.approx(22), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'further', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'FE_pop', 'FEPTt',
           'FEPT15n', 'FEPT30n', 'FEPT45n', 'FEPT60n', 'FEPT15pct',
           'FEPT30pct', 'FEPT45pct', 'FEPT60pct', 'FECyct', 'FECyc15n',
           'FECyc30n', 'FECyc45n', 'FECyc60n', 'FECyc15pct', 'FECyc30pct',
           'FECyc45pct', 'FECyc60pct', 'FECart', 'FECar15n', 'FECar30n',
           'FECar45n', 'FECar60n', 'FECar15pct', 'FECar30pct', 'FECar45pct',
           'FECar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['FECar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FECar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FECar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['FE_pop'][0] == pytest.approx(22), "Incorrect value in row 0"
    
    assert jts_df['FE_pop'][32843] == pytest.approx(27), "Incorrect value in last row"
    
    assert jts_df['FE_pop'][len(jts_df)-2] == pytest.approx(53), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0505():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'gp', sheet = '2019')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'GP_pop', 'GPPTt',
           'GPPT15n', 'GPPT30n', 'GPPT45n', 'GPPT60n', 'GPPT15pct',
           'GPPT30pct', 'GPPT45pct', 'GPPT60pct', 'GPCyct', 'GPCyc15n',
           'GPCyc30n', 'GPCyc45n', 'GPCyc60n', 'GPCyc15pct', 'GPCyc30pct',
           'GPCyc45pct', 'GPCyc60pct', 'GPCart', 'GPCar15n', 'GPCar30n',
           'GPCar45n', 'GPCar60n', 'GPCar15pct', 'GPCar30pct', 'GPCar45pct',
           'GPCar60pct', 'GPWalkt', 'GPWalk15n', 'GPWalk30n', 'GPWalk45n',
           'GPWalk60n', 'GPWalk15pct', 'GPWalk30pct', 'GPWalk45pct',
           'GPWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['GPWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['GPWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['GPWalk60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['GP_pop'][0] == pytest.approx(863.21459197998), "Incorrect value in row 0"
    
    assert jts_df['GP_pop'][32843] == pytest.approx(894.036071777344), "Incorrect value in last row"
    
    assert jts_df['GP_pop'][len(jts_df)-2] == pytest.approx(601.734466552734), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'gp', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'GP_pop', 'GPPTt',
           'GPPT15n', 'GPPT30n', 'GPPT45n', 'GPPT60n', 'GPPT15pct',
           'GPPT30pct', 'GPPT45pct', 'GPPT60pct', 'GPCyct', 'GPCyc15n',
           'GPCyc30n', 'GPCyc45n', 'GPCyc60n', 'GPCyc15pct', 'GPCyc30pct',
           'GPCyc45pct', 'GPCyc60pct', 'GPCart', 'GPCar15n', 'GPCar30n',
           'GPCar45n', 'GPCar60n', 'GPCar15pct', 'GPCar30pct', 'GPCar45pct',
           'GPCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['GPCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['GPCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['GPCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['GP_pop'][0] == pytest.approx(809), "Incorrect value in row 0"
    
    assert jts_df['GP_pop'][32843] == pytest.approx(854), "Incorrect value in last row"
    
    assert jts_df['GP_pop'][len(jts_df)-2] == pytest.approx(574), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0506():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'hospital', sheet = '2019')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Hosp_pop', 'HospPTt',
           'HospPT15n', 'HospPT30n', 'HospPT45n', 'HospPT60n', 'HospPT15pct',
           'HospPT30pct', 'HospPT45pct', 'HospPT60pct', 'HospCyct',
           'HospCyc15n', 'HospCyc30n', 'HospCyc45n', 'HospCyc60n',
           'HospCyc15pct', 'HospCyc30pct', 'HospCyc45pct', 'HospCyc60pct',
           'HospCart', 'HospCar15n', 'HospCar30n', 'HospCar45n', 'HospCar60n',
           'HospCar15pct', 'HospCar30pct', 'HospCar45pct', 'HospCar60pct',
           'HospWalkt', 'HospWalk15n', 'HospWalk30n', 'HospWalk45n',
           'HospWalk60n', 'HospWalk15pct', 'HospWalk30pct', 'HospWalk45pct',
           'HospWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['HospWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['HospWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['HospWalk60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Hosp_pop'][0] == pytest.approx(863.21459197998), "Incorrect value in row 0"
    
    assert jts_df['Hosp_pop'][32843] == pytest.approx(894.036071777344), "Incorrect value in last row"
    
    assert jts_df['Hosp_pop'][len(jts_df)-2] == pytest.approx(601.734466552734), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'hospital', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Hosp_pop', 'HospPTt',
           'HospPT15n', 'HospPT30n', 'HospPT45n', 'HospPT60n', 'HospPT15pct',
           'HospPT30pct', 'HospPT45pct', 'HospPT60pct', 'HospCyct',
           'HospCyc15n', 'HospCyc30n', 'HospCyc45n', 'HospCyc60n',
           'HospCyc15pct', 'HospCyc30pct', 'HospCyc45pct', 'HospCyc60pct',
           'HospCart', 'HospCar15n', 'HospCar30n', 'HospCar45n', 'HospCar60n',
           'HospCar15pct', 'HospCar30pct', 'HospCar45pct', 'HospCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['HospCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['HospCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['HospCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Hosp_pop'][0] == pytest.approx(809), "Incorrect value in row 0"
    
    assert jts_df['Hosp_pop'][32843] == pytest.approx(854), "Incorrect value in last row"
    
    assert jts_df['Hosp_pop'][len(jts_df)-2] == pytest.approx(574), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0507():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'food', sheet = '2019')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Food_pop', 'FoodPTt',
           'FoodPT15n', 'FoodPT30n', 'FoodPT45n', 'FoodPT60n', 'FoodPT15pct',
           'FoodPT30pct', 'FoodPT45pct', 'FoodPT60pct', 'FoodCyct',
           'FoodCyc15n', 'FoodCyc30n', 'FoodCyc45n', 'FoodCyc60n',
           'FoodCyc15pct', 'FoodCyc30pct', 'FoodCyc45pct', 'FoodCyc60pct',
           'FoodCart', 'FoodCar15n', 'FoodCar30n', 'FoodCar45n', 'FoodCar60n',
           'FoodCar15pct', 'FoodCar30pct', 'FoodCar45pct', 'FoodCar60pct',
           'FoodWalkt', 'FoodWalk15n', 'FoodWalk30n', 'FoodWalk45n',
           'FoodWalk60n', 'FoodWalk15pct', 'FoodWalk30pct', 'FoodWalk45pct',
           'FoodWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['FoodWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FoodWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FoodWalk60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Food_pop'][0] == pytest.approx(863.21459197998), "Incorrect value in row 0"
    
    assert jts_df['Food_pop'][32843] == pytest.approx(894.036071777344), "Incorrect value in last row"
    
    assert jts_df['Food_pop'][len(jts_df)-2] == pytest.approx(601.734466552734), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'food', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Food_pop', 'FoodPTt',
           'FoodPT15n', 'FoodPT30n', 'FoodPT45n', 'FoodPT60n', 'FoodPT15pct',
           'FoodPT30pct', 'FoodPT45pct', 'FoodPT60pct', 'FoodCyct',
           'FoodCyc15n', 'FoodCyc30n', 'FoodCyc45n', 'FoodCyc60n',
           'FoodCyc15pct', 'FoodCyc30pct', 'FoodCyc45pct', 'FoodCyc60pct',
           'FoodCart', 'FoodCar15n', 'FoodCar30n', 'FoodCar45n', 'FoodCar60n',
           'FoodCar15pct', 'FoodCar30pct', 'FoodCar45pct', 'FoodCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['FoodCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['FoodCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['FoodCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Food_pop'][0] == pytest.approx(809), "Incorrect value in row 0"
    
    assert jts_df['Food_pop'][32843] == pytest.approx(854), "Incorrect value in last row"
    
    assert jts_df['Food_pop'][len(jts_df)-2] == pytest.approx(574), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0508():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'town', sheet = '2019')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Town_pop', 'TownPTt',
           'TownPT15n', 'TownPT30n', 'TownPT45n', 'TownPT60n', 'TownPT15pct',
           'TownPT30pct', 'TownPT45pct', 'TownPT60pct', 'TownCyct',
           'TownCyc15n', 'TownCyc30n', 'TownCyc45n', 'TownCyc60n',
           'TownCyc15pct', 'TownCyc30pct', 'TownCyc45pct', 'TownCyc60pct',
           'TownCart', 'TownCar15n', 'TownCar30n', 'TownCar45n', 'TownCar60n',
           'TownCar15pct', 'TownCar30pct', 'TownCar45pct', 'TownCar60pct',
           'TownWalkt', 'TownWalk15n', 'TownWalk30n', 'TownWalk45n',
           'TownWalk60n', 'TownWalk15pct', 'TownWalk30pct', 'TownWalk45pct',
           'TownWalk60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['TownWalk60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['TownWalk60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['TownWalk60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Town_pop'][0] == pytest.approx(863.21459197998), "Incorrect value in row 0"
    
    assert jts_df['Town_pop'][32843] == pytest.approx(894.036071777344), "Incorrect value in last row"
    
    assert jts_df['Town_pop'][len(jts_df)-2] == pytest.approx(601.734466552734), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'town', sheet = '2014')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Town_pop', 'TownPTt',
           'TownPT15n', 'TownPT30n', 'TownPT45n', 'TownPT60n', 'TownPT15pct',
           'TownPT30pct', 'TownPT45pct', 'TownPT60pct', 'TownCyct',
           'TownCyc15n', 'TownCyc30n', 'TownCyc45n', 'TownCyc60n',
           'TownCyc15pct', 'TownCyc30pct', 'TownCyc45pct', 'TownCyc60pct',
           'TownCart', 'TownCar15n', 'TownCar30n', 'TownCar45n', 'TownCar60n',
           'TownCar15pct', 'TownCar30pct', 'TownCar45pct', 'TownCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['TownCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['TownCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['TownCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Town_pop'][0] == pytest.approx(809), "Incorrect value in row 0"
    
    assert jts_df['Town_pop'][32843] == pytest.approx(854), "Incorrect value in last row"
    
    assert jts_df['Town_pop'][len(jts_df)-2] == pytest.approx(574), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
def test_jts0509():
    
    jts_df =jts.get_jts(type_code = 'jts05', spec = 'pharmacies', sheet = '2015')
    assert (jts_df.columns.values == ['LSOA_code', 'Region', 'LA_Code', 'LA_Name', 'Ph_pop', 'PhCyct',
           'PhCyc15n', 'PhCyc30n', 'PhCyc45n', 'PhCyc60n', 'PhCyc15pct',
           'PhCyc30pct', 'PhCyc45pct', 'PhCyc60pct', 'PhCart', 'PhCar15n',
           'PhCar30n', 'PhCar45n', 'PhCar60n', 'PhCar15pct', 'PhCar30pct',
           'PhCar45pct', 'PhCar60pct']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['PhCar60pct'][0] == pytest.approx(100, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['PhCar60pct'][32843] == pytest.approx(100, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['PhCar60pct'][len(jts_df)-2] == pytest.approx(100, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    assert jts_df['Ph_pop'][0] == pytest.approx(999), "Incorrect value in row 0"
    
    assert jts_df['Ph_pop'][32843] == pytest.approx(865), "Incorrect value in last row"
    
    assert jts_df['Ph_pop'][len(jts_df)-2] == pytest.approx(583), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
def test_jts0901():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'airports', sheet = 'JTS0901_Nearest')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority',
           'Nearest airport by travel time (by public transport',
           'Average travel time (minutes, by public transport)',
           'Nearest airport by travel time (by car)',
           'Average travel time (minutes, by car)']).all(), "Column names incorrect"
    
    assert len(jts_df) == 128, "Incorrect number of rows in data frame"
    
    assert jts_df['Average travel time (minutes, by car)'][0] == pytest.approx(79.5136648986137, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['Average travel time (minutes, by car)'][127] == pytest.approx(81.2457301073894, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Average travel time (minutes, by car)'][len(jts_df)-2] == pytest.approx(130.486163541346, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    assert jts_df['Average travel time (minutes, by public transport)'][0] == pytest.approx(108.269654376754), "Incorrect value in row 0"
    assert jts_df['Average travel time (minutes, by public transport)'][127] == pytest.approx(120.285701174995), "Incorrect value in last row"
    assert jts_df['Average travel time (minutes, by public transport)'][len(jts_df)-2] == pytest.approx(163.998773114274), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'airports', sheet = 'JTS0901_Selected')
    
    assert len(jts_df) == 128, "Incorrect number of rows in data frame"
    
    assert jts_df['Heathrow T2 by public transport'][0] == pytest.approx(240, rel = 0.01), "Incorrect value in row 0"
    
    assert jts_df['Heathrow T2 by public transport'][127] == pytest.approx(153.791211815982, rel = 0.01), "Incorrect value in last row"
    
    assert jts_df['Heathrow T2 by public transport'][len(jts_df)-2] == pytest.approx(240, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Leeds by car'][0] == pytest.approx(94.6353632732069), "Incorrect value in row 0"
    assert jts_df['Leeds by car'][127] == pytest.approx(240), "Incorrect value in last row"
    assert jts_df['Leeds by car'][len(jts_df)-2] == pytest.approx(240), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    
def test_jts0902():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'airports', sheet = 'JTS0902')
    assert (jts_df.columns.values == ['Ref', 'Airport name',
           'People within 30 minutes by public transport',
           'People within 60 minutes by public transport',
           'People within 120 minutes by public transport',
           'People within 30 minutes by car',
           'People within 60 minutes by car',
           'People within 120 minutes by car',
           '%People within 20km and within 30 minutes by public transport',
           '%People within 20km and within 60 minutes by public transport',
           '%People within 20km and within 120 minutes by public transport',
           '%People within 20km and within 30 minutes by car',
           '%People within 20km and within 60 minutes by car',
           '%People within 20km and within 120 minutes by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32, "Incorrect number of rows in data frame"
    
    assert jts_df['People within 30 minutes by public transport'][0] == pytest.approx(0.102901, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['People within 30 minutes by public transport'][31] == pytest.approx(0.039852, rel = 0.01), "Incorrect value in last row"
    assert jts_df['People within 30 minutes by public transport'][len(jts_df)-2] == pytest.approx(0.011929, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['%People within 20km and within 120 minutes by car'][0] == pytest.approx(99.8412998415507), "Incorrect value in row 0"
    assert jts_df['%People within 20km and within 120 minutes by car'][31] == pytest.approx(100), "Incorrect value in last row"
    assert jts_df['%People within 20km and within 120 minutes by car'][len(jts_df)-2] == pytest.approx(99.3720022436668), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0903():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'airports', sheet = 'JTS0903')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority', 'Population',
           '%People within 30 minutes by public transport',
           '%People within 60 minutes by public transport',
           '%People within 120 minutes by public transport',
           '%People within 30 minutes by car', '%People within 60 minutes by car',
           '%People within 120 minutes by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 130, "Incorrect number of rows in data frame"
    
    assert jts_df['Population'][0] == pytest.approx(54786.327, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Population'][129] == pytest.approx(486.093, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Population'][len(jts_df)-2] == pytest.approx(133.373, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['%People within 120 minutes by car'][0] == pytest.approx(93.1806032552611), "Incorrect value in row 0"
    assert jts_df['%People within 120 minutes by car'][129] == pytest.approx(99.7294756353208), "Incorrect value in last row"
    assert jts_df['%People within 120 minutes by car'][len(jts_df)-2] == pytest.approx(0), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0904():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'airports', sheet = 'JTS0904')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority Area', 'Local Authority Name',
           'Number airports within 30 mins by public transport',
           'Number airports within 60 mins by public transport',
           'Number airports within 120 mins by public transport',
           'Number airports within 30 mins by car',
           'Number airports within 60 mins by car',
           'Number airports within 120 mins by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 129, "Incorrect number of rows in data frame"
    
    assert jts_df['Number airports within 30 mins by public transport'][0] == pytest.approx(0.0211512443129884, abs = 0.03), "Incorrect value in row 0"
    assert jts_df['Number airports within 30 mins by public transport'][128] == pytest.approx(0, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Number airports within 30 mins by public transport'][len(jts_df)-2] == pytest.approx(0, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Number airports within 120 mins by car'][0] == pytest.approx(1.2938127066727, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Number airports within 120 mins by car'][128] == pytest.approx(6.00246660618441, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Number airports within 120 mins by car'][len(jts_df)-2] == pytest.approx(1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0905():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'airports', sheet = 'JTS0905_Selected')
    assert (jts_df.columns.values == ['LSOA Code', 'LSOA Name', 'Upper tier local authority code',
           'Upper tier local authority name', 'LSOA population (2015)',
           'Heathrow T2 by public transport',
           'Heathrow T3 by public transport',
           'Heathrow T4 by public transport',
           'Heathrow T5 by public transport',
           'Gatwick North Terminal by public transport',
           'Gatwick South Terminal by public transport',
           'Manchester T1 by public transport',
           'Manchester T2 by public transport',
           'Manchester T3 by public transport',
           'Stansted by public transport', 'Luton by public transport',
           'Birmingham by public transport', 'Bristol by public transport',
           'Liverpool John Lennon by public transport',
           'Newcastle by public transport',
           'East Midlands by public transport',
           'London City by public transport', 'Leeds by public transport',
           'Heathrow T2 by car', 'Heathrow T3 by car', 'Heathrow T4 by car',
           'Heathrow T5 by car', 'Gatwick North Terminal by car',
           'Gatwick South Terminal by car', 'Manchester T1 by car',
           'Manchester T2 by car', 'Manchester T3 by car', 'Stansted by car',
           'Luton by car', 'Birmingham by car', 'Bristol by car',
           'Liverpool John Lennon by car', 'Newcastle by car',
           'East Midlands by car', 'London City by car', 'Leeds by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['Heathrow T2 by public transport'][0] == pytest.approx(51.46, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Heathrow T2 by public transport'][32843] == pytest.approx(240, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Heathrow T2 by public transport'][len(jts_df)-2] == pytest.approx(240, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Leeds by car'][0] == pytest.approx(240, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Leeds by car'][32843] == pytest.approx(125.68, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Leeds by car'][len(jts_df)-2] == pytest.approx(128.67), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'airports', sheet = 'JTS0905_Summary')
    assert (jts_df.columns.values == ['LSOA Code', 'LSOA Name', 'Upper tier local authority code',
           'Upper tier local authority name', 'LSOA population (2015)',
           'Nearest airport by public transport/walking travel time',
           'Average minimum journey time by public transport/walking',
           'Nearest airport by car time', 'Average minimum journey by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['LSOA population (2015)'][0] == pytest.approx(1639, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['LSOA population (2015)'][32843] == pytest.approx(1253, rel = 0.01), "Incorrect value in last row"
    assert jts_df['LSOA population (2015)'][len(jts_df)-2] == pytest.approx(1045, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average minimum journey by car'][0] == pytest.approx(31.25, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Average minimum journey by car'][32843] == pytest.approx(24.59, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average minimum journey by car'][len(jts_df)-2] == pytest.approx(22.52), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"


def test_jts0921():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0921_Nearest')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority', 'Local Authority Name',
           'Nearest station by public transport/walking',
           'Average travel time by public transport/walking',
           'Nearest station by car', 'Average travel time by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 120, "Incorrect number of rows in data frame"
    
    assert jts_df['Average travel time by public transport/walking'][0] == pytest.approx(25.0198728163714, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Average travel time by public transport/walking'][119] == pytest.approx(95.2230216074373, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average travel time by public transport/walking'][len(jts_df)-2] == pytest.approx(132.113207684715, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average travel time by car'][0] == pytest.approx(12.2928389110818, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Average travel time by car'][119] == pytest.approx(69.7998686821597, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average travel time by car'][len(jts_df)-2] == pytest.approx(142.607107135627), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'car')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority', 'Birmingham New Street',
           'Birmingham Moor Street', 'Liverpool Lime Street',
           'Manchester Piccadilly', 'Manchester Victoria',
           'Bristol Temple Meads', 'Crewe', 'Doncaster', 'Gatwick Airport',
           'Leeds', 'Newcastle', 'Preston', 'Reading', 'Stockport', 'York',
           'Ashford International', 'Basingstoke', 'Billericay',
           'Birmingham International', 'Brighton', 'Bristol Parkway',
           'Cambridge', 'Carlisle', 'Chelmsford', 'Colchester', 'Coventry',
           'Darlington', 'Didcot Parkway', 'Ebbsfleet International',
           'Gatwick Airport', 'Guildford', 'Haywards Heath', 'Huddersfield',
           'Hull', 'Ipswich', 'Lancaster', 'Liverpool South Parkway',
           'Manchester Airport', 'Milton Keynes Central', 'Newark North Gate',
           'Norwich', 'Nottingham', 'Oxford', 'Peterborough', 'Sevenoaks',
           'Sheffield', 'Southampton Central', 'Stansted Airport',
           'Tonbridge', 'Wakefield Westgate', 'Warrington Bank Quay',
           'Watford Junction', 'Wigan North Western', 'Winchester', 'Woking',
           'Wolverhampton', 'Clapham Junction', 'Stratford (London)',
           'Barking', 'Bromley South', 'East Croydon',
           'Richmond (Greater London)', 'Romford', 'Wimbledon',
           'London Blackfriars', 'London Bridge', 'London Cannon Street',
           'London Charing Cross', 'London Euston', 'London Fenchurch Street',
           'London Kings Cross', 'London Liverpool Street',
           'London Marylebone', 'London Paddington', 'London St Pancras',
           'London Victoria', 'London Waterloo', 'London Waterloo East',
           'Vauxhall']).all(), "Column names incorrect"
    
    assert len(jts_df) == 120, "Incorrect number of rows in data frame"
    
    assert jts_df['Liverpool Lime Street'][0] == pytest.approx(195.900927800814, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Liverpool Lime Street'][119] == pytest.approx(230.351396025749, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Liverpool Lime Street'][len(jts_df)-3] == pytest.approx(235.059635246245, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Wigan North Western'][0] == pytest.approx(174.838248488931, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Wigan North Western'][119] == pytest.approx(230.394012637028, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Wigan North Western'][len(jts_df)-3] == pytest.approx(229.577610277515), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'PT')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority', 'Birmingham New Street',
           'Birmingham Moor Street', 'Liverpool Lime Street',
           'Manchester Piccadilly', 'Manchester Victoria',
           'Bristol Temple Meads', 'Crewe', 'Doncaster', 'Gatwick Airport',
           'Leeds', 'Newcastle', 'Preston', 'Reading', 'Stockport', 'York',
           'Ashford International', 'Basingstoke', 'Billericay',
           'Birmingham International', 'Brighton', 'Bristol Parkway',
           'Cambridge', 'Carlisle', 'Chelmsford', 'Colchester', 'Coventry',
           'Darlington', 'Didcot Parkway', 'Ebbsfleet International',
           'Gatwick Airport', 'Guildford', 'Haywards Heath', 'Huddersfield',
           'Hull', 'Ipswich', 'Lancaster', 'Liverpool South Parkway',
           'Manchester Airport', 'Milton Keynes Central', 'Newark North Gate',
           'Norwich', 'Nottingham', 'Oxford', 'Peterborough', 'Sevenoaks',
           'Sheffield', 'Southampton Central', 'Stansted Airport',
           'Tonbridge', 'Wakefield Westgate', 'Warrington Bank Quay',
           'Watford Junction', 'Wigan North Western', 'Winchester', 'Woking',
           'Wolverhampton', 'Clapham Junction', 'Stratford (London)',
           'Barking', 'Bromley South', 'East Croydon',
           'Richmond (Greater London)', 'Romford', 'Wimbledon',
           'London Blackfriars', 'London Bridge', 'London Cannon Street',
           'London Charing Cross', 'London Euston', 'London Fenchurch Street',
           'London Kings Cross', 'London Liverpool Street',
           'London Marylebone', 'London Paddington', 'London St Pancras',
           'London Victoria', 'London Waterloo', 'London Waterloo East',
           'Vauxhall']).all(), "Column names incorrect"
    
    assert len(jts_df) == 120, "Incorrect number of rows in data frame"
    
    assert jts_df['Manchester Piccadilly'][0] == pytest.approx(136.7523196812, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Manchester Piccadilly'][119] == pytest.approx(240, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Manchester Piccadilly'][len(jts_df)-4] == pytest.approx(184.399993896484, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Wakefield Westgate'][0] == pytest.approx(109.397932610622, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Wakefield Westgate'][119] == pytest.approx(240, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Wakefield Westgate'][len(jts_df)-9] == pytest.approx(170.687967523298), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    

def test_jts0922():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0922')
    assert (jts_df.columns.values == ['Ref', 'Rail station name',
           'People within 30 mins of the station by public transport',
           'People within 60 mins of the station by public transport',
           'People within 120 mins of the station by public transport',
           'People within 30 mins of the station by car',
           'People within 60 mins of the station by car',
           'People within 120 mins of the station by car',
           '%People within 20km and 30 mins of the station by public transport',
           '%People within 20km and 60 mins of the station by public transport',
           '%People within 20km and 120 mins of the station by public transport',
           '%People within 20km and 30 mins of the station by car',
           '%People within 20km and 60 mins of the station by car',
           '%People within 20km and 120 mins of the station by car',
           'Population within 20km']).all(), "Column names incorrect"
    
    assert len(jts_df) == 79, "Incorrect number of rows in data frame"
    
    assert jts_df['People within 30 mins of the station by public transport'][0] == pytest.approx(0.093243, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['People within 30 mins of the station by public transport'][78] == pytest.approx(0.1628, rel = 0.01), "Incorrect value in last row"
    assert jts_df['People within 30 mins of the station by public transport'][len(jts_df)-2] == pytest.approx(0.242376, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Population within 20km'][0] == pytest.approx(0.237291, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Population within 20km'][78] == pytest.approx(0.303024, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Population within 20km'][len(jts_df)-2] == pytest.approx(1.844361), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0923():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0923')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority', 'Local Authority Name', 'Population',
           '%People within 30 mins to stations by public transport',
           '%People within 60 mins to stations by public transport',
           '%People within 120 mins to stations by public transport',
           '%People within 30 mins to stations by car',
           '%People within 60 mins to stations by car',
           '%People within 120 mins to stations by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 130, "Incorrect number of rows in data frame"
    
    assert jts_df['%People within 30 mins to stations by public transport'][0] == pytest.approx(22.7474146971013, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['%People within 30 mins to stations by public transport'][129] == pytest.approx(0, rel = 0.01), "Incorrect value in last row"
    assert jts_df['%People within 30 mins to stations by public transport'][len(jts_df)-2] == pytest.approx(0, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['%People within 120 mins to stations by car'][0] == pytest.approx(97.1068274023918, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['%People within 120 mins to stations by car'][129] == pytest.approx(99.7294756353208, rel = 0.01), "Incorrect value in last row"
    assert jts_df['%People within 120 mins to stations by car'][len(jts_df)-2] == pytest.approx(0), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0924():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0924')
    assert (jts_df.columns.values == ['LA Code', 'Local Authority', 'Local Authority Name',
           'Number of stations within 30  mins by public transport',
           'Number of stations within 60  mins by public transport',
           'Number of stations within 120  mins by public transport',
           'Number of stations within 30  mins by car',
           'Number of stations within 60  mins by car',
           'Number of stations within 120  mins by car']).all(), "Column names incorrect"
    
    assert len(jts_df) == 129, "Incorrect number of rows in data frame"
    
    assert jts_df['Number of stations within 30  mins by public transport'][0] == pytest.approx(0.0955010266244155, rel = 0.1), "Incorrect value in row 0"
    assert jts_df['Number of stations within 30  mins by public transport'][128] == pytest.approx(0, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Number of stations within 30  mins by public transport'][len(jts_df)-2] == pytest.approx(0, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Number of stations within 120  mins by car'][0] == pytest.approx(3.49484630352344, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Number of stations within 120  mins by car'][128] == pytest.approx(9.79099678456592, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Number of stations within 120  mins by car'][len(jts_df)-2] == pytest.approx(0), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0925():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0925_Selected')
    assert (jts_df.columns.values == ['LSOA Code', 'LSOA Name', 'Upper tier local authority code',
           'Upper tier local authority name', 'LSOA population (2015)', 'BHM',
           'LIV', 'MAN', 'BRI', 'CRE', 'DON', 'GTW', 'LDS', 'NCL', 'PRE',
           'RDG', 'SPT', 'YRK', 'BFR', 'LBG', 'CST', 'CHX', 'EUS', 'FST',
           'KGX', 'LST', 'MYB', 'PAD', 'SPL', 'VIC', 'WAT', 'BMO', 'MCV',
           'ASI', 'BSK', 'BIC', 'BHI', 'BTN', 'BPW', 'CBG', 'CAR', 'CHM',
           'COL', 'COV', 'DAR', 'DID', 'EBF', 'GRA', 'GLD', 'HHE', 'HUD',
           'HUL', 'IPS', 'LAN', 'LPY', 'MIA', 'MKC', 'NNG', 'NRW', 'NOT',
           'OXF', 'PBO', 'SEV', 'SHF', 'SOU', 'SSD', 'TON', 'WKF', 'WBQ',
           'WFJ', 'WGN', 'WIN', 'WOK', 'WVH', 'CLJ', 'SRA', 'BKG', 'BMS',
           'ECR', 'RMD', 'RMF', 'WIM', 'WAE', 'VXH']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['BHM'][0] == pytest.approx(111.88, rel = 0.1), "Incorrect value in row 0"
    assert jts_df['BHM'][32843] == pytest.approx(131.69, rel = 0.01), "Incorrect value in last row"
    assert jts_df['BHM'][len(jts_df)-2] == pytest.approx(139.18, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['VXH'][0] == pytest.approx(30.83, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['VXH'][32843] == pytest.approx(240, rel = 0.01), "Incorrect value in last row"
    assert jts_df['VXH'][len(jts_df)-23] == pytest.approx(34.5), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0925_Summary')
    assert (jts_df.columns.values == ['LSOA Code', 'LSOA Name', 'Upper tier local authority code',
           'Upper tier local authority name', 'LSOA population (2015)',
           'Nearest station by travel time', 'Average travel time (minutes)']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['Nearest station by travel time'][0] == 'BFR', "Incorrect value in row 0"
    assert jts_df['Nearest station by travel time'][32843] == 'LIV', "Incorrect value in last row"
    assert jts_df['Nearest station by travel time'][len(jts_df)-2] == 'LIV', "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average travel time (minutes)'][0] == pytest.approx(15.83, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Average travel time (minutes)'][32843] == pytest.approx(16.61, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average travel time (minutes)'][len(jts_df)-2] == pytest.approx(24.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0926():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0926_Selected')
    assert (jts_df.columns.values == ['LSOA Code', 'LSOA Name', 'Upper tier local authority code',
           'Upper tier local authority name', 'LSOA population (2015)', 'BHM',
           'LIV', 'MAN', 'BRI', 'CRE', 'DON', 'GTW', 'LDS', 'NCL', 'PRE',
           'RDG', 'SPT', 'YRK', 'BFR', 'LBG', 'CST', 'CHX', 'EUS', 'FST',
           'KGX', 'LST', 'MYB', 'PAD', 'SPL', 'VIC', 'WAT', 'BMO', 'MCV',
           'ASI', 'BSK', 'BIC', 'BHI', 'BTN', 'BPW', 'CBG', 'CAR', 'CHM',
           'COL', 'COV', 'DAR', 'DID', 'EBF', 'GRA', 'GLD', 'HHE', 'HUD',
           'HUL', 'IPS', 'LAN', 'LPY', 'MIA', 'MKC', 'NNG', 'NRW', 'NOT',
           'OXF', 'PBO', 'SEV', 'SHF', 'SOU', 'SSD', 'TON', 'WKF', 'WBQ',
           'WFJ', 'WGN', 'WIN', 'WOK', 'WVH', 'CLJ', 'SRA', 'BKG', 'BMS',
           'ECR', 'RMD', 'RMF', 'WIM', 'WAE', 'VXH']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['BHM'][0] == pytest.approx(197.01, rel = 0.1), "Incorrect value in row 0"
    assert jts_df['BHM'][32843] == pytest.approx(152.78, rel = 0.01), "Incorrect value in last row"
    assert jts_df['BHM'][len(jts_df)-2] == pytest.approx(155.77, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['VXH'][0] == pytest.approx(17.07, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['VXH'][32843] == pytest.approx(240, rel = 0.01), "Incorrect value in last row"
    assert jts_df['VXH'][len(jts_df)-23] == pytest.approx(25.7), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = 'rail', sheet = 'JTS0926_Summary')
    assert (jts_df.columns.values == ['LSOA Code', 'LSOA Name', 'Upper tier local authority code',
           'Upper tier local authority name', 'LSOA population (2015)',
           'Nearest station by travel time', 'Average travel time (minutes)']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['Nearest station by travel time'][0] == 'BFR', "Incorrect value in row 0"
    assert jts_df['Nearest station by travel time'][32843] == 'LIV', "Incorrect value in last row"
    assert jts_df['Nearest station by travel time'][len(jts_df)-2] == 'LIV', "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average travel time (minutes)'][0] == pytest.approx(10.15, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Average travel time (minutes)'][32843] == pytest.approx(10.55, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average travel time (minutes)'][len(jts_df)-2] == pytest.approx(14.08), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
def test_jts0930():
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = '', sheet = 'JTS0930_LA')
    assert (jts_df.columns.values == ['Region', 'LA_Code', 'LA_Name',
           'Average min travel time by PT (minutes)',
           'Average min travel time by Car (minutes)']).all(), "Column names incorrect"
    
    assert len(jts_df) == 361, "Incorrect number of rows in data frame"
    
    assert jts_df['Average min travel time by PT (minutes)'][0] == pytest.approx(53.803420360467, rel = 0.1), "Incorrect value in row 0"
    assert jts_df['Average min travel time by PT (minutes)'][360] == pytest.approx(116.427983456931, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average min travel time by PT (minutes)'][len(jts_df)-2] == pytest.approx(108.936206011987, rel = 0.1), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average min travel time by Car (minutes)'][0] == pytest.approx(28.8876116377259, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Average min travel time by Car (minutes)'][360] == pytest.approx(74.2062107955701, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average min travel time by Car (minutes)'][len(jts_df)-2] == pytest.approx(47.1541742310627), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    
    jts_df =jts.get_jts(type_code = 'jts09', spec = '', sheet = 'JTS0930_LSOA')
    assert (jts_df.columns.values == ['LSOA_Code', 'Region', 'LA_Code', 'LA_Name',
           'Average min travel time by PT (minutes)',
           'Average min travel time by Car (minutes)']).all(), "Column names incorrect"
    
    assert len(jts_df) == 32844, "Incorrect number of rows in data frame"
    
    assert jts_df['Average min travel time by PT (minutes)'][0] == pytest.approx(28.2925503355705), "Incorrect value in row 0"
    assert jts_df['Average min travel time by PT (minutes)'][32843] == pytest.approx(21.4816280925778), "Incorrect value in last row"
    assert jts_df['Average min travel time by PT (minutes)'][len(jts_df)-2] == pytest.approx(23.6060861244019), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    
    assert jts_df['Average min travel time by Car (minutes)'][0] == pytest.approx(17.4665039658328, rel = 0.01), "Incorrect value in row 0"
    assert jts_df['Average min travel time by Car (minutes)'][32843] == pytest.approx(25.7274301675978, rel = 0.01), "Incorrect value in last row"
    assert jts_df['Average min travel time by Car (minutes)'][len(jts_df)-2] == pytest.approx(28.9018277511962), "Incorrect value in second to last row (suggests issue with cleaning of data and incorrect rows numbering)"
    













