import pathlib
import pandas as pd
import geopandas as gp

pd.set_option('display.max_columns', None)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def csvImport(csvPath):
    # Read the csv prediction table to dataframe
    df = pd.read_csv(csvPath)

    # Add an ID field to the table for easier join with shapefile
    df["ID"] = df['Image Name']

    # Query probabilities over 0.98 for water and wildland
    probQuery = df.query("(`Water Probability` >= 0.98) or (`Wildland Probability` >= 0.98)")

    return probQuery

def shpImport(shpPath):
    # Read and create data frame for zipped Firebreak shapefile
    gdf = gp.GeoDataFrame.from_file(shpPath, crs='EPSG:4326', geometry='geometry')

    # Calc and add center point lat/lon column
    gdf["x"] = gdf.centroid.x
    gdf["y"] = gdf.centroid.y

    # Make Break Name values all lowercase for join
    gdf['BREAK_NAME'] = gdf['BREAK_NAME'].map(str.lower)

    return gdf

def joinFilter(csvIn, shpIn):
    # Inner join
    dfJoin = pd.merge(csvIn, shpIn, on='ID', how='inner')

    # Query labels that correct the Firebreak class
    dfFilter = dfJoin.loc[dfJoin['Label'] != dfJoin['BREAK_NAME']]

    return dfFilter

def exportSHP(csvIn, shpOut):
    # Read the csv with lat/long as x/y
    data = pd.read_csv(csvIn)

    # Use geopandas to create a dataframe of csv with x/y points as the geometry
    data_gdf = gp.GeoDataFrame(data, geometry=gp.points_from_xy(data['x'], data['y']))

    # Define CRS for output shp
    ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

    # Write the dataframe to a esri shapefile
    data_gdf.to_file(filename=shpOut, driver='ESRI Shapefile', crs='EPSG:4326')

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Run Script
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#stateList = ['AZ','FL','OK','OR','WA','WY','SD','CO','ID','UT']
stateList = ['NV']

for state in stateList:

    # Define path variable for csv of predictions
    predictionsCSV  = r'D:\Projects\WORKING\ML\prediction_tables\{0}_Results_Table.csv'.format(state)
    predPath        = pathlib.Path(predictionsCSV)
    #print(predPath)

    # Define path variable for zipped firebreak shapefile
    firebreakSHP  = r'D:\Projects\WORKING\ML\vectors\National_WW\{0}_WW_Merge.zip'.format(state)
    firebreakPath = pathlib.Path(firebreakSHP)
    #print(firebreakPath)

    # Create output path variable for output csv
    csvPath = r'D:\Projects\WORKING\ML\vectors\{0}_WW_XY.csv'.format(state)
    gdfCSV  = pathlib.Path(csvPath)
    #print(gdfCSV)

    # Create output path variable for output point shapefile
    shpPath = r'D:\Projects\WORKING\ML\vectors\{0}_WW_XY.shp'.format(state)
    pntSHP  = pathlib.Path(shpPath)
    #print(pntSHP)

    # Call functions as variables
    myCSV  = csvImport(predPath)
    myGDF  = shpImport(firebreakPath)
    myJoin = joinFilter(myCSV, myGDF)

    print(f'Number of records found in prediction csv:\n\t{len(myCSV)}')
    print(f'Number of records found in firebreak shp:\n\t{len(myGDF)}')
    print(f'Number of records found after join & filter:\n\t{len(myJoin)}')
    # print(myCSV.head())
    # print(myGDF.head())
    # print(myJoin.head())
    # print(myJoin.columns.values)

    # Write the geodataframe to a csv and delete geometry field to increase runtime
    myJoin.drop('geometry',axis=1).to_csv(gdfCSV)

    # Output a point shapefile for the csv
    exportSHP(gdfCSV,pntSHP)