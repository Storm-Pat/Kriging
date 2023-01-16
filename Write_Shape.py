import fiona
#reading in function, takes file as an argument
def write_file(df):

    #setting up fiona schema
    schema = {'geometry':'Point','properties':[('Depth_m','float')]}
    #creating a fiona object
    shape = fiona.open('Outputs/output.shp', mode ='w', driver ='ESRI Shapefile', schema=schema, crs ='WGS84')

    #creating points list
    for i,j in df[['Longitude','Latitude']].iterrows():
        rowDict = {'geometry': {'type': 'Point', 'coordinates': (j.Longitude,j.Latitude)}, "properties": {'Depth_m': df.iloc[i,2]}}
        shape.write(rowDict)
    #writing and closing the file
    shape.close()








